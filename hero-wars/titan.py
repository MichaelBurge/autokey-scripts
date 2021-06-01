# Enter script code
# Displays the information of the next window to be left-clicked
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
button_dungeon_target1 = (500, 780)
button_dungeon_target2 = (700, 780)
button_dungeon_double_left = (305, 1000)
button_dungeon_double_right = (700, 1000)
button_attack = (500, 1000)
button_attack_left = (272,1004)
button_attack_right = (726,1019)
button_start_battle = (870, 1117)
button_activate = (260, 760)
button_activate_collect = (700, 1000)
button_divination_accept = (567, 1000)
button_divination_fight = (300, 1000)
num_floors_cleared = 0
num_divinations = 0

def get_level():
    return int(store.get_global_value("TITAN_LEVEL") or 0)

def get_stopped():
    return store.get_global_value("STOP")

def click_button(button):
    mouse.click_relative(button[0] - base_x, button[1] - base_y, 1)

def clear_divination():
    click_button(button_divination)
    time.sleep(1)
    
def dispatch_level(level, on_hero, on_single_titan, on_double_titan):
    table = {
        0: on_double_titan,
        1: on_hero,
        2: on_single_titan,
        3: on_hero,
        4: on_hero,
        5: on_double_titan,
        6: on_hero,
        7: on_double_titan,
        8: on_single_titan,
        9: on_double_titan
    }
    on_hero()
    on_double_titan()
    #table[level % 10]()

def clear_level(has_divination):
    if get_stopped():
        return
    level = get_level()    
    click_button(button_dungeon_target1)
    click_button(button_dungeon_target2)
    time.sleep(0.25)
    # Never use divination cards
    if has_divination:
        click_button(button_divination_fight)
        time.sleep(0.25)
    def on_single():
        click_button(button_attack)
    def on_double():
        click_button(random.choice([ button_dungeon_double_left, button_dungeon_double_right ]))
    dispatch_level(level, on_single, on_single, on_double) 
    time.sleep(0.25)
    click_button(button_start_battle)
    time.sleep(6) # Wait for battle to load
    click_button(button_auto)
    click_button(button_speedup)
    time.sleep(15) # Wait for battle to finish
    click_button(button_victory_ok)
    store.set_global_value("TITAN_LEVEL", level+1)
    
    if level % 10 == 5:
        time.sleep(10) # End of floor takes a little longer to move through
    elif level % 10 == 0:
        click_button(button_activate)
        time.sleep(6) # Wait for window to shift up and back down
        click_button(button_activate_collect)
        time.sleep(10) # Wait for titans to move to next floor
    else:
        time.sleep(6) # Wait for titans to move through dungeon
    # Ready for another loop

def main():
    firefox = "Navigator.Firefox"
    window.resize_move(firefox, xOrigin=0, yOrigin=base_y, width=1000, height=1000, matchClass=True)
    dialog_info = dialog.input_dialog(message=f"Level {get_level()}. How many to clear?")
    if not (dialog_info[0] == 0 and dialog_info[1] != ''):
        dialog.info_dialog(message=f"Got error code {dialog_info[0]}")
        return
    num_levels = int(dialog_info[1])
    window.activate(firefox, switchDesktop=True, matchClass=True)
    time.sleep(0.25)
    for i in range(num_levels):
        clear_level(True)
    dialog.info_dialog(message=f"Done clearing {num_levels} floors. New level number={get_level()}")
main()
