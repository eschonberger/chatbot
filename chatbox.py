#-*- coding: utf-8 -*-

#Para poder generar esperas de tiempo e interactuar con el OS
import time, os

#Para pintar la pantalla
import colorama
from colorama import Fore
from colorama import Back
from colorama import Style


#Para obtener numeros random
from random import randint, randrange
from colorama.ansi import clear_screen

# librería útil para requerir mediante http
import requests

def esNum( dado_objeto ):
	try:
		float( dado_objeto )
		return True
	except:
		return False

def preguntarNum( dado_mensaje,mensajeSiError = "Ingreso erroneo" ):
  respuesta = input( dado_mensaje + ">" )
  
  while not esNum(respuesta):
    print(mensajeSiError)
    respuesta = input(dado_mensaje + ">")
    
  return respuesta

def preguntarSi( dado_mensaje ):
  respuesta = input( dado_mensaje + ">" )
  respuesta = "\n" + respuesta.lower().strip() + "\n" ;
  posiblesSi = [ 
  "\nsi\n"
  ," si\n"
  ," si "
  ,"si,"
  ,"1\n"    
  ]
  retornar = False
  for cada_opcion in posiblesSi:
    if respuesta.count(cada_opcion) > 0:
      retornar = True   

  return retornar

#1er Pregunta
def procesarEstadoAnimo(usuario_dijo, tema):
  usuario_dijo = usuario_dijo.lower()
  if usuario_dijo == "bien":
    estado_animo = (usuario_dijo, 1)
  elif usuario_dijo == "muy bien":
    estado_animo = (usuario_dijo, 2)
  elif usuario_dijo == "excelente":
    estado_animo = (usuario_dijo, 3)
  elif usuario_dijo == "mal":
    estado_animo = (usuario_dijo, -1)
  elif usuario_dijo == "terrible":
    estado_animo = (usuario_dijo, -4)
  
  #Cuenta un chiste para que el usuario se relaje  
  if estado_animo[1] < 0:
    contarChiste()

  return ("Cual es tu nombre?: ","preguntando nombre", estado_animo[0]) #estado_animo[0] dado que es una tupla para que envie solo el texto {bien, mal, etc}

#2da Pregunta
def procesarPreguntandoNombre (usuario_dijo, tema):
  usuario_dijo = usuario_dijo.lower()
  if usuario_dijo == "carlos":
    print("Sabias que tu nombre es de procedencia germana y significa 'hombre libre'.")
  elif usuario_dijo == "jose":
    print("Sabias que tu nombre es de origen hebreo y significa el 'hombre que multiplica'.")
  elif usuario_dijo == "marcelo":
    print("Marcelo es un nombre de origen latino. Proviene de Marte, el dios romano de la guerra.")
  elif usuario_dijo == "gladys":
    print("Sabias que tu nombre es de origen gales, significa 'gobernador de un gran territorio'.")
  elif usuario_dijo == "susana":
    print("Sabias que tu nombre es de origen Egipcio, significa 'Bella como la flor'.")
  elif usuario_dijo == "patricia":
    print("Sabias que tu nombre es de origen latino, significa 'mujer noble'.")
  else:
    print("No hemos encontrado significado.....quizas no eres de este mundo ;-)")
    
  #Limpia la pantalla
  time.sleep(6)
  os.system('cls')
  
  return ("Te gusta el Futbol?: ", "preguntando futbol", usuario_dijo)
  
#3er Pregunta
def procesarPreguntandoFutbol (usuario_dijo, tema):
  futbol="no"
  usuario_dijo = usuario_dijo.lower()
  if usuario_dijo == "si":
    print("Que mal que boca perdio la punta :-(")
    futbol="si"
  elif usuario_dijo == "no":
    print("A mi tampoco, mucha plata derrochada....")
      
  #Limpia la pantalla
  time.sleep(3)
  os.system('cls')
  
  #Manda Propaganda
  print("TRASNOCHE PARANORMAL ~ * RADIO POP - fm 101.5 ")
  time.sleep(3)
  os.system('cls')
  return ("Te gusta la Milanesa?: ", "preguntando milanesa", futbol)

