# Mechatronics & Computer Vision Portfolio

Welcome to my engineering portfolio repository. Below are selected projects highlighting my work in embedded systems, computer vision, and mechatronic design.

---

## Project 1: Real-Time Shape & Color Inspection System
* **Tech Stack:** Python, TensorFlow, Keras, MobileNetV2, OpenCV, NumPy, Pandas.
* **Description:** Developed a hybrid computer vision pipeline combining classical image processing with deep learning for real-time shape classification and color attribute sorting.
* **Key Features:**
  * Implemented transfer learning using a frozen MobileNetV2 backbone trained via TensorFlow/Keras.
  * Integrated real-time OpenCV video streaming (`cv2.VideoCapture`) with Canny edge detection and HSV color space masking.

---

## Project 2: Active Boat Stabilization System (Control Systems & Modeling)
* **Context:** Collaborative University Semester Project (SPRO 4).
* **My Individual Contributions:**
  * **Mathematical Modeling & Linearization:** Formulated the non-linear lumped parameter dynamics for the boat hull and airkeel, applying Taylor series expansions around the equilibrium setpoint (phi = 0) to linearize roll equations.
  * **System Identification & Transfer Function:** Computed empirical transfer functions relating keel angle inputs to boat roll outputs using MATLAB's System Identification Toolbox, identifying non-minimum phase characteristics (right-half-plane zeros).
  * **Control System Design:** Evaluated Internal Model Control (IMC) strategies and tuned digital PID controllers using MATLAB's PID tuner application.

---

## Project 3: Autonomous Warehouse Forklift (Path Planning & Navigation)
* **Context:** Collaborative University Semester Project (SPRO 3).
* **My Individual Contributions:**
  * **Path Planning & Mapping (Software .1):** Implemented a Greedy Best First Search (GBFS) path-planning algorithm in Python using `NetworkX` and `Matplotlib` on a discrete grid coordinate map.
  * **Dynamic Obstacle Avoidance (Software .2):** Developed real-time logic parsing angular and distance telemetry from an LD06 LiDAR sensor to detect unmapped obstacles, automatically setting occupied node costs to infinity for instant route replanning.

---
