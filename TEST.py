from tkinter import *
import tkintermapview 
from PIL import Image, ImageTk
import os

# Create a window
root = Tk()
root.title("Groud Controll Point")
root.geometry(f"{1000}x{800}")
root.iconbitmap('images/icon.ico')
#root.iconbitmap()


# create map widget
my_label = LabelFrame(root)
my_label.pack(pady=20)#padx, pady − How many pixels to pad widget, horizontally and vertically, outside v's borders
map_widget = tkintermapview.TkinterMapView(root, width=800, height=600, corner_radius=0)
map_widget.pack(fill="both", expand=True)
#map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# load images
current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
start_icon = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "images", "start_icon.png")).resize((30, 40)))
stop_icon= ImageTk.PhotoImage(Image.open(os.path.join(current_path, "images", "stop_icon.png")).resize((30, 40)))
#Set Coordinates
map_widget.set_position(55.998256, 37.223383)#Miet 
#Set zoom level
map_widget.set_zoom(17)



# set a position marker
marker_1 = map_widget.set_marker(55.997256, 37.223383, text="Miet", icon=start_icon)
marker_2 = map_widget.set_marker(55.998216, 37.224313, text="52.55, 13.4")


list_position = [marker_1.position, marker_2.position,[55.999176, 37.225893]]

# set a path
path_1 = map_widget.set_path(list_position)


def polygon_click(polygon):
    print(f"polygon clicked - text: {polygon.name}")
    
polygon_1 = map_widget.set_polygon(list_position,
                                   # fill_color=None,
                                   # outline_color="red",
                                   # border_width=12,
                                   command=polygon_click,
                                   name="switzerland_polygon")

# methods
# polygon_1.remove_position(46.3772542, 6.4160156)
# polygon_1.add_position(0, 0, index=5)
polygon_1.delete()

def add_marker_event(coords):
    print("Add marker:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="new marker")
    

map_widget.add_right_click_menu_command(label="Add Marker",
                                        command=add_marker_event,
                                        pass_coords=True)

def left_click_event(coordinates_tuple):
    print("Left click event with coordinates:", coordinates_tuple)
    
map_widget.add_left_click_map_command(left_click_event)

map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
# map_widget.delete_all_marker()
map_widget.pack()

root.mainloop()


