import pyray as pr

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
SCREEN_TITLE = 'Hello in 3 Dimensions!'

pr.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
pr.set_target_fps(60)

camera = pr.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)

while not pr.window_should_close():
    # pan camera on mouse down
    if pr.is_mouse_button_down(0):
        pr.update_camera(camera, pr.CAMERA_THIRD_PERSON)
        
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)
    pr.draw_fps(10, 10)
    
    pr.begin_mode_3d(camera)
    
    pr.draw_line_3d([0, 0, -10], [0, 0, 10], pr.BLACK)
    pr.draw_line_3d([0, -10, 0], [0, 10, 0], pr.BLACK)
    pr.draw_line_3d([-10, 0, 0], [10, 0, 0], pr.BLACK)
    
    pr.draw_sphere([5, 5, 5], 0.2, pr.BLUE)
    
    pr.end_mode_3d()
    pr.end_drawing()
pr.close_window()