#!/usr/bin/env python3

import random
import sys

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

def run_simulation(count):
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
    
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + "monty_hall_problem.py <count>")
        exit()
    count = int(sys.argv[1])
    result = run_simulation(count)

