class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Usuario):
    def __init__(self, nombre, cursos):
        super().__init__(nombre)
        self.cursos = cursos
        self.estudiantes = {}

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Cursos Inscritos: {self.cursos}\n"

    def inscribir_curso(self, curso):
        if curso in self.cursos:
            raise ValueError(f"El estudiante {self.nombre} ya está inscrito en {curso}.")
        self.cursos.append(curso)
        return f"Estudiante {self.nombre} inscrito en {curso}"

    def CargarEstudiantes(self):
        try:
            with open("usuarios.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        cui, nombre, rol = linea.split(":")
                        if rol == "Estudiante":
                            self.estudiantes[cui] = {
                                "cui": cui,
                                "nombre": nombre,
                                "rol": rol
                            }
            print("Se importaron estudiantes de usuarios.txt")
        except FileNotFoundError:
            print("No existe este archivo")

    def GuardarEstudiantes(self):
        with open("usuarios.txt", "a", encoding="utf-8") as archivo:
            for cui, datos in self.estudiantes.items():
                archivo.write(f"{cui}:{datos['nombre']}:{datos['rol']}\n")

    def AgregarEstudiantes(self, cui, nombre):
        self.estudiantes[cui] = {
            "cui": cui,
            "nombre": nombre,
            "rol": "Estudiante",
        }
        self.GuardarEstudiantes()
        print(f"Estudiante con CUI {cui} agregado y guardado correctamente.")