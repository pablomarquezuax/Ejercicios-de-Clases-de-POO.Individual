class Palindromo:
    def __init__(self, cadena):
        self.cadena = cadena

    def esPalindromo(self):
        # Verificar si la cadena tiene espacios
        if " " in self.cadena:
            return False
        # Eliminar los caracteres no alfanuméricos y convertir a minúsculas
        cadena_limpia = "".join(car for car in self.cadena if car.isalnum()).lower()
        # Comparar la cadena limpia con su inversa
        return cadena_limpia == cadena_limpia[::-1]

    def test(self):
        # Verifica si el atributo de la instancia es un palíndromo.
        if self.esPalindromo():
            print(f"La cadena '{self.cadena}' ES un palíndromo.")
            # No se llama a __del__ explícitamente, se deja que Python maneje la destrucción
        else:
            print(f"La cadena '{self.cadena}' NO es un palíndromo. La instancia será destruida.")
            # Se invoca el método para manejar la lógica de destrucción, aunque simbólicamente
            self.destruir()

    def destruir(self):
        # Simulación de destrucción. En práctica, solo muestra un mensaje.
        print(f"Destruyendo la instancia... La cadena fue: {self.cadena.upper()}")

    def __del__(self):
        # Método que se llama automáticamente al destruir la instancia.
        pass

# Ejemplo de uso
palindromo1 = Palindromo("Anita lava la tina")
palindromo1.test()

# Crear otra instancia para probar sin espacios
palindromo2 = Palindromo("anitalavalatina")
palindromo2.test()  

palindromo3 = Palindromo("radar")
palindromo3.test()

palindromo4 = Palindromo("holaquetal")
palindromo4.test()

# Pregunta adicional: ¿por qué se muestra RADAR después de la instanciación Palindromo("sonar")?
# En ambas pruebas de plaindromo se utiliza como nombre de la variable "p"
# por lo que se guarda la palabra radar inicialmente como valor de la variable.
# Por eso al ser radar la palabra en el primer test, se imprime radar como instancia destruida
# al utilizar sonar como test y este no ser un plaindromo.En el siguiente test como se
# guarda sonar como valor de "p" si se imprime dicha palabra como instancia destruida.