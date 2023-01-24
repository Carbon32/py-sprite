# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                           #
#                    Python Pixel Editor                    #
#                     Developer: Carbon                     #
#                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Imports: #

from src.editor import *

# Pixel Editor: #

editor = Editor(800, 600, 1920, 1080)
editor.start_window()

while(editor.window_running):
    editor.update_editor()
    editor.update_window(120)