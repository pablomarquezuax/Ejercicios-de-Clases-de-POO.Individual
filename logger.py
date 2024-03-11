class Logger:
    def __init__(self, filename='log.txt'):
        self.filename = filename
        self.log_count = 0
        with open(self.filename, 'w') as file:
            file.write("--Start log--\n")

    def log(self, mensaje):
        with open(self.filename, 'a') as file:
            file.write(f"{mensaje}\n")
        self.log_count += 1

    def __del__(self):
        with open(self.filename, 'a') as file:
            file.write(f"--End log: {self.log_count} log(s) --\n")

# Ejemplo de uso de la clase Logger
logger = Logger()

# Suponiendo que esta clase Logger se utiliza en un método llamada() de una clase Test
class Test:
    def llamada(self):
        global logger
        logger.log("Mensaje de prueba")

# Creando una instancia de Test y llamando al método llamada
test = Test()
test.llamada()
# Al finalizar el programa (o cuando se destruya la instancia de Logger), se escribe el end log