#4er Pregunta
def procesarPreguntandoMilanesa (usuario_dijo, tema):
  milanesa="no"
  usuario_dijo = usuario_dijo.lower()
  if usuario_dijo == "si":
    print("Seee compañer@, a mi tambien me encanta la fritanga")
    milanesa="si"
  elif usuario_dijo == "no":
    print("Es mejor cuidar la salud y comer mas verduras...")
      
  #Limpia la pantalla
  time.sleep(3)
  os.system('cls')
  
  #Manda Propaganda
  print("BODEGON NUÑEZ ~ * ARRIBEÑOS 3198 - CABA ")
  time.sleep(3)
  os.system('cls')

  return ("Te gusta la Coca Cola?: ", "preguntando cocaCola", milanesa)


#5ta Pregunta
def procesarPreguntandoCocaCola (usuario_dijo, tema):
  coca="no"
  usuario_dijo = usuario_dijo.lower()
  if usuario_dijo == "si":
    print("A mi tambien me encanta. Probaste los nuevos Sabores?")
    coca="si"
  elif usuario_dijo == "no":
    print("Es mejor no tomar mas el veneno negro")
      
  #Limpia la pantalla
  time.sleep(3)
  os.system('cls')
  
  #Manda Propaganda
  print("20% DE DESCUENTO EN BEBIDAS  ~ * CARREFOUR!!!")
  time.sleep(3)
  os.system('cls')

  return ("Te gusta la Magia?: ", "preguntando magia", coca)


#6ta Pregunta
def procesarPreguntandoMagia (usuario_dijo, tema):
  magia="no"
  usuario_dijo = usuario_dijo.lower()
  if usuario_dijo == "si":
    magia="si"
    print("Pensa un numero entre 1 y 9.....")
    time.sleep(7)
    print("Sumale 5")
    time.sleep(7)
    print("Multiplica el resultado por 2")
    time.sleep(7)
    print("Restale 4.....")
    time.sleep(7)
    print("Dividilo por 2.....")
    time.sleep(7)
    print("Restale el numero que pensaste.....")
    time.sleep(7)
    print("""
                      .

                   .
         /^\     .
    /\   "V"
   /__\   I      O  o
  //..\\  I     .
  \].`[/  I
  /l\/j\  (]    .  O
 /. ~~ ,\/I          .
 \\L__j^\/I       o
  \/--v}  I     o   .
  |    |  I   _________
  |    |  I c(`       ')o
  |    l  I   \.     ,/
_/j  L l\_!  _//^---^\\_    
    """)
    print("El resultado es : --->3<---" )
    time.sleep(6)
    
  elif usuario_dijo == "no":
    print("Menos, mal me salve de hacer un papelon")
      
  #Limpia la pantalla
  time.sleep(2)
  os.system('cls')
  
  return ("Te gustaria ver productos Magicos? : ", "preguntando tienda", magia)

###ESPECIALIZACION TIENDA MAGICA

#7ta Pregunta
def procesarPreguntandoTienda (usuario_dijo, tema):
  if usuario_dijo=="no":
    apiClima()
    exit()
  else:
    menu()
    

#MENU

def menu():
  Articulos = ["🃏 Cartas","฿ Monedas","🎓 Cursos"]

  print(f"{Fore.BLUE}----->B@zar MAGICO<-----")
  for items in Articulos:
    print(items)

  seleccion = input("Indica el articulo sobre el cual queres ver mas detalles: ")
  seleccion = seleccion.lower()

#Seleccion x la Cartas
  if (seleccion=="carta" or seleccion=="cartas"):
    mostrarCartas()
    seleccioncarta = input(f"{Fore.YELLOW}Desea ver mas informacion o el Precio: ")
    seleccioncarta = seleccioncarta.lower()
    
    if (seleccioncarta=="detalle" or seleccioncarta=="detalles" or seleccioncarta=="info" or seleccioncarta=="informacion"):
      infoCartas()
      
    elif (seleccioncarta=="precio" or seleccioncarta=="costo"):
      precioCartas()
    
    elif (seleccioncarta=="salir" or seleccioncarta=="exit"):
      apiClima()
      exit()
      

#Seleccion x las Monedas  
  elif (seleccion=="moneda") or (seleccion=="monedas"):
    mostrarMonedas()
    seleccionmoneda = input("Desea ver mas informacion o el Precio: ")
    seleccionmoneda = seleccionmoneda.lower()
    
    if (seleccionmoneda=="detalle" or seleccionmoneda=="detalles" or seleccionmoneda=="info" or seleccionmoneda=="informacion"):
      infoMonedas()
      
    elif (seleccionmoneda=="precio" or seleccionmoneda=="costo"):
      precioMonedas()
    
    elif (seleccionmoneda=="salir" or seleccionmoneda=="exit"):
      apiClima()
      exit()

