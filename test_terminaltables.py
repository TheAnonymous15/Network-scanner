#!/usr/bin/env python3
try:
    from terminaltables import DoubleTable
    print("terminaltables is accessible")
except ImportError as e:
    print(f"ImportError: {e}")
