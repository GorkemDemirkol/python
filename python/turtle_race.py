import turtle
import random

colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'yellow', 'brown', 'black', 'cyan', 'magenta', 'violet', 'indigo', 'turquoise', 'maroon']

def get_number_of_racers(screen):
    while True:
        racers = screen.textinput("Yarışmacılar", "Kaç kişi yarışacak? (2-15):")
        if racers and racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 15:
                return racers
            else:
                turtle.textinput("Hata", "Yarışmacı sayısı 2 ile 15 arasında olmalıdır.")
        else:
            turtle.textinput("Hata", "Lütfen rakam giriniz.")

def init_turtle():
    width, height = 800, 500
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.bgcolor('grey')
    screen.title("Kaplumbağa Yarışı")
    return screen

def create_turtles(colors, racers):
    turtles = []
    start_y = -200
    for i in range(racers):
        racer = turtle.Turtle()
        racer.color(colors[i])
        racer.shape('turtle')
        racer.penup()
        racer.goto(-380, start_y)
        start_y += 30
        turtles.append(racer)
    return turtles

def race(turtles):
    while True:
        for racer in turtles:
            distance = random.randint(5, 18)
            racer.forward(distance)
            if racer.xcor() >= 380:
                return turtles.index(racer)

def main():
    screen = init_turtle()
    racers = get_number_of_racers(screen)
    turtles = create_turtles(colors, racers)
    winner = race(turtles)
    print(f"Yarışı kazanan kaplumbağa: {colors[winner]}")
    turtle.done()

if __name__ == "__main__":
    main()
