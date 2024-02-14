import numpy as np

def get_color_gradient(c1, c2, n):
    assert n > 1
    c1_rgb = np.array(c1) / 255
    c2_rgb = np.array(c2) / 255
    mix_pcts = [x / (n - 1) for x in range(n)]
    rgb_colors = [((1 - mix) * c1_rgb + (mix * c2_rgb)) for mix in mix_pcts]
    return [[int(round(x * 255)) for x in color] for color in rgb_colors]