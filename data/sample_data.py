from typing import List, Dict, Any
from datetime import datetime, timedelta
import random

def generate_sample_users(num_users: int = 50) -> List[Dict[str, Any]]:
    """Genera datos de ejemplo de usuarios"""
    cities = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Zaragoza', 'Málaga', 'Murcia', 'Palma']
    status_options = ['Activo', 'Inactivo', 'Pendiente', 'Bloqueado']

    users = []
    for i in range(1, num_users + 1):
        registration_date = (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')

        users.append({
            'id': i,
            'nombre': f'Usuario {i}',
            'email': f'user{i}@example.com',
            'edad': random.randint(18, 65),
            'ciudad': random.choice(cities),
            'telefono': f'+34 6{random.randint(1000000, 9999999)}',
            'fecha_registro': registration_date,
            'estado': random.choice(status_options),
            'saldo': round(random.uniform(100, 5000), 2),
            'acciones': ''  # Se llenará con botones
        })

    return users

    def get_sample_columns() -> List[Dict[str, str]]:
        """Retorna las columnas para la tabla de usuarios"""
        return [
            {'name': 'id', 'label': 'ID', 'field': 'id', 'sortable': True, 'align': 'left', 'width': '80px'},
            {'name': 'nombre', 'label': 'Nombre', 'field': 'nombre', 'sortable': True, 'align': 'left'},
            {'name': 'email', 'label': 'Email', 'field': 'email', 'sortable': True, 'align': 'left'},
            {'name': 'edad', 'label': 'Edad', 'field': 'edad', 'sortable': True, 'align': 'center', 'width': '80px'},
            {'name': 'ciudad', 'label': 'Ciudad', 'field': 'ciudad', 'sortable': True, 'align': 'left'},
            {'name': 'telefono', 'label': 'Teléfono', 'field': 'telefono', 'sortable': False, 'align': 'left'},
            {'name': 'fecha_registro', 'label': 'Registro', 'field': 'fecha_registro', 'sortable': True, 'align': 'center'},
            {'name': 'estado', 'label': 'Estado', 'field': 'estado', 'sortable': True, 'align': 'center'},
            {'name': 'saldo', 'label': 'Saldo (€)', 'field': 'saldo', 'sortable': True, 'align': 'right', 'format': lambda val: f'{val:,.2f} €'},
            {'name': 'acciones', 'label': 'Acciones', 'field': 'acciones', 'sortable': False, 'align': 'center', 'width': '120px'}
        ]