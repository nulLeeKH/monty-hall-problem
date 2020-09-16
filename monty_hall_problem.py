#!/usr/bin/env python3

import random

def run_situation(selected, answer, opened, switch):
    if switch:
        if selected == answer:
            return False
        else:
            return True
    else:
        if selected == answer:
            return True
        else:
            return False

def run_simulation():
    result = {
        "switch": {
            "win": 0,
            "lose": 0
        },
        "unswitch": {
            "win": 0,
            "lose": 0
        }
    }
    
    return

if __name__ == "__main__":
    result = run_simulation()

