# Socket - Network communication

Read and write over network sockets!

Sockets are the technical term to describe the process of programs talking over a network connection.

Network communications are based on the "client-server" model. 

* The role of the "server" program is to listen for programs wanting to communicate with it, listen to what they have to say and to then send a reply. 
* The role of the "client" program is to initiate communication with a server, send a message and listen for the reply.

This means you will need two programs running to get this to work. Even better if you can run them on different computers and actually get them to communicate over a network! (but it will work just fine running both programs on the same computer)

* If you do use separate computers, you will need to know the network IP address of the "server" computer.  You will then have to send the correct IP address in the second parameter of the send_message_get_reply function of the client so it knows where to initiate the conversation.

I've deliberately made the client program work so the one function call is all that is required to talk to a server. This should make it a lot easier to incorporate into a project.

Some possible uses:

* Create a chat server
* Live multiplayer games!
* What ever your imagination can conjure!

## Exericse 1 - Simple chat server

Note: This will only function properly where two computers can see each other on the same network (eg: peer-to-peer). For instance, this won't work between two people at different addresses each running off their own ISP internet connection unless you know how to set up Network Address Translation port forwarding.

```python
### File: basicnetworking.py

import socket
import select
import threading

class BasicServer(threading.Thread):

    def __init__(self, callback, port):
        threading.Thread.__init__(self)
        self.port = port
        self.callback = callback
        self.event = threading.Event()

    def stop(self):
        self.event.set()

    def get_message(self, socket):
        # Will only terminate when it receives an end of line character \n
        received = ""
        finished = False
        while not finished:
            # Receive the message up to 2048 bytes at a time
            partial = socket.recv(2048).decode()
            if "\n" in partial:
                end_at = partial.index("\n")
                finished = True
                received = received + partial[:end_at]
            elif partial == '':
                raise RuntimeError("socket connection broken")
            else:
                received = received + partial
        return received

    def run(self):
        # Create a socket object
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Attach ourselves to the port
        host = socket.gethostname()
        serversocket.bind(("0.0.0.0", self.port))

        # Queue up to 5 requests
        serversocket.listen(5)

        # Servers keep running until they die
        timeout_in_seconds = 1
        # serversocket.settimeout(1)
        while not self.event.is_set():
            ready = select.select([serversocket], [], [], timeout_in_seconds)
            if ready[0]:
                # Wait until a connection
                clientsocket, addr = serversocket.accept()
                # Receive a message
                msg_received = self.get_message(clientsocket)
                self.callback(addr[0], msg_received)
                # All done, close connection
                clientsocket.close()

def send(message, addr, port):
    message = message + "\n"  # Make sure to send the "end of message" signal!
    # Connect, send, close
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((addr, port))
    s.sendall(message.encode())
    s.close()
    print("Message to {}: {}".format(addr, message[:-1]))


def get_my_ipaddress():
    return socket.gethostbyname(socket.gethostname())

```

Using the above class file, it is now as simple as this to run a network application from your main:

```python
### File: main.py
import basicnetworking

def receive_message(addr, msg):
    # This function will be automatically run every time a message is received. This is where I code how I want my program to respond to a message.
    print("Message from {}: {}".format(addr,msg))

if __name__ == "__main__":
    print("Your IP address is: " + basicnetworking.get_my_ipaddress())
    my_port = int(input("What port number would you like to receive messages on? (between 1024 and 65535) "))
    client_addr = input("What's the other computer's IP address?")
    client_port = int(input("What's the other computer's port?"))

    # Start my server
    server = basicnetworking.BasicServer(receive_message, my_port)
    server.start()

    # Run the program
    print("Write your messages. [ENTER] to send, or an empty line to quit.")
    msg = input()
    while msg != "":
        # To send a message over the network is now just this one line of code.
        basicnetworking.send(msg, client_addr, client_port)
        msg = input()

    server.stop()
    print("Goodbye...")

```

<div class="page" />

## Exercise 2 - Multi player snake game

