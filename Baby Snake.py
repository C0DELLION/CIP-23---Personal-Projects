from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    background = canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "white")
    canvas.set_color(background, "#c6c4c4")
    dx = 0
    dy = 0
    
    # Create a black block as player 
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, "black")
    
    # Create the red block as the goal
    goal_x = 360
    goal_y = 360
    goal = canvas.create_rectangle(goal_x, goal_y, goal_x + SIZE, goal_y + SIZE,"red")
    
    direction = 'Right'
    count = 0
    
    while True:
        # Handle Key Press
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            direction = 'Left'
        elif key == 'ArrowRight':
            direction = 'Right'
        elif key == 'ArrowUp':
            direction = 'Up'
        elif key == 'ArrowDown':
            direction = 'Down'
        
        # Update the player's position
        if direction == 'Left':
            dx -= SIZE
        elif direction == 'Right':
            dx += SIZE
        elif direction == 'Up':
            dy-= SIZE
        else:  # direction == 'Down'
            dy += SIZE
        
        # change player possition
        canvas.moveto(player, dx, dy)
        
        # Check for out of bounds
        player_x = canvas.get_left_x(player)
        player_y = canvas.get_top_y(player)
        if player_x < 0 or player_x >= CANVAS_WIDTH or player_y < 0 or player_y >= CANVAS_HEIGHT:
            break
        
        # Detecting collisions
        goal_x = canvas.get_left_x(goal)
        goal_y = canvas.get_top_y(goal)
        goal_right = goal_x + SIZE
        goal_bottom = goal_y + SIZE
        
        if player_x < goal_right and player_x + SIZE > goal_x and player_y < goal_bottom and player_y + SIZE > goal_y:
            move_goal(canvas, goal)
            count += 1
        
        # print points
        text_obj = canvas.create_text(4, 387,text=f"Your points : {count}")
        
        # Sleep    
        time.sleep(DELAY)
        
        # Delete old points text
        canvas.delete(text_obj)
        
    # show result
    result = f"Your Score is : {str(count)}"
    canvas.create_text((CANVAS_WIDTH/2)-100, (CANVAS_HEIGHT/2)-14, '🆂🅽🅰🅺🅴 🅸🆂 🅾🆄🆃 🅾🅵 🅱🅾🅽🅳')
    canvas.create_text((CANVAS_WIDTH/2)-50, CANVAS_HEIGHT/2, '🅶🅰🅼🅴 🅾🆅🅴🆁')
    canvas.create_text((CANVAS_WIDTH/2)-45, (CANVAS_HEIGHT/2)+14, result, color='blue')
    
# Move the goal to a new location
def move_goal(canvas, goal):
    goal_x = random.randint(0, CANVAS_WIDTH // SIZE - 1) * SIZE
    goal_y = random.randint(0, CANVAS_HEIGHT // SIZE - 1) * SIZE
    canvas.moveto(goal, goal_x, goal_y)

if __name__ == '__main__':
    main()