#Seleccion de los Cursos    
  elif (seleccion=="curso" or seleccion=="cursos"):
    mostrarCursos()
    seleccioncurso = input("Desea ver mas informacion o el Precio: ")
    seleccioncurso = seleccioncurso.lower()
    
    if (seleccioncurso=="detalle" or seleccioncurso=="detalles" or seleccioncurso=="info" or seleccioncurso=="informacion"):
      infoCursos()
      
    elif (seleccioncurso=="precio" or seleccioncurso=="costo"):
      precioCursos()
    
    elif (seleccioncurso=="salir" or seleccioncurso=="exit"):
      apiClima()
      exit()
  
  elif (seleccion=="salir" or seleccion=="exit"):
    apiClima()
    exit()



#Funciones de las Cartas 
def mostrarCartas():
  os.system('cls')
  print(f"{Fore.RED}🂡 Baraja Bicycle - Poker\n")
  print("🃏 Baraja Moonshine Midnight por Enigma Ltd\n")
  print("🃠 Baraja Tally Ho\n")

def infoCartas():
  os.system('cls')
  print("✓ Baraja Bicycle - Poker")
  print("\tEl mejor mazo de naipes para magia. Cartas de poker de la mejor calidad. Disponible en Azul y Rojo. \n")
      
  print("✓ Baraja Moonshine Midnight por Enigma Ltd")
  print("\tApartándose del aspecto genérico de las cartas actuales, el objetivo es que vuelvas a una época de pandillas y muñecas, a los antros y bares llenos de humo de la América de los años 20.\n")

  print("✓ Baraja Tally Ho")
  print("\tEste es un diseño clásico Tally-Ho en verde con la impresión a todo color.\n")
      
  seleccioncarta = input("Desea ver el Precio: ")
  seleccioncarta = seleccioncarta.lower()
  if (seleccioncarta=="si" or seleccioncarta=="dale"):
    precioCartas()
  
  #Retorna al Menu
  menu()

def precioCartas():
  os.system('cls')
  print("✓ Baraja Bicycle - Poker")
  print("\tPrecio: $935")
  print("\tLink: https://trucosymagia.com/barajas-de-poker/90-28-baraja-de-poker-bicycle.html#/2-color-azul\n")
      
  print("✓ Baraja Moonshine Midnight por Enigma Ltd")
  print("\tPrecio: $150")
  print("\tLink: https://trucosymagia.com/barajas-de-poker/499-baraja-moonshine-midnight-por-enigma-ltd.html\n")

  print("✓ Baraja Tally Ho")
  print("\tPrecio: $320")
  print("\tLink: https://trucosymagia.com/barajas-de-poker/490-baraja-tally-ho-verde.html\n")
  time.sleep(3)
#Retorna al Menu
  menu()

#Funciones de las Monedas
def mostrarMonedas():
  os.system('cls')
  print("฿ Cascarilla Expandida Nacional")
  print("฿ Moneda Mordida Medio Dolar")
  print("฿ Flipper Medio Dolar")



def infoMonedas():
  os.system('cls')
  print("✓ Cascarilla Expandida Nacional")
  print("\tMiles de rutinas se podrán realizar con este accesorio. Efectos de moneda a través de la mano o de billete y muchas rutinas más.\n")

  print("✓ Moneda Mordida Medio Dolar")
  print("\tEl mago enseña una moneda, la muerde y le arranca un pedazo. Abre su boca y muestra el pedazo entre sus dientes, lo lanza sobre la moneda y el pedazo vuelve mágicamente a su lugar. Quedando la moneda como nueva.\n")
  
  print("✓ Flipper Medio Dolar")
  print("\tEl mago enseña dos monedas de iguales, las coloca en la palma de su mano, cierra la misma e increíblemente al abrirla una de ellas ha desaparecido.\n")
  
  seleccionmoneda = input("Desea ver el Precio: ")
  seleccionmoneda = seleccionmoneda.lower()
  if (seleccionmoneda=="si" or seleccionmoneda=="dale"):
    precioMonedas()
  
  #Retorna al Menu
  menu()




