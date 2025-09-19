estudiantes = {}
instructores = {}
cursos = []
curso_instructor = {}
evaluaciones = {}
calificaciones = {}

class Curso:
    def __init__(self, nombre, instructor_cui):
        self.nombre = nombre
        self.instructor_cui = instructor_cui

class Usuario:
    def __init__(self, nombre, *args, **kwargs):
        self.nombre = nombre
        self.extra = kwargs

    def descripcion(self):
        return f"Usuario {self.nombre}."

class Estudiante(Usuario):
    def __init__(self, nombre, *args, **kwargs):
        super().__init__(nombre, *args, **kwargs)
        self.cui = None

    def descripcion(self):
        return f"Estudiante {self.nombre} (extras: {self.extra})"

    def inscribir_curso(self, curso_nombre):
        if self.cui not in calificaciones:
            calificaciones[self.cui] = {}
        if curso_nombre not in calificaciones[self.cui]:
            calificaciones[self.cui][curso_nombre] = {}
            return f"Estudiante {self.nombre} inscrito en {curso_nombre}"
        else:
            raise ValueError(f"El estudiante {self.nombre} ya está inscrito en {curso_nombre}.")

class Instructor(Usuario):
    def __init__(self, nombre, *args, **kwargs):
        super().__init__(nombre, *args, **kwargs)
        self.cursos = []

    def descripcion(self):
        return f"Instructor {self.nombre} (extras: {self.extra})"

    def asignar_curso(self, curso_nombre):
        if curso_nombre in self.cursos:
            raise ValueError(f"El curso {curso_nombre} ya está asignado al instructor {self.nombre}.")
        self.cursos.append(curso_nombre)
        return f"{self.nombre} ahora imparte {curso_nombre}"


def crear_instructor(cui, nombre, **kwargs):
    if cui in instructores:
        raise ValueError("CUI de instructor ya existe.")
    inst = Instructor(nombre.lower(), **kwargs)
    inst.cui = cui
    instructores[cui] = inst
    return inst

def crear_estudiante(cui, nombre, **kwargs):
    if cui in estudiantes:
        raise ValueError("CUI de estudiante ya existe.")
    est = Estudiante(nombre.lower(), **kwargs)
    est.cui = cui
    estudiantes[cui] = est
    return est

def crear_curso(nombre, instructor_cui):
    nombre = nombre.lower()
    if nombre in cursos:
        raise ValueError("Curso ya existe.")
    if instructor_cui not in instructores:
        raise ValueError("Instructor no encontrado.")
    cursos.append(nombre)
    curso_instructor[nombre] = instructor_cui
    instr = instructores[instructor_cui]
    instr.asignar_curso(nombre)
    evaluaciones[nombre] = []
    return nombre

def crear_evaluacion(curso_nombre, *args):
    curso_nombre = curso_nombre.lower()
    if curso_nombre not in cursos:
        raise ValueError("Curso no encontrado.")
    nuevas = []
    for nombre_evaluacion in args:
        ev = nombre_evaluacion.strip().lower()
        if ev in evaluaciones[curso_nombre]:
            raise ValueError(f"La Evaluación '{ev}' ya existe en este curso.")
        evaluaciones[curso_nombre].append(ev)
        # agregar la evaluación a las calificaciones existentes
        for cui, cursos_dict in calificaciones.items():
            if curso_nombre in cursos_dict:
                cursos_dict[curso_nombre][ev] = None
        nuevas.append(ev)
    return nuevas

def registrar_calificacion(cui_est, curso_nombre, **kwargs):
    curso_nombre = curso_nombre.lower()
    if cui_est not in estudiantes:
        raise ValueError("Estudiante no encontrado.")
    if curso_nombre not in cursos:
        raise ValueError("Curso no encontrado.")
    calificaciones.setdefault(cui_est, {})
    calificaciones[cui_est].setdefault(curso_nombre, {})

    for nombre_evaluacion, puntuacion in kwargs.items():
        ev = nombre_evaluacion.strip().lower()
        if ev not in evaluaciones[curso_nombre]:
            raise ValueError(f"Evaluación '{ev}' no encontrada en ese curso.")
        try:
            score = float(puntuacion)
        except ValueError:
            raise ValueError("La puntuación debe ser un número.")
        if score < 0 or score > 100:
            raise ValueError("La puntuación debe estar entre 0 y 100.")
        calificaciones[cui_est][curso_nombre][ev] = score

    guardar_punteos_en_archivo()
    return f"Registradas calificaciones para {estudiantes[cui_est].nombre} en {curso_nombre}: {kwargs}"

def promedio_estudiante_en_curso(cui_est, curso_nombre):
    curso_nombre = curso_nombre.lower()
    if cui_est not in calificaciones or curso_nombre not in calificaciones[cui_est]:
        return None
    evals = calificaciones[cui_est][curso_nombre]
    valores = [v for v in evals.values() if v is not None]
    if not valores:
        return None
    return sum(valores) / len(valores)

def promedio_general_estudiante(cui_est):
    if cui_est not in calificaciones:
        return None
    promedios = []
    for curso_nombre in calificaciones[cui_est]:
        p = promedio_estudiante_en_curso(cui_est, curso_nombre)
        if p is not None:
            promedios.append(p)
    if not promedios:
        return None
    return sum(promedios) / len(promedios)

