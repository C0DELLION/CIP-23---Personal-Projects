from graphics import Canvas

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
CIRCLE_SIZE = 20
DELAY = 0.001

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(0, 0, 600, 75, 'black')
    text = canvas.create_text(40, 20, font='Arial', font_size = 45, text='️🎨 DRAWING BOARD🖌️', color='white')
    
    canvas.create_rectangle(0, 75, 100, 150, 'red')
    text = canvas.create_text(30, 105, font='Arial', font_size = 15, text ='RED', color='black')
    
    canvas.create_rectangle(0, 150, 100, 225, 'yellow')
    text = canvas.create_text(20, 180, font='Arial', font_size = 15, text ='YELLOW', color='black')
    
    canvas.create_rectangle(0, 225, 100, 300, 'green')
    text = canvas.create_text(20, 255, font='Arial', font_size = 15, text ='GREEN', color='black')
    
    canvas.create_rectangle(0, 300, 100, 375, 'blue')
    text = canvas.create_text(30, 330, font='Arial', font_size = 15, text ='BLUE', color='black')
    
    canvas.create_rectangle(0, 375, 100, 450, 'black')
    text = canvas.create_text(25, 410, font='Arial', font_size = 15, text ='BLACK', color='white')
    
    canvas.create_rectangle(0, 450, 100, 525, 'purple')
    text = canvas.create_text(20, 480, font='Arial', font_size = 15, text ='PURPLE', color='black')
    
    canvas.create_rectangle(0, 525, 100, 600, 'white')
    text = canvas.create_text(20, 555, font='Arial', font_size = 15, text ='ERASER', color='black')
    
    
    b = -1
    color = 'white'
    while True:
        a = canvas.get_last_click()
        left_x = canvas.get_mouse_x()
        top_y = canvas.get_mouse_y()
        
        if a != None:
            if 150 < left_x < CANVAS_WIDTH and 0 < top_y < CANVAS_HEIGHT:
                b = -b
            if 0 < left_x < 150:
                if 75 < top_y < 150:
                    color = 'red'
                elif 150 < top_y < 225:
                    color = 'yellow'
                elif 225 < top_y < 300:
                    color = 'green'
                elif 300 < top_y < 375:
                    color = 'blue'
                elif 375 < top_y < 450:
                    color = 'black'
                elif 450 < top_y < 525:
                    color = 'purple'
                elif 525 < top_y < 600:
                    color = 'white'
   
        if b == 1:
            if 150 < left_x < CANVAS_WIDTH - CIRCLE_SIZE and 0 < top_y < CANVAS_HEIGHT - CIRCLE_SIZE:
                canvas.create_oval(left_x, top_y, left_x + CIRCLE_SIZE, top_y + CIRCLE_SIZE, color)
        
        time.sleep(DELAY)

if __name__ == "__main__":
    main()
