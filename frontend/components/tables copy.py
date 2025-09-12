# Creado en DeepSeek
# frontend/components/tables.py


from nicegui import ui
from typing import List, Dict, Any, Optional, Callable
import pandas as pd
from datetime import datetime

class AdvancedDataTable:
    def __init__(self):
        self.table = None
        self.columns = []
        self.data = []
        self.filtered_data = []
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
        Crea una tabla avanzada con múltiples funcionalidades
        """
        self.columns = columns
        self.data = data
        self.filtered_data = data.copy()

        # Header con título y controles
        with ui.card().classes("w-full shadow-lg rounded-lg data-table-card"):
            # Header de la tabla
            with ui.row().classes("w-full items-center justify-between p-4 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-t-lg"):
                ui.label(title).classes("text-xl font-bold")

                # Controles de búsqueda y acciones
                with ui.row().classes("items-center gap-2"):
                    with ui.input(placeholder="Buscar...").props('dense outlined').bind_value(self, 'search_term') as search:
                        search.on('update:model-value', self._filter_data)
                    ui.button(icon='refresh', on_click=self._refresh_data).props('flat round color=white')
                    ui.button(icon='download', on_click=self._export_data).props('flat round color=white')

            # Tabla principal
            table_options = {
                'rows': self.filtered_data,
                'columns': self.columns,
                'selection': selection,
                'pagination': pagination,
                'rows-per-page': rows_per_page,
                'style': f'height: {height};',
                'class': 'full-width sticky-header'
            }
            table_options.update(kwargs)

            self.table = ui.table(**table_options).classes("w-full")

            # Eventos
            self.table.on('selection', self._on_row_selection)

            # Footer con estadísticas
            with ui.row().classes("w-full justify-between items-center p-3 bg-gray-100 rounded-b-lg"):
                ui.label().bind_text_from(self, 'selected_rows',
                                        backward=lambda x: f'{len(x)} fila(s) seleccionada(s)')
                ui.label().bind_text_from(self, 'filtered_data',
                                        backward=lambda x: f'Total: {len(x)} registro(s)')

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
        """Maneja la selección de filas"""
        self.selected_rows = set(e.args)

    def _refresh_data(self):
        """Actualiza los datos"""
        self.filtered_data = self.data.copy()
        self.search_term = ""
        if self.table:
            self.table.rows = self.filtered_data

    def _export_data(self):
        """Exporta datos a CSV"""
        df = pd.DataFrame(self.filtered_data)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"export_{timestamp}.csv"
        df.to_csv(filename, index=False)
        ui.notify(f"Datos exportados a {filename}")

    def get_selected_rows(self):
        """Retorna las filas seleccionadas"""
        return [row for row in self.filtered_data if row['id'] in self.selected_rows]


class ActionableDataTable(AdvancedDataTable):
    def __init__(self):
        super().__init__()
        self.row_actions = []

    def add_row_action(self, icon: str, handler: Callable, color: str = "primary", tooltip: str = ""):
        """Añade acción personalizada por fila"""
        self.row_actions.append({
            'icon': icon,
            'handler': handler,
            'color': color,
            'tooltip': tooltip
        })

    def create_table(self, *args, **kwargs):
        """Override para añadir columna de acciones automáticamente"""
        if self.row_actions and 'acciones' not in [col['name'] for col in kwargs.get('columns', [])]:
            # Añadir columna de acciones si no existe
            kwargs['columns'].append({
                'name': 'acciones',
                'label': 'Acciones',
                'field': 'acciones',
                'sortable': False,
                'align': 'center'
            })

        return super().create_table(*args, **kwargs)