import webcolors as wb
from google.cloud import vision
from google.cloud.vision import types
from ColorPostRequest import getColor



common_colors = {"#FFFFFF":"white",
				 "#808080":"gray",
				 "#000000":"black",
				 "#FF0000":"red",
				 "#FFFF00":"yellow",
				 "#008000":"green",
				 "#0000FF":"blue",
				 "#800080":"purple",
				 "#E5760B":"orange",
				 "#7CA7E6":"lightblue",
				 "#DEBD8B":"tan"
				 } 


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in common_colors.items():
        r_c, g_c, b_c = wb.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]



def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = wb.rgb_to_name(requested_colour, spec=u'html4')
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

def clothes_color(path):
	actual_name, closest_name = get_colour_name(getColor(path))
	return(closest_name)
