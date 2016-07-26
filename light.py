#!/usr/bin/env python3
current_state = False

def light_switch():
    """XOR light switch, requires the global boolean current_state"""
    
    global current_state
    state = True
    toggle = state ^ current_state
    current_state = toggle
    
    if current_state == True:
        return "The light was turned on."
    return "The light was turned off."

if __name__ == "__main__":
    print(light_switch())
