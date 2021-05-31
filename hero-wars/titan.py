import time
import random

store.set_global_value("STOP", False)
base_x = 0
base_y = 360
num_levels_per_floor = 5
num_levels_per_floorset = 10
button_auto = (919, 1074)
button_speedup = (928, 1140)
button_victory_ok = (503, 1040)
button_dungeon_single = (515, 780)
button_dungeon_double_left = (305, 720)
button_dungeon_double_right = (700, 720)
button_attack = (500, 1000)
button_attack_left = (272,1004)
button_attack_right = (726,1019)
button_start_battle = (870, 1117)
button_activate = (260, 760)
button_activate_collect = (700, 1000)

num_floors_cleared = 0

def get_level():
    return int(store.get_global_value("TITAN_LEVEL") or 0)

def get_stopped():
    return store.get_global_value("STOP")

def click_button(button):
    mouse.click_relative(button[0] - base_x, button[1] - base_y, 1)

def clear_level():
    if get_stopped():
        return
    level_number = get_level()
    click_button(button_dungeon_single)
    click_button(random.choice([ button_dungeon_double_left, button_dungeon_double_right ]))
    #click_button(button_dungeon_double_left)
    #click_button(button_dungeon_double_right)
    time.sleep(0.25)
    click_button(button_attack)
    click_button(button_attack_right) 
    time.sleep(0.25)
    click_button(button_start_battle)
    time.sleep(6) # Wait for battle to load
    click_button(button_auto)
    click_button(button_speedup)
    time.sleep(10) # Wait for battle to finish
    click_button(button_victory_ok)
    store.set_global_value("TITAN_LEVEL", level_number+1)
    
    time.sleep(5) # Wait for titans to move through dungeon
    if level_number % 10 == 5:
        time.sleep(10) # End of floor takes a little longer to move through
    if level_number % 10 == 0:
        click_button(button_activate)
        time.sleep(12) # Wait for window to shift up and back down
        click_button(button_activate_collect)
        time.sleep(10) # Wait for titans to move to next floor
    # Ready for another loop

def main():
    firefox = "Navigator.Firefox"
    window.resize_move(firefox, xOrigin=0, yOrigin=0, width=1000, height=1000, matchClass=True)
    dialog_info = dialog.input_dialog(message=f"Level {get_level()}. How many to clear?")
    if not (dialog_info[0] == 0 and dialog_info[1] != ''):
        dialog.info_dialog(message=f"Got error code {dialog_info[0]}")
        return
    num_levels = int(dialog_info[1])
    window.activate(firefox, switchDesktop=True, matchClass=True)
    time.sleep(0.25)
    for i in range(num_levels):
        clear_level()
    dialog.info_dialog(message=f"Done clearing {num_levels} floors. New level number={get_level()}")
main()
