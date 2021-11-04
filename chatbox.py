#-*- coding: utf-8 -*-

#Para poder generar esperas de tiempo e interactuar con el OS
import time, os

#Para obtener numeros random
from random import randint, randrange

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
  time.sleep(4)
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
  time.sleep(2)
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
  time.sleep(2)
  os.system('cls')
  
  #Manda Propaganda
  print("BODEGON NUÑEZ ~ * ARRIBEÑOS 3198 - CABA ")
  time.sleep(2)
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
  time.sleep(2)
  os.system('cls')
  
  #Manda Propaganda
  print("20% DE DESCUENTO EN BEBIDAS  ~ * CARREFOUR!!!")
  time.sleep(2)
  os.system('cls')

  return ("Te gusta la Magia?: ", "preguntando magia", coca)


#6ta Pregunta
def procesarPreguntandoMagia (usuario_dijo, tema):
  magia="no"
  usuario_dijo = usuario_dijo.lower()
  if usuario_dijo == "si":
    magia="si"
    print("Pensa un numero entre 1 y 9.....")
    time.sleep(4)
    print("Sumale 5")
    time.sleep(4)
    print("Multiplica el resultado por 2")
    time.sleep(4)
    print("Restale 4.....")
    time.sleep(4)
    print("Dividilo por 2.....")
    time.sleep(4)
    print("Restale el numero que pensaste.....")
    time.sleep(5)
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
    time.sleep(4)
    
  elif usuario_dijo == "no":
    print("Menos, mal me salve de hacer un papelon")
      
  #Limpia la pantalla
  time.sleep(2)
  os.system('cls')
  
  return ("Jugamos un partidito en la Play? : ", "preguntando play", magia)


#7ta Pregunta
def procesarPreguntandoPlay (usuario_dijo, tema):
  play="no"
  usuario_dijo = usuario_dijo.lower()
  if usuario_dijo == "si":
    print("Okey, le digo a ALEXA que encienda la Play")
    play="si"
  elif usuario_dijo == "no":
    print("Uhhh que aburrid@....Me voy a dormir, nos vemos mañana....zzzzzz")
    exit()
      
  #Limpia la pantalla
  time.sleep(2)
  os.system('cls')
  
  #Iniciando la Play
  print("SONY PLAYSTATION - INICIANDO..... ")
  time.sleep(4)
  
  exit()



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
  print("""
             ,\ 
             \\\,_
              \` ,\ 
         __,.-" =__)
       ."        )
    ,_/   ,    \/\_
    \_|    )_-\ \_-`
       `-----` `--`
""")

