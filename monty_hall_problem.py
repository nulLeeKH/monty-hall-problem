#!/usr/bin/env python3

import random

def run_situation(selected, switch, opened, answer):
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
    return

if __name__ == "__main__":
    result = run_simulation()

