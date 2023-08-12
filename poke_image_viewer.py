"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox
import poke_api
import image_lib
import ctypes
import inspect


# Get the script and images directory
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')
script_name = inspect.getframeinfo(inspect.currentframe()).filename


# TODO: Create the images directory if it does not exist
if not os.path.isdir(images_dir):
  os.makedirs(images_dir)

# Create the main window
root = Tk()
root.title("Pokemon Viewer")
root.iconbitmap('POKEBALL.png')
root.geometry('600x600')
root.minsize(500,600)
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

# TODO: Set the icon
icon_path = os.path.join(script_dir, 'Rankred')
app_id = 'COMP593.PokeimageViewer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
root.iconbitmap(os.path.join(script_dir, 'POKEBALL.png'))


# TODO: Create frames
frm = ttk.Frame(root)
frm.columnconfigure(0,weight=100)
frm.rowconfigure(0,weight=100)
frm.grid(row=0, column=0, sticky=NSEW)

#create the button to set desktop bg
def handle_set_desktop():
   """
   Event handler called when user clicks the "Set as Desktop Image" button.
   Sets the desktop bg image to the current Pokemon display image

   """
   image_lib.set_desktop_background_image(image_path)

btn_set_desktop = ttk.Button(frm, text='Set as Desktop Image', command=handle_set_desktop)

btn_set_desktop.state('Disabled')
btn_set_desktop.grid(row=1,column=1,padx=0,pady=(10,20)),

#create list of pull down pokemon names
pokemon_list = poke_api.get_pokemon_names()
pokemon_list.sort()
cbox_poke_sel = ttk.Combobox(frm, value=pokemon_list, state = 'readonly')
cbox_poke_sel.set("Select a pokemon")
cbox_poke_sel.grid(row=1, column=0, padx=0, pady=10)


def handle_os_sel(event):

    os_logo = ('WindowsLogo.png', 'MacOSLogo.png', 'LinuxLogo.png')
    sel_os_index = cbox_poke_sel.current()
    img_logo['file'] = os_logo[sel_os_index]
cbox_poke_sel.bind('<<ComboboxSelected>>', handle_os_sel)

# TODO: Populate frames with widgets and define event handler functions
image_path = os.path.join(script_dir, 'POKEBALL.png')
img_logo = PhotoImage(file=image_path)
label_image = ttk.Label(frm, image=img_logo)
label_image.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

root.mainloop()