def precioMonedas():
  os.system('cls')
  print(f"{Fore.GREEN}✓ Cascarilla Expandida Nacional")
  print("\tPrecio: $2200")
  print("\tLink: https://trucosymagia.com/monedas-trucadas/152-cascarilla-expandida-50-cents-nacional.html\n")
      
  print("✓ Moneda Mordida Medio Dolar")
  print("\tPrecio: $2200")
  print("\tLink: https://trucosymagia.com/monedas-trucadas/311-moneda-mordida-medio-dolar-sistema-interno.html\n")

  print("✓ Flipper Medio Dolar")
  print("\tPrecio: $1980")
  print("\tLink: https://trucosymagia.com/monedas-trucadas/144-scotch-and-soda-nacional.html\n")
  time.sleep(3)
  
#Retorna al Menu
  menu()


#####Funciones de los cursos

def mostrarCursos():
  os.system('cls')
  print(f"{Fore.RED}🂡 Magia Inicial\n")
  print("🃏 Magia Intermedia\n")
  print("🃠 Magia Avanzada\n")

def infoCursos():
  os.system('cls')
  print("✓ Baraja Bicycle - Poker")
  print("\tPosición de agarre de una baraja, como cortar, mezclar, buscar, distribuir y manejar cartas. Florituras básicas. Teorías de la Magia\n")
      
  print("✓ Magia Intermedia")
  print("\tTécnicas Cartomágicas I. Técnicas Numismagia I. El humor en la magia. Teoría de tipos de Efecto. Ilusiones con todo tipo de elementos, naipes, sogas, monedas, papeles, velocidad mental, control mental, explosiones. \n")

  print("✓ Magia Avanzada")
  print("\tTécnica Cartomágica II y Técnica Numismagica II. Conceptos de 'One Ahead' y elección del mago. Psicología aplicada a los espectadores. Gags Mágicos.\n")
      
  seleccioncurso = input("Desea ver el Precio: ")
  seleccioncurso = seleccioncurso.lower()
  if (seleccioncurso=="si" or seleccioncurso=="dale"):
    precioCursos()
  
  #Retorna al Menu
  menu()

def precioCursos():
  os.system('cls')
  print("✓ Magia Inicial")
  print("\tPrecio: $9035")
  print("\tLink: https://trucosymagia.com/cursos/nivel-inicial.html\n")
      
  print("✓ Magia Intermedia")
  print("\tPrecio: $15000")
  print("\tLink: https://trucosymagia.com/cursos/nivel-intermedio.html\n")

  print("✓ Magia Avanzada")
  print("\tPrecio: $32000")
  print("\tLink: https://trucosymagia.com/cursos/nivel-avanzado.html\n")
  time.sleep(3)
#Retorna al Menu
  menu()



def apiClima():
  
  def asesoraClima(temp):
    if temp <10:
        return "lleva abrigo, hace frio"
    elif temp <20:
        return "lleva pullover, esta freco"
    else:
        return "sali tranqui en remera"

  strApi = "https://api.open-meteo.com/v1/forecast?latitude=-34.6118&longitude=-58.4173&current_weather=true"

  # Conectamos a http  mediante método GET, el mismo de formularios
  recuperado = requests.get(strApi)

  # Devuelve un diccionario. A cada dato accedemos mediante .get() de obtener
  recuperadoEnJson = recuperado.json()

  temperatura = recuperadoEnJson.get("current_weather" ).get("temperature")

  resultado = asesoraClima(int(temperatura))

  print( "Ahora mismo hace {}º, {}.".format( temperatura, resultado) )


def contarChiste():
  print("¿Qué sale de la cruza entre un mono y un pato?")
  time.sleep(3)
  print("----->¡Un monopatín!<-----")
  time.sleep(3)
  #Limpia la pantalla
  os.system('cls')


def saludarxHorario():
  hora = time.localtime().tm_hour
  if (hora >= 20):
    print("Buenas Noches")
  elif (hora <20 and hora >=13):
    print("Buenas Tardes")
  else:
    print("Buenos Dias")
  print(f"""{Fore.GREEN}
             ,\ 
             \\\,_
              \` ,\ 
         __,.-" =__)
       ."        )
    ,_/   ,    \/\_
    \_|    )_-\ \_-`
       `-----` `--`
""")