def guardar_punteos_en_archivo(ruta="calificaciones.txt"):
    with open(ruta, "w", encoding="utf-8") as f:
        for cui, cursos_dict in calificaciones.items():
            nombre = estudiantes.get(cui).nombre if cui in estudiantes else "Desconocido"
            f.write(f"Estudiante: {nombre} (CUI: {cui})\n")
            for curso_nombre, evals in cursos_dict.items():
                f.write(f"  Curso: {curso_nombre}\n")
                for ev_name, score in evals.items():
                    f.write(f"    {ev_name}: {score}\n")
                avg = promedio_estudiante_en_curso(cui, curso_nombre)
                f.write(f"    Promedio en curso: {avg}\n")
            pg = promedio_general_estudiante(cui)
            f.write(f"  Promedio general: {pg}\n")
            f.write("-" * 40 + "\n")
    return ruta

def listar_cursos():
    if not cursos:
        return []
    return list(cursos)

def estudiantes_en_curso(curso_nombre):
    curso_nombre = curso_nombre.lower()
    if curso_nombre not in cursos:
        raise ValueError("Curso no encontrado.")
    inscritos = []
    for cui, cursos_dict in calificaciones.items():
        if curso_nombre in cursos_dict:
            inscritos.append(estudiantes[cui].nombre)
    return inscritos

if __name__ == "__main__":
    open("usuarios.txt", "w", encoding="utf-8").close()
    while True:
        print("- - MENU - -")
        print("1. Agregar Instructor")
        print("2. Crear curso")
        print("3. Agregar estudiante")
        print("4. Inscribir estudiante a curso")
        print("5. Crear evaluacion en un curso")
        print("6. Registrar calificacion")
        print("7. Mostrar promedios de un estudiante")
        print("8. Guardar punteos en archivo")
        print("9. Listar cursos")
        print("10. Listar estudiantes de un curso")
        print("11. Salir")
        menu = input("Selecciona una opcion: ").strip()

        try:
            match menu:
                case "1":
                    cui = input("Ingrese el cui del instructor: ").strip().lower()
                    nombre = input("Ingrese el nombre del instructor: ").strip()
                    crear_instructor(cui, nombre)
                    print(f"Instructor {nombre} creado con CUI {cui}\n")

                case "2":
                    nombre = input("Ingrese el nombre del curso: ").strip()
                    cui_instructor = input("Ingrese el cui del instructor: ").strip().lower()
                    crear_curso(nombre, cui_instructor)
                    print(f"Curso '{nombre}' creado y asignado al instructor {cui_instructor}\n")

                case "3":
                    cui = input("Ingrese su cui: ").strip().lower()
                    nombre = input("Ingrese el nombre del estudiante: ").strip()
                    crear_estudiante(cui, nombre)
                    print(f"Estudiante {nombre} creado con CUI {cui}\n")

                case "4":
                    cui = input("Ingresa el cui del estudiante: ").strip().lower()
                    curso = input("Ingresa el nombre del curso a agregar: ").strip().lower()
                    if cui in estudiantes and curso in cursos:
                        estudiantes[cui].inscribir_curso(curso)
                        print(f"{estudiantes[cui].nombre} fue agregado a {curso}\n")
                    else:
                        print("--Estudiante o curso no encontrado\n")

                case "5":
                    curso = input("Escriba el nombre del curso: ").strip().lower()
                    if curso in cursos:
                        nombre_ev = input("Ingrese el nombre del examen o actividad: ").strip()
                        crear_evaluacion(curso, nombre_ev)
                        print(f"Evaluación '{nombre_ev}' creada para {curso}\n")
                    else:
                        print("--Curso no encontrado\n")

                case "6":
                    cui = input("Ingrese el cui del estudiante: ").strip().lower()
                    curso = input("Ingrese el nombre del curso: ").strip().lower()
                    evaluacion = input("Ingrese el nombre de la evaluación: ").strip().lower()
                    puntuacion = input("Ingrese la puntuación (número): ").strip()
                    registrar_calificacion(cui, curso, **{evaluacion: puntuacion})
                    print("Calificación registrada.\n")

                case "7":
                    cui = input("Ingrese el cui del estudiante: ").strip().lower()
                    if cui in estudiantes:
                        print("Promedios por curso:")
                        if cui in calificaciones:
                            for curso_nombre in calificaciones[cui]:
                                p = promedio_estudiante_en_curso(cui, curso_nombre)
                                print(f"  {curso_nombre}: {p}")
                        else:
                            print("  Sin calificaciones.")
                        pg = promedio_general_estudiante(cui)
                        print(f"Promedio general: {pg}\n")
                    else:
                        print("--Estudiante no encontrado\n")

                case "8":
                    ruta = guardar_punteos_en_archivo()
                    print(f"Punteos guardados en {ruta}\n")

                case "9":
                    cursos_disponibles = listar_cursos()
                    if cursos_disponibles:
                        print("Cursos registrados:")
                        for c in cursos_disponibles:
                            print(f" - {c}")
                    else:
                        print("No hay cursos registrados.\n")

                case "10":
                    curso = input("Ingrese el nombre del curso: ").strip().lower()
                    try:
                        alumnos = estudiantes_en_curso(curso)
                        if alumnos:
                            print(f"Estudiantes en {curso}:")
                            for est in alumnos:
                                print(f" - {est}")
                        else:
                            print(f"No hay estudiantes inscritos en {curso}.")
                    except Exception as e:
                        print("Error:", e)

                case "11":
                    print("Saliendo...")
                    break

                case _:
                    print("--Opcion no válida\n")
        except Exception as e:
            print("Error:", e, "\n")