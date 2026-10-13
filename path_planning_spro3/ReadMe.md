# Warehouse Forklift Path Planning & Navigation (SPRO 3)

This folder contains the path-planning and navigation software developed for an autonomous warehouse mobile robot.

### Files:
* `pathplanidle.py`: Implements a hierarchical Greedy Best-First Search (GBFS) algorithm using NetworkX and Matplotlib. It builds a grid-based coordinate map, manages region-based node exploration, incorporates static obstacles, and visualizes the calculated route.

### How to Run:
Make sure you have the required dependencies installed:
bash
pip install networkx matplotlib numpy
python pathplanidle.py
