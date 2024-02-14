import pyray as pr
import os
import src.csv_util as cu

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000
SCREEN_TITLE = 'D-Vis'

pr.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
pr.set_target_fps(100)

BACKGROUND_COLOR = [0, 0, 0, 255]
AXIS_COLOR = [255, 255, 255, 255]

camera = pr.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)

csv = cu.CSV('mnist_SCALED.csv')
#csv = cu.CSV('iris.csv')
#csv = cu.CSV('heart.csv')

while not pr.window_should_close():
    # pan camera on mouse down
    if pr.is_mouse_button_down(0):
        pr.update_camera(camera, pr.CAMERA_THIRD_PERSON)
        
    pr.begin_drawing()
    pr.clear_background(BACKGROUND_COLOR)
    pr.draw_fps(10, 10)
    
    #pr.draw_text('hello world', 950, 100, 20, [255, 255, 255, 255])
    
    LABEL_X = 1100
    LABEL_Y = 70
    LABEL_FONT_SIZE = 20
    i = 0
    for label in sorted(csv.label_color):
        pr.draw_text(label, LABEL_X, LABEL_Y + i * 23, LABEL_FONT_SIZE, [*csv.label_color[label], 255])
        i += 1
    
    pr.begin_mode_3d(camera)
    
    # draw 3d axis
    pr.draw_line_3d([0, 0, -10], [0, 0, 10], AXIS_COLOR)
    pr.draw_line_3d([0, -10, 0], [0, 10, 0], AXIS_COLOR)
    pr.draw_line_3d([-10, 0, 0], [10, 0, 0], AXIS_COLOR)
    
    #pr.draw_sphere([5, 5, 5], 0.2, [0, 0, 255, 255])
    for row in csv.scaled_rows:
        color = [*csv.label_color[row['label']], 255]
        pr.draw_sphere([row['x'], row['y'], row['z']], 0.3, color)
    
    pr.end_mode_3d()
    pr.end_drawing()
pr.close_window()