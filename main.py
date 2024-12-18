import pyxel
import time

class App:   
    def __init__(self):
        # Initialize the Pyxel window (width, height)
        pyxel.init(160, 120)
        pyxel.load("my_resource.pyxres")
        # Set the initial position of the square
        self.x = 75
        self.y = 55
        self.time = 0
        # Set the initial position and velocity of the sprite
        self.sprite_x = 80
        self.sprite_y = 80
        self.sprite_dx = 2
        self.sprite_dy = 2
        self.game_started = False
        # Start the game loop
        pyxel.run(self.update, self.draw)
    def update(self):
        # Update the square's position based on arrow keys
        if pyxel.btn(pyxel.KEY_W):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_S):
            self.y += 2
        if pyxel.btn(pyxel.KEY_A):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_D):
            self.x += 2
        # Simple interaction: Has aatimer to track score
        if self.x < 160 and self.y < 120:
            #while = true:
            #time.sleep(1)
            #x = round(self.time, 1)
            self.time += 0.03275
        # Update the sprite's position
        self.sprite_x += self.sprite_dx
        self.sprite_y += self.sprite_dy
        # Bounce the sprite off the edges of the screen
        if self.sprite_x <= 5 or self.sprite_x >= 150:
            self.sprite_dx *= -1
            #self.sprite_dx += -3
        if self.sprite_y <= 5 or self.sprite_y >= 110:
            self.sprite_dy *= -1

        self.distance = ((self.x + 8 - self.sprite_x) ** 2 + (self.y + 8 - self.sprite_y) ** 2) ** 0.5
        if self.distance <= 13:  # 13 is the sum of the radii (8 for blt + 5 for circ)
            # Handle collision (e.g., change sprite color)        
            pyxel.circ(self.sprite_x, self.sprite_y, 5, 10)
    
    def draw(self):
        # Clear the screen with black (color 0)
        if self.distance <= 13:
            time.sleep(1000)
            #pyxel.quit()
        else:
            pyxel.cls(0)
        # Draw a square (color 9)
        # pyxel.rect(0, 0, 10, 10, 9)
        # Draw the moving sprite (color 11)
        pyxel.circ(self.sprite_x, self.sprite_y, 5, 11)
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)  # Draws a 16x16 sprite from bank 0
       
        # Display the score
        pyxel.text(5, 5, f"Time: {self.time}", 7)
        # Display a message when score is high
        if self.time >= 0.1:
            pyxel.text(10, 20, "If the game froze, you lost.", 6)
        if self.time >= 0.2:
            pyxel.text(10, 30, "(Time is score.)", 6)
        if self.time >= 15:
            pyxel.text(50, 50, "Ball speed increased", 8)
        if self.time >= 30:
            #pyxel.cls(0)
            pyxel.text(50, 50, "Ball speed increased", 0)
            pyxel.text(50, 50, "Ball speed increased 2x", 8)
        if self.time >= 45:
            pyxel.text(50, 50, "Ball speed increased 2x", 0)
            pyxel.text(50, 50, "Ball movement changed", 8)
        if self.time >= 60:
            pyxel.text(50, 50, "Ball movement changed", 0)
            pyxel.text(35, 50, "Good luck, ball max speed", 8)
        if self.time >= 15 and  self.time <= 15.05:
            self.sprite_dy *= -1.25
            self.sprite_dx *= -1.25
        if self.time >= 30 and  self.time <= 30.05:
            self.sprite_dy *= -1.5
            self.sprite_dx *= -1.5
        if self.time >= 45 and  self.time <= 45.05:
            self.sprite_dy *= -2
            self.sprite_dy *= -1.5
        if self.time >= 60 and  self.time <= 60.05:
            self.sprite_dy *= -1
            self.sprite_dy *= -1.5
        if self.x <= 0 or self.x >= 145:
            self.x = 55
        if self.y <= 0 or self.y >= 105:
            self.y = 55

# Run the game
App()