```python 
import socket
import json

snakes = {}

def get_message(socket):
    # Will only terminate when it receives an end of line character \n
    received = ""
    finished = False
    while not finished:
        # Receive the message up to 2048 bytes at a time
        partial = socket.recv(2048).decode()
        if "\n" in partial:
            end_at = partial.index("\n")
            finished = True
            received = received + partial[:end_at]
        elif partial == '':
            raise RuntimeError("socket connection broken")
        else:
            received = received + partial
    return received

def process_data(data):

# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attach ourselves to the port
host = socket.gethostname()
port = 9999
serversocket.bind(("0.0.0.0", port))

# Queue up to 5 requests
serversocket.listen(5)
print("Waiting for connection on {0}:{1}".format(host,port))

# Servers keep running until they die
while True:
    # Wait until a connection
    clientsocket, addr = serversocket.accept()
    # Woohoo! Someone loves us and wants to chat
    print("Got a connection from {0}".format(str(addr)) )
    # Receive a message
    received = get_message(clientsocket)
    print("Message from {0}: {1}".format(addr, received))

    msg = process_data(received)

    clientsocket.sendall(msg.encode())
    # All done, close connection
    clientsocket.close()
```

## Demo exercise 2: Multi player snake: Snake.py

```python
import pygame, sys, random, socket, json
from pygame.locals import *

def get_message(socket):
    # Will only terminate when it receives an end of line character \n
    received = ""
    finished = False
    while not finished:
        # Receive the message up to 2048 bytes at a time
        partial = socket.recv(2048).decode()
        if "\n" in partial:
            end_at = partial.index("\n")
            finished = True
            received = received + partial[:end_at]
        elif partial == '':
            raise RuntimeError("socket connection broken")
        else:
            received = received + partial
    return received

def send_message_get_reply(message, address="127.0.0.1", port=9999):
    # Make a connection
    print("Connecting to {0}:{1}".format(address,port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address, port))
    # Send a message
    s.sendall(message.encode())
    # Receive a reply
    reply = get_message(s)
    # All done, ciao!
    s.close()
    return reply
```

Modify your snake game program as follows.

```python
import basicnetworking

print("Welcome to multiplayer snake!")
our_player_name = input("Player name: ")
server_address = input("IP address of server: ")

pygame.init()
fps = pygame.time.Clock()

# Create window
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")

# Create colours
colorFruit = (255,0,0)
colorBlack = (0,0,0)
ourColor = (255,255,255)
playerColors = [
    (255,255,0), (0,0,255), (0,255,0),
    (128,128,128), (128,128,128), (128,128,128),
    (128,128,128), (128,128,128), (128,128,128)
] # really the only limit to the number of players is the number of colours we set here

gameRunning = True
snakeXY = [(10,10)]
fruitXY = (5,5)
fullWindow = (0,0,500,500)
currentX = 10
currentY = 10
dirX = 0
dirY = 0

while gameRunning:
    # Events
    for event in pygame.event.get():
        if event.type == QUIT:
            gameRunning = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                dirX = -1
                dirY = 0
            elif event.key == K_RIGHT:
                dirX = +1
                dirY = 0
            elif event.key == K_UP:
                dirX = 0
                dirY = -1
            elif event.key == K_DOWN:
                dirX = 0
                dirY = +1
    # Update our snake
    currentX += dirX
    currentY += dirY
    snakeXY.insert(0,(currentX, currentY))
    nothing = snakeXY.pop()

    window.fill(colorBlack)

    # Send our snake to the server, and find out where all the others are to draw
    data = {}
    data["player_name"] = our_player_name
    data["snake_data"] = snakeXY
    msg = json.dumps(data)
    reply_str = send_message_get_reply(msg+"\n", server_address)
    reply_data = json.loads(reply_str)

    # Clear window, Draw fruit
    window.fill(colorBlack)
    fruit = Rect(fruitXY[0]*20, fruitXY[1]*20, 20, 20)
    pygame.draw.rect(window, colorFruit, fruit)

    # Draw all snakes using data form server
    fruitCollide = False
    player_is_us = False
    player_number = 0
    for player, snake_data in reply_data.items():
        # pick a color. check to see if this is us.
        colorToUse = playerColors[player_number]
        if player == our_player_name:
            colorToUse = ourColor
            player_is_us = True
        else:
            player_number += 1
        # Draw this snake
        for snakePiece in snake_data:
            snakeRect = Rect(snakePiece[0] * 20, snakePiece[1] * 20, 20, 20)
            pygame.draw.rect(window, colorToUse, snakeRect)
            # Detect collision with fruit
            if player_is_us and snakeRect.colliderect(fruit):
                fruitCollide = True

    # If we ate the fruit, increase our length, relocate the fruit
    if fruitCollide:
        snakeXY.append((currentX, currentY))
        # Reposition the fruit
        fruitXY = (random.randint(1, 25), random.randint(1, 25))

    # Draw on screen
    pygame.display.update()
    fps.tick(10)

pygame.quit()
print("Good bye!")
```
