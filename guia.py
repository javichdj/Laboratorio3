def leer_guia (entrada):
	guia=[]

	for linea in open(entrada):
		if 'nombre' in linea.lower ():
			continue

		linea=linea.strip()
		nombre, telf= linea.split()
		telf= int (telf)

		guia={'nombre':nombre,'telf':telf}
		guia.append (guia)
	return guia

def borrar_nombre(guia):
	linea=[]
	linea.append(guia['nombre'])
	linea.append(str(guia['telf']))

	linea += '\n'
	return linea
def escribir_fichero(fichero, guia):
	fhand= open('guia.txt','w')
	fhand.write('Nombre Telf\n')

	for guia in guia:
		linea=borrar_nombre(guia)
		fhand.write(linea)
