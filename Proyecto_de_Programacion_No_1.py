estudiantes = {}
instructores = {}
cursos = []

class Curso:
    def __init__(self, curso, instructor):
        self.curso = curso
        self.instructor = instructor

    def agregar_curso(self):
        cursos.append(self.curso)

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Usuario):
    def __init__(self, nombre, cursos):
        super().__init__(nombre)
        self.cursos = cursos


    def inscribir_curso(self, curso):
        if curso in self.cursos:
            raise ValueError(f"El estudiante {self.nombre} ya está inscrito en {curso}.")
        self.cursos.append(curso)
        return f"Estudiante {self.nombre} inscrito en {curso}"


class Instructor(Usuario):
    def __init__(self, nombre, cursos):
        super().__init__(nombre)
        self.cursos = cursos

    def asignar_curso(self, curso):
        if curso in self.cursos:
            raise ValueError(f"El curso {curso} ya está asignado al instructor {self.nombre}.")
        self.cursos.append(curso)
        return f"{self.nombre} ahora imparte {curso}"

if __name__ == "__main__":
    open("usuarios.txt", "w", encoding="utf-8").close()

while True:
    print("1. Agregar Instructor")
    print("2. Crear curso")
    print("3. Agregar estudiante")
    print("4. Asignar estudiante a curso")
    print("5. Crear evalauciones")
    print("6. Registrar calificaciones")
    menu = input("Selecciona una opcion: ")
    match menu:
        case "2":
            curso = input("Ingrese el nombre del curso: ")
            cui_instructor = input("Ingrese el cui del instructor: ").lower()
            if cui_instructor in instructores:
                print(f"El instructor {instructores[cui_instructor]} con cui {cui_instructor} está seleccioando")
                cur = Curso(curso, cui_instructor)
                cur.agregar_curso()
                print(cur.curso)
            else:
                print("Instructor no encontrado")
            print()

        case "3":
            cui = input("Ingrese su cui: ")
            nombre = input("Ingrese el nombre: ").lower()
            cursos = []
            est = Estudiante(nombre, cursos)
            estudiantes[cui] = nombre
            print(estudiantes)
            print()

        case "4":
            cui = input("Ingresa el cui del estudiante: ")
            if cui in estudiantes:
                print(f"El estudiante es {estudiantes[cui]}")
                curso = input("Ingresa el nombre del curso a agregar: ").lower()
                if curso in cursos:
                    Estudiante.inscribir_curso(est, curso)
                    print(f"{estudiantes[cui]} fue agregado a {curso}")
                else:
                    print("Curso no encontrado")
            else:
                print("Estudiante no encontrado!")
            print()

        case "1":
            cui = input("Ingrese su cui: ")
            nombre = input("Ingrese el nombre: ").lower()
            cursos = []
            inst = Instructor(nombre, cursos)
            instructores[cui] = nombre
            print(instructores)
            print()

        case "5":
            curso = input("Escriba el nombre del curso: ")
            if curso in cursos:
                input("Ingrese el nombre del examen o actividad: ")
            else:
                print("Curso no encontrado")
            print()

        case "6":
            cui = input("Ingrese el cui del estudiante: ")
            if cui in estudiantes:
                print(f"El estudiante es {estudiantes[cui]}")
                curscal = input("Ingrese el nombre del curso al que se le asignará calificacion: ")
                print(cursos)
                if curscal in cursos:
                    cal = input(f"Ingresa la calificacion de {estudiantes[cui]} en {curscal}: ")
                else:
                    print("Curso no encontrado")
            else:
                print("Estudiante no encontrado")
            print()