import time

base_x = 0
base_y = 360

button_battle_left = (317, 900)
button_battle_right = (670, 850)
button_skip = (570, 950)
button_buff_exit = (815, 650)
button_proceed_left = (175, 800)
button_proceed_right = (850, 850)
button_chest_center = (500, 950)
button_chest_proceed = (800, 1100)
button_attack = (500, 1025)
button_start_battle = (870, 1117)
button_auto = (919, 1074)
button_speedup = (928, 1140)
button_victory_ok = (503, 1040)
button_last_chest = (800, 860)
button_skull = (50, 600)
button_skull_collect = (500, 950)
button_towerpoints = (125, 1111)
button_towerpoints_collect = (500, 1100)

def click_button(button):
    mouse.click_relative(button[0] - base_x, button[1] - base_y, 1)

def button_target(level):
    if level == 50:
        return button_last_chest
    if level % 2 == 1:
        return button_battle_left
    else:
        return button_battle_right

def button_proceed(level):
    if level % 2 == 1:
        return button_proceed_left
    else:
        return button_proceed_right

def clear_fight(level):
    button_battle = button_target(level)
    click_button(button_battle)
    time.sleep(0.25)
    click_button(button_attack) 
    time.sleep(0.25)
    click_button(button_start_battle)
    time.sleep(5) # Wait for battle to load
    click_button(button_auto)
    click_button(button_speedup)
    time.sleep(16) # Wait for battle to finish
    click_button(button_victory_ok)
    time.sleep(5) # Wait for heroes to move

def clear_chest(level):
    button_chest = button_target(level)
    click_button(button_chest)
    time.sleep(0.25)
    click_button(button_chest_center)
    time.sleep(2)
    click_button(button_chest_proceed)
    time.sleep(5)
    
def clear_skip(level):
    button_battle = button_target(level)
    click_button(button_battle)
    time.sleep(0.25)
    click_button(button_skip)
    time.sleep(5)

def clear_buff(level):
    button_buff = button_target(level)
    click_button(button_buff)
    time.sleep(0.25)
    click_button(button_buff_exit)
    time.sleep(0.25)
    click_button(button_proceed(level))
    time.sleep(5)
    
    
def dispatch_level(level, fight, buff, chest):
    table = {
        1:  fight,
        2:  buff,
        3:  fight,
        4:  chest,
        5:  fight,
        6:  buff,
        7:  fight,
        8:  chest,
        9:  fight,
        10: chest,
        11: fight,
        12: buff,
        13: fight,
        14: chest,
        15: fight,
        16: chest,
        17: fight,
        18: buff,
        19: fight,
        20: chest,
        21: fight,
        22: chest,
        23: fight,
        24: buff,
        25: fight,
        26: chest,
        27: fight, 
        28: chest,
        29: fight,
        30: buff,
        31: fight,
        32: chest,
        33: fight,
        34: fight,
        35: chest,
        36: fight,
        37: buff,
        38: fight,
        39: chest,
        40: fight,
        41: fight,
        42: chest,
        43: buff,
        44: fight,
        45: fight,
        46: chest,
        47: fight,
        48: buff,
        49: fight,
        50: chest
    }
    table[level](level)

# https://hero-wars.fandom.com/wiki/Tower
def clear_level(level):
    level_skip = 26
    def fight(level):
        if level <= level_skip:
            clear_skip(level)
        else:
            clear_fight(level)
    dispatch_level(level, fight, clear_buff, clear_chest)

def clear_rewards():
    click_button(button_skull)
    time.sleep(0.25)
    click_button(button_skull_collect)
    time.sleep(0.5)
    
    click_button(button_towerpoints)
    time.sleep(0.25)
    click_button(button_towerpoints_collect)
    time.sleep(0.25)

def main():
    firefox = "Navigator.Firefox"
    window.resize_move(firefox, xOrigin=0, yOrigin=base_y, width=1000, height=1000, matchClass=True)
    window.activate(firefox, switchDesktop=True, matchClass=True)
    time.sleep(0.25)
    
    for level in range(51, 51):
        clear_level(level)
        
    clear_rewards()
    dialog.info_dialog(message="Finished running tower")
    
main()

        
