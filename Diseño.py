class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        super().__init__()

class Estudiante(Usuario):
    def __init__(self, nombre, cursos):
        super().__init__(nombre)
        self.cursos = cursos
        self.estudiantes = {}

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Cursos Inscritos: {self.cursos}\n"

    def inscribir_curso(self, curso):
        if curso in self.cursos:
            raise ValueError(f"El estudiante {self.nombre} ya esta inscrito en {curso}.")
        self.cursos.append(curso)
        return f"Estudiante: {self.nombre} inscrito en {curso}-"

    def CargarEstudiantes(self):
        try:
            with open("usuarios.txt", "r", encoding="utf-8") as archivo:
                for liena in archivo:
                    linea = linea.strip()
                    if linea:
                        cui, nombre, rol = linea.split(":")
                        self.estudiantes[cui] = {
                            'cui': cui,
                            'nombre': nombre,
                            'rol': rol
                        }
            print("Se importaron usuarios de usuarios.txt")
        except FileNotFoundError:
            print("No existe este archivo")#cambiar por tkinter

    def GuardarEstudiantes(self):
        with open("usuarios.txt", "w", encoding="utf=8") as archivo:
            for cui, datos in self.estudiantes.items():
                archivo.write(f"{cui}:{datos['nombre']}:{datos['rol']}")

    def AgregarEstudiantes(self, cui, nombre, rol):
        self.estudiantes[cui] = {
            'cui': cui,
            'nombre': nombre,
            'rol': rol,
        }
        self.GuardarEstudiantes()
        print(f"Cliente con CUI {cui} agregado y guardado correctamente.")

class Instructor(Usuario):
    def __init__(self, nombre, cursos):
        super().__init__(nombre)
        self.cursos = cursos
        self.instructores = {}

    def mostrar_info(self):
        return f"Instructor: {self.nombre}, Cursos asignados: {self.cursos}\n"


    def CargarInstructores(self):
        try:
            with open("usuarios.txt", "r", encoding="utf-8") as archivo:
                for liena in archivo:
                    linea = linea.strip()
                    if linea:
                        cui, nombre, rol = linea.split(":")
                        self.instructores[cui] = {
                            'cui': cui,
                            'nombre': nombre,
                            'rol': rol
                        }
            print("Se importaron usuarios de usuarios.txt")
        except FileNotFoundError:
            print("No existe este archivo")#cambiar por tkinter

    def GuardarInstructores(self):
        with open("usuarios.txt", "w", encoding="utf=8") as archivo:
            for cui, datos in self.instructores.items():
                archivo.write(f"{cui}:{datos['nombre']}:{datos['rol']}")

    def AgregarInstructores(self, cui, nombre, rol):
        self.instructores[cui] = {
            'cui': cui,
            'nombre': nombre,
            'rol': rol,
        }
        self.GuardarInstructores()
        print(f"Cliente con CUI {cui} agregado y guardado correctamente.")