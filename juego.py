import turtle
import time
import random

retraso= 0.1
marcador = 0
marcador_record = 0

s= turtle.Screen()  #creamos la pantalla
s.setup(650,650) # damos un tamaño a la pantalla
s.bgcolor("orange") #color a la pantalla
s.title("Juego: Snake (Viborita)")

serpiente = turtle.Turtle()
serpiente.shape("circle")
serpiente.penup()
serpiente.direction = "stop"


comida= turtle.Turtle()
comida.shape("square")
comida.shapesize(0.7,0.7,0.7)
comida.color("white")
comida.penup()
comida.goto(0,100)
comida.speed(0)

cuerpo = []

texto = turtle.Turtle()
texto.hideturtle()
texto.penup()
texto.goto(0, -260)
texto.write("Puntos: 0 \t Puntaje record: 0" , align="center", font=("verdana", 24))


def arriba():
    serpiente.direction = "up"

def abajo():
    serpiente.direction = "down"

def derecha():
    serpiente.direction = "right"

def izquierda():
    serpiente.direction = "left"

def movimiento():
    if serpiente.direction == "up":
        y = serpiente.ycor()  #este metodo me retorna la cordenada del eje y
        serpiente.sety(y+20) #este metodo mueve al objeto en el eje y
    if serpiente.direction == "down":
        y = serpiente.ycor()  
        serpiente.sety(y-20)
    if serpiente.direction == "right":
        x = serpiente.xcor()  
        serpiente.setx(x+20) #ahora movemos el objeto en el eje x
    if serpiente.direction == "left":
        x = serpiente.xcor()  
        serpiente.setx(x-20)


s.listen() #la screen queda espectante a la escucha de lo que se le ordene
s.onkeypress(arriba, "Up") #designamos un valor a cada tecla del teclado
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")

while True:
    s.update() #actualizamos la pantalla

    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() >300 or serpiente.ycor() <-300:
        time.sleep(1)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = "stop"
        cuerpo.clear()

        marcador = 0
        texto.clear()
        texto.write(f"Puntos: {marcador} \t Puntaje record: {marcador_record}" , align="center", font=("verdana", 24))


    if serpiente.distance(comida) < 20: #cuando la distancia entre la serpiente y la comida es menor a 20 se mueve
        x = random.randint(-250, 250)  #este metodo elige una cordenada aleatoria para moverse la comida
        y = random.randint(-250, 250)
        comida.goto(x,y)

        nuevo_cuerpo = turtle.Turtle()   #aqui se crea un nuevo pedacito de serpiente
        nuevo_cuerpo.shape("circle")
        nuevo_cuerpo.shapesize(0.7,0.7,0.7)
        nuevo_cuerpo.color("black")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo) #agregamos este nuevo pedacito de serpiente a la lista

        marcador += 10
        if marcador > marcador_record:
            marcador_record = marcador
            texto.clear()
            texto.write(f"Puntos: {marcador} \t Puntaje record: {marcador_record}" , align="center", font=("verdana", 24))

    total = len(cuerpo)
    for i in range(total -1,0,-1):
        x= cuerpo[i-1].xcor()
        y= cuerpo[i-1].ycor()
        cuerpo[i].goto(x,y)

    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x,y)

    movimiento()

    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
            serpiente.direction = "stop"

            marcador = 0
            texto.clear()
            texto.write(f"Puntos: {marcador} \t Puntaje record: {marcador_record}" , align="center", font=("verdana", 24))

        
    time.sleep(retraso)







turtle.done()