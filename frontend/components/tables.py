# Hidrobart Costeo
# frontend/components/tables.py

from nicegui import ui
from typing import List, Dict, Any, Callable
import pandas as pd
from datetime import datetime

class AdvancedDataTable:
    def __init__(self):
        self.table = None
        self.columns: List[Dict[str, str]] = []
        self.data: List[Dict[str, Any]] = []
        self.filtered_data: List[Dict[str, Any]] = []
        self.selected_rows = set()
        self.search_term = ""

    def create_table(self,
                    columns: List[Dict[str, str]],
                    data: List[Dict[str, Any]],
                    title: str = "Tabla de Datos",
                    height: str = "600px",
                    selection: str = "multiple",
                    pagination: bool = True,
                    rows_per_page: int = 10,
                    **kwargs) -> ui.table:
        """
        Crea una tabla avanzada con funcionalidades básicas
        """
        self.columns = columns
        self.data = data
        self.filtered_data = data.copy()

        # Header con título y controles
        with ui.card().classes("w-full shadow-lg rounded-lg data-table-card"):
            with ui.row().classes(
                "w-full items-center justify-between p-4 "
                "bg-gradient-to-r from-blue-600 to-purple-600 "
                "text-white rounded-t-lg"
            ):
                ui.label(title).classes("text-xl font-bold")

                # Campo de búsqueda
                with ui.row().classes("items-center gap-2"):
                    with ui.input(placeholder="Buscar...").props("dense outlined").bind_value(self, "search_term") as search:
                        search.on("update:model-value", self._filter_data)

            # Tabla principal
            table_options = {
                "rows": self.filtered_data,
                "columns": self.columns,
                "selection": selection,
                "pagination": pagination,
                "rows_per_page": rows_per_page,
                "row_key": "id",   # 👈 necesario para manejar selección
                "style": f"height: {height};",
            }
            table_options.update(kwargs)

            self.table = ui.table(**table_options).classes("w-full sticky-header")

            # Eventos
            self.table.on("selection", self._on_row_selection)

            # Footer con estadísticas
            with ui.row().classes("w-full justify-between items-center p-3 bg-gray-100 rounded-b-lg"):
                ui.label().bind_text_from(
                    self, "selected_rows",
                    backward=lambda x: f"{len(x)} fila(s) seleccionada(s)"
                )
                ui.label().bind_text_from(
                    self, "filtered_data",
                    backward=lambda x: f"Total: {len(x)} registro(s)"
                )

        return self.table

    def _filter_data(self):
        """Filtra los datos basado en el término de búsqueda"""
        if not self.search_term:
            self.filtered_data = self.data.copy()
        else:
            search_lower = self.search_term.lower()
            self.filtered_data = [
                row for row in self.data
                if any(search_lower in str(value).lower() for value in row.values())
            ]

        if self.table:
            self.table.rows = self.filtered_data

    def _on_row_selection(self, e):
        """Maneja la selección de filas (guarda solo IDs)"""
        ids = []
        for item in e.args:
            if isinstance(item, dict):
                ids.append(item.get("id"))
            else:
                ids.append(item)
        self.selected_rows = set(x for x in ids if x is not None)

    def get_selected_rows(self):
        """Retorna las filas seleccionadas"""
        return [row for row in self.filtered_data if row["id"] in self.selected_rows]


class ActionableDataTable(AdvancedDataTable):
    def __init__(self):
        super().__init__()
        self.row_actions: List[Dict[str, Any]] = []

    def add_row_action(self, icon: str, handler: Callable, color: str = "primary", tooltip: str = ""):
        """Añade acción personalizada por fila"""
        self.row_actions.append({
            "icon": icon,
            "handler": handler,
            "color": color,
            "tooltip": tooltip,
        })

    def create_table(self, *args, **kwargs):
        """Override para añadir columna de acciones automáticamente"""
        if self.row_actions and "acciones" not in [col["name"] for col in kwargs.get("columns", [])]:
            kwargs["columns"].append({
                "name": "acciones",
                "label": "Acciones",
                "field": "acciones",
                "sortable": False,
                "align": "center",
            })

        return super().create_table(*args, **kwargs)
