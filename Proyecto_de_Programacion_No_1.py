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

class Instructor(Usuario):
    def __init__(self, nombre, cursos):
        super().__init__(nombre)
        self.cursos = cursos
        self.instructores = {}

    def mostrar_info(self):
        return f"Instructor: {self.nombre}, Cursos asignados: {self.cursos}\n"

    def asignar_curso(self, curso):
        if curso in self.cursos:
            raise ValueError(f"El curso {curso} ya está asignado al instructor {self.nombre}.")
        self.cursos.append(curso)
        return f"{self.nombre} ahora imparte {curso}"

    def CargarInstructores(self):
        try:
            with open("usuarios.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        cui, nombre, rol = linea.split(":")
                        if rol == "Instructor":
                            self.instructores[cui] = {
                                "cui": cui,
                                "nombre": nombre,
                                "rol": rol
                            }
            print("Se importaron instructores de usuarios.txt")
        except FileNotFoundError:
            print("No existe este archivo")

    def GuardarInstructores(self):
        with open("usuarios.txt", "a", encoding="utf-8") as archivo:
            for cui, datos in self.instructores.items():
                archivo.write(f"{cui}:{datos['nombre']}:{datos['rol']}\n")

    def AgregarInstructores(self, cui, nombre):
        self.instructores[cui] = {
            "cui": cui,
            "nombre": nombre,
            "rol": "Instructor",
        }
        self.GuardarInstructores()
        print(f"Instructor con CUI {cui} agregado y guardado correctamente.")

def crear_curso(nombre_curso, *estudiantes, **kwargs):
    curso = {"nombre": nombre_curso, "estudiantes": [], "instructor": kwargs.get("instructor")}
    for est in estudiantes:
        curso["estudiantes"].append(est.nombre)
    return curso

def registrar_usuario():
    print("=== Registro de Usuario ===")
    cui = input("Ingrese CUI: ")
    nombre = input("Ingrese nombre: ")
    rol = input("Ingrese rol (Estudiante/Instructor): ")

    if rol.lower() == "estudiante":
        est = Estudiante(nombre, [])
        est.AgregarEstudiantes(cui, nombre)
    elif rol.lower() == "instructor":
        ins = Instructor(nombre, [])
        ins.AgregarInstructores(cui, nombre)
    else:
        print("Rol no válido. Intente de nuevo.")

if __name__ == "__main__":
    open("usuarios.txt", "w", encoding="utf-8").close()

    # Menú de registro
    while True:
        opcion = input("\n¿Desea registrar un nuevo usuario? (s/n): ")
        if opcion.lower() == "s":
            registrar_usuario()
        else:
            break

    print("\n--- Contenido del archivo usuarios.txt ---")
    with open("usuarios.txt", "r", encoding="utf-8") as f:
        print(f.read())

    e_temp = Estudiante("temp", [])
    e_temp.CargarEstudiantes()
    print("Diccionario estudiantes:", e_temp.estudiantes)

    i_temp = Instructor("temp", [])
    i_temp.CargarInstructores()
    print("Diccionario instructores:", i_temp.instructores)

