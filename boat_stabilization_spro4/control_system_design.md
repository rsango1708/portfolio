# Control System & Controller Design (SPRO 4)

This document details the design, tuning, and evaluation of the closed-loop control system developed for the active boat stabilization prototype.

---

## 1. Control Loop Architecture
The feedback control loop was mapped to physical components of the system:
* **Controller:** Arduino MKR WiFi 1010.
* **Actuator:** Servo motor driving the airkeel.
* **Plant:** The boat hull, where the input is cumulative torque and the output is the roll angle.
* **Sensor:** MPU-9250 IMU providing real-time roll angle feedback via sensor fusion.

The controller compares the measured roll angle from the IMU against the desired setpoint ($0^\circ$) to compute the error and drive the servo position accordingly.

Here it can be seen how the boat angle and servo angle are opposite, due to the counteracting effect of the keel.
[Comparison of Keel and Boat angle](screenshots/comp.png)

---

## 2. Open-Loop Transfer Function Combination
The open-loop transfer function $G(s)$ was formed by multiplying the actuator (servo) and plant transfer functions:

$$G(s) = G_{actuator}(s) \cdot G_{plant}(s)$$

Due to the physical characteristics of the airkeel mechanism, the resulting plant exhibited **non-minimum phase behavior** (characterized by right-half-plane zeros, causing the boat to initially tilt in the opposite direction before correcting).

---

## 3. Controller Design Approaches & Comparison

Two distinct tuning methodologies were implemented and compared:

### Method A: Internal Model Control (IMC) Approach
* **Rationale:** IMC was initially chosen because it is theoretically effective for non-minimum phase systems with right-half-plane zeros, where traditional tuning methods like Ziegler-Nichols fail.
* **Implementation:** The open-loop transfer function was decomposed into invertible and non-invertible parts, and combined with a low-pass filter $F(s) = \frac{1}{(\lambda s + 1)^n}$ to attenuate high-frequency noise and prevent unstable pole/zero inversions.
* **Result:** The IMC approach yielded an unreasonable response with a massive settling time ($\ge 45$ seconds) and steady-state inversion. This occurred because the empirical plant transfer function contained poles too close to the origin.

### Method B: MATLAB PID Tuner App (Selected Method)
* **Rationale:** Given the limitations encountered with manual IMC calculations on the complex empirical model, MATLAB's automated **PID Tuner App** was utilized.
* **Result:** The PID tuner successfully generated a stable closed-loop step response that converged correctly, accounting for the system's non-minimum phase traits.
* **Output Saturation:** To prevent extreme oscillations typical of non-minimum phase systems, output saturation limits corresponding to the maximum and minimum allowable keel angles were integrated into the PID block.

---

## 4. Final Tuned PID Parameters
The controller gains computed via the MATLAB PID tuner app and implemented in the system were:
* **Proportional Term ($K_p$):** $-4.20$
* **Integral Term ($K_i$):** $-0.207$
* **Derivative Term ($K_d$):** $-4.64$
* **Filter Coefficient ($N$):** $21.17$

  The step response of the final controller can be seen here:
   [Final step response](screenshots/settlingtime.png)

---


### MATLAB / Simulink Simulation Files
The closed-loop control model used for simulation and controller validation can be accessed here:
* [Download Closed-Loop Simulink Model (.slxc)](Simulink_model/Semproj4Simulink.slxc)
