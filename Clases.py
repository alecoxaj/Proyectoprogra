class Curso:
    def __init__(self, curso):
        self.curso = curso
        self.cursos = []
        self.estudiantes = []
        self.instructores = []

    def agregar_curso(self):
        self.cursos.append(self.curso)

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def agregar_instructor(self, instructor):
        if self.instructores:
            print("Ya hay un instrucotr asignado a este curso!")
        else:
            self.instructores.append(instructor)

class Usuario:
    def __init__(self, cui, nombre):
        self.nombre = nombre
        self.cui = cui
        super().__init__()

class Estudiante(Usuario):
    def __init__(self, cui, nombre, curso):
        super().__init__(cui, nombre)
        self.curso = curso
        self.estudiantes = []

class Instructor(Usuario):
    def __init__(self, cui, nombre, curso):
        super().__init__(cui, nombre)
        self.curso = curso
        self.instructores = []

x = Curso

while True:
    print("1. Crear curso")
    print("2. Agregar estudiante")
    print("3. Agregar Instructor")
    menu = input("Selecciona una opcion: ")

    match menu:
        case "1":
            nombreCurso = input("Ingresa el nombre del curso: ").lower()
            cur = Curso(nombreCurso)
            cur.agregar_curso()

        case "2":
            cui = input("Ingresa el cui: ")
            nombre = input("Ingresa el nombre: ")
            curso = input("Ingresa el nombre del curso al que se asignará: ").lower()

            if curso == cur.curso:
                est = Estudiante(cui, nombre, curso)
                cur.agregar_estudiante(est)
            else:
                print("Curso no encontrado")

        case "3":
            cui = input("Ingresa el cui: ")
            nombre = input("Ingresa el nombre: ")
            curso = input("Ingresa el nombre del curso al que se asignará: ").lower()

            if curso == cur.curso:
                inst = Instructor(cui, nombre, curso)
                cur.agregar_estudiante(inst)
            else:
                print("Curso no encontrado")


