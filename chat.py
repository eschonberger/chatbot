from chatbox import *

estado_animo = "Sin informar"
nombre = "Sin informar"
tema = "Estado de Animo"
futbol = "no"
milanesa = "no"
coca = "no"
magia ="no"
play="no"

#Saluda al usuario basandose en la Hora
saludarxHorario()

usuario_dijo = input( "Hola, ¿Cómo andás?: " ) # Puede contestar Bien / muy bien / excelente / mal / terrible
while not usuario_dijo == "salir":
  if tema == "Estado de Animo":
    (siguiente_pregunta, tema, estado_animo) = procesarEstadoAnimo(usuario_dijo, tema) # Cuenta chiste si el estado de animo es mal o terrible
  elif tema == "preguntando nombre":
      (siguiente_pregunta, tema, nombre) = procesarPreguntandoNombre( usuario_dijo, tema )  # Detalla el origen del nombre
  elif tema == "preguntando futbol":
      (siguiente_pregunta, tema, futbol) = procesarPreguntandoFutbol( usuario_dijo, tema ) # Publicidad
  elif tema == "preguntando milanesa":
      (siguiente_pregunta, tema, milanesa) = procesarPreguntandoMilanesa( usuario_dijo, tema ) #Publicidad
  elif tema == "preguntando cocaCola":
      (siguiente_pregunta, tema, coca) = procesarPreguntandoCocaCola( usuario_dijo, tema )      #Publicidad
  elif tema == "preguntando magia":
      (siguiente_pregunta, tema, magia) = procesarPreguntandoMagia( usuario_dijo, tema )    #Hace un truco matematico
  elif tema == "preguntando play":
      (siguiente_pregunta, tema, play) = procesarPreguntandoPlay( usuario_dijo, tema ) # Inicia la play 
    
            

  usuario_dijo = input( siguiente_pregunta )

  