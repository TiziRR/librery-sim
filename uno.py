import random

# Ejercicio improvisado

# Crear un sistema para una biblioteca. Utilizando POO y lo que sepa o pueda.

# * Clases/Tablas

# Biblioteca -> Tiene: Nombre, Dueños, *Libros, *Clientes, Ubicación, *Empleados, Horario de atención
class Biblioteca:
    def __init__(self, nombre, dueños, ubicacion, horario):
        self.nombre_biblioteca = nombre
        self.dueños = dueños
        self.ubicacion = ubicacion
        self.horario = horario
        self.libros = []
        self.clientes = []
        self.empleados = []

    def __str__(self):
        return f'\n{'=' * 20} {self.nombre_biblioteca} {'=' * 20}\n{'-' * 10}> Dueño/a/os/as: {self.dueños}\n{'-' * 10}> Ubicacion: {self.ubicacion}\n{'-' * 10}> Horarios: {self.horario}'

    def mostrar_libros(self):
        try:
            if not self.libros:
                raise ValueError('No hay libros disponibles')
            else:
                print('\nLibros disponibles')
                for lib in self.libros:
                    print(f'{'-' * 10}> {lib}')
        except ValueError as error:
            print(f'\nError: {error}')

    def agregar_libro(self, libro):
        try:
            self.libros.append(libro)
            if libro in self.libros:
                print(f'\nLibro agregado correctamente ✔')
            else:
                raise ValueError(f'No se pudo cargar el libro ❌')
        except ValueError as error:
            print(f'\nError: {error}')

    def agregar_cliente(self, cliente):
        try:
            self.clientes.append(cliente)
            if self.clientes:
                print(f'{'-' * 10}> Cliente cargado correctamente ✔')
            else:
                raise NameError('No se pudo cargar el cliente ❌')
        except NameError as error:
            print(f'Error: {error}')

    def agregar_empleado(self, empleado):
        try:
            self.empleados.append(empleado)
            if self.empleados:
                print(f'{'-' * 10}> Empleado cargado correctamente ✔')
            else:
                raise NameError('No se pudo cargar el empleado ❌')
        except NameError as error:
            print(f'Error: {error}')

# Libro -> Tiene: ID, Nombre, *Autor, Precio, Fecha de Emisión, Cantidad de páginas, Categoria
class Libro:
    autores = ['Jorge Luis Borges', 'Gabriel García Marquez', 'Maria Elena Walsh', 'J.K Rowing', 'Tim Burton']
    
    def __init__(self, nombre: str, autor: str, precio: float, fecha_emi: str, cant_pag: int, categoria: list):
        try:
            self.nombre = nombre
            if autor in self.autores:
                self.autor = autor 
            else:
                raise NameError('Autor no disponible')
            self.precio = precio
            self.fecha_emision = fecha_emi
            self.cant_paginas = cant_pag
            self.categoria = categoria
        except NameError as error:
            print(f'Error: {error}')

    def __str__(self) -> str:
        return f'\n{'-' * 8}> Nombre del Libro: {self.nombre}\n{'-' * 8}> Autor: {self.autor}\n{'-' * 8}> Fecha de Emision: {self.fecha_emision}\n{'-' * 8}> Cantidad de Paginas: {self.cant_paginas}\n{'-' * 8}> Categoria/as: {self.categoria}'

# Cliente -> Tiene: DNI, Nombre, Apellido, Edad, Preferencias de categoria, Alquileres Disponibles
class Cliente:
    def __init__(self, dni: int, nombre: str, apellido: str, edad: int, prefe_cat: list):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.preferencias = prefe_cat
        self.alquileres_disponibles = 3

    def __str__(self) -> str:
        return f'\n{'=' * 10} {self.nombre} {'=' * 10}\n{'-' * 10}> Nombre completo: {self.nombre} {self.apellido}\n{'-' * 10}> DNI: {self.dni}\n{'-' * 10}> Edad: {self.edad}\n{'-' * 10}> Preferencias: {self.preferencias}\n{'-' * 10}> Alquileres disponibles: {self.alquileres_disponibles}'

biblio_prueba = Biblioteca('Tras los pasos', 'Pepe Argento', 'Posadas', '15hs - 20hs')

print(biblio_prueba)
print(biblio_prueba.agregar_libro('Facha.com'))
print(biblio_prueba.agregar_libro('El bijas - Master class'))
print(biblio_prueba.agregar_libro('Chanti - El risas'))
print(biblio_prueba.mostrar_libros())
