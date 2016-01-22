class Persona: 
  def saludo(self):
	return "Hola mundo"


class Estudiante(Persona):
	def __init__(self,nombre,edad):
	 self.nombre = nombre
	 self.edad = edad
	def hola(self):
	 return "Mi nombre es %s" % self.nombre
	 return "Tengo %s" % self.edad
	 return self.saludo

e = Estudiante("Arturo",25)
print e.hola()
