class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = {}

    def CargarUsuarios(self):
        try:
            with open("usuarios.txt", "r", encoding="utf-8") as archivo:
                for liena in archivo:
                    linea = linea.strip()
                    if linea:
                        cui, nombre, rol = linea.split(":")
                        self.usuarios[cui] = {
                            'cui': cui,
                            'nombre': nombre,
                            'rol': rol
                        }
            print("Se importaron usuarios de usuarios.txt")
        except FileNotFoundError:
            print("No existe este archivo")  #cambiar por tkinter

    def GuardarUsuarios(self):
        with open("usuarios.txt", "w", encoding="utf=8") as archivo:
            for cui, datos in self.usuarios.items():
                archivo.write(f"{cui}:{datos['nombre']}:{datos['rol']}")