class A:
    def z(self):
        return self

    def y(self, t):
        return len(t)

# Crear una instancia de A
aa = A()

# Comparar si dos instancias de A son el mismo objeto (esto siempre será False)
print(aa is A())  # False

# Llamar al método y con una tupla vacía, esperando longitud 0
print(aa.y(()))  # 0

# Llamar al método y con una tupla que contiene un elemento, esperando longitud 1
print(aa.y((aa,)))  # 1

# Llamar al método y con una tupla que contiene dos elementos, esperando longitud 2
print(aa.y((aa, aa.z)))  # 2

# Llamar al método y con una tupla que contiene tres elementos, esperando longitud 3
print(aa.y((aa.z, 1, 'z')))  # 3
