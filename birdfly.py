import pgzrun
import random

# Set window dimensions
WIDTH = 350
HEIGHT = 600

# Load background and bird images
background = Actor('background')
background.x = WIDTH // 2  # Center the background horizontally
background.y = HEIGHT // 2  # Center the background vertically

bird = Actor('bird')
bird.x = 50
bird.y = HEIGHT / 2

# Load and set obstacle images (upper and lower parts)
bar_up = Actor('bar_up')
bar_down = Actor('bar_down')
bar_up.x = 300
bar_down.x = 300

# Score and game state variables
score = 0
game_over = False

# Initial speed and obstacle position
obstacle_speed = random.randint(2, 5)
background_speed = 0.5  # Set the speed of the background scroll
bar_up.y = random.randint(-200, 0)
bar_down.y = bar_up.y + 600  # Maintain a gap between obstacles


# Draw function to render all objects on the screen
def draw():
    screen.clear()
    # Draw two backgrounds side by side for a scrolling effect
    background.draw()
    screen.blit("background", (background.x - WIDTH, background.y - HEIGHT // 2))

    # Draw obstacles and bird
    bar_up.draw()
    bar_down.draw()
    bird.draw()

    # Draw score and game over text
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")
    if game_over:
        screen.draw.text("Game Over!", center=(WIDTH / 2, HEIGHT / 2), fontsize=60, color="red")


# Update function to handle game logic
def update():
    global score, game_over, obstacle_speed

    if not game_over:
        # Bird falling effect
        bird.y += 3

        # Move the background for scrolling effect
        background.x -= background_speed
        if background.x <= 0:
            background.x = WIDTH  # Reset position to create a seamless scroll

        # Move the obstacles left
        bar_up.x -= obstacle_speed
        bar_down.x -= obstacle_speed

        # Reset obstacles when they go off-screen and increase score
        if bar_up.x < 0:
            bar_up.x = WIDTH
            bar_down.x = WIDTH
            bar_up.y = random.randint(-200, 0)
            bar_down.y = bar_up.y + 500
            obstacle_speed = random.randint(2, 5)
            score += 1  # Increment score when bird passes obstacle

        # Check for collisions
        if bird.colliderect(bar_up) or bird.colliderect(bar_down):
            game_over = True  # End the game on collision

        # Check if bird hits the ground or flies too high
        if bird.y > HEIGHT or bird.y < 0:
            game_over = True  # End the game if bird is out of bounds


# Function to make bird fly up on mouse click
def on_mouse_down():
    if not game_over:
        bird.y -= 100


# Function to make bird fly up when up arrow key is pressed
def on_key_down(key):
    if key == keys.UP and not game_over:
        bird.y -= 100  # Adjust the value to control the upward movement


# Start the game loop
pgzrun.go()
