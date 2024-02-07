import pyray as pr
import os
import src.csv_util as cu

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
SCREEN_TITLE = 'Hello in 3 Dimensions!'

pr.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
pr.set_target_fps(60)

BACKGROUND_COLOR = [240, 240, 240, 255]
AXIS_COLOR = [0, 0, 0, 255]

camera = pr.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)

csv = cu.CSV(os.path.join('.', 'data', 'iris.csv'))
csv.scale_rows(-10, 10)

while not pr.window_should_close():
    # pan camera on mouse down
    if pr.is_mouse_button_down(0):
        pr.update_camera(camera, pr.CAMERA_THIRD_PERSON)
        
    pr.begin_drawing()
    pr.clear_background(BACKGROUND_COLOR)
    pr.draw_fps(10, 10)
    
    pr.begin_mode_3d(camera)
    
    # draw 3d axis
    pr.draw_line_3d([0, 0, -10], [0, 0, 10], AXIS_COLOR)
    pr.draw_line_3d([0, -10, 0], [0, 10, 0], AXIS_COLOR)
    pr.draw_line_3d([-10, 0, 0], [10, 0, 0], AXIS_COLOR)
    
    #pr.draw_sphere([5, 5, 5], 0.2, [0, 0, 255, 255])
    for row in csv.scaled_rows:
        if row['species'] == 'setosa': color = [255, 0, 0, 255]
        if row['species'] == 'versicolor': color = [0, 255, 0, 255]
        if row['species'] == 'virginica': color = [0, 0, 255, 255]
        pr.draw_sphere([row['x'], row['y'], row['z']], 0.3, color)
    
    pr.end_mode_3d()
    pr.end_drawing()
pr.close_window()