# SelfDrivingDeliveryVehicle
---
### Obstacle Avoidance • STOP Sign Detection • ESP32 Camera Streaming • Arduino Control

This repository contains an autonomous robot car system that:
- Streams video from an ESP32-CAM
- Runs a Keras/TensorFlow image classification model
- Detects STOP signs and stops the car
- Performs ultrasonic-based obstacle avoidance
- Controls motors via a motor driver
- Uses a servo to rotate the camera for special target behavior (e.g., "banana" detection)
- Runs the full control loop from `main.py`

---

## Table of Contents
1. [Quick Start](#quick-start)
2. [Features](#features)
3. [Hardware Requirements & Wiring](#hardware-requirements--wiring)
4. [Software Structure](#software-structure)
5. [Installation](#installation)
6. [Future Improvements](#future-improvements)
7. [Contributing](#contributing)

---

## Quick Start

1. Put your `keras_model.h5` and `labels.txt` in the project root and ensure python version 3.11.9 is installed
2. Verify `STREAM_URL` in `main.py` (default: `http://192.168.4.1:81/stream`).
3. Power your car and ensure ESP32 stream is online.
4. Run:

---

# Features

## AI Detection
- Real-time inference with Keras model (`keras_model.h5`)
- STOP sign detection → car immediately stops
- Banana detection → servo rotates
- Continuous frame analysis from ESP32-CAM

## Wireless Camera Streaming
- Reads live video feed from ESP32-CAM
- Converts frames to RGB for AI processing
- Displays real-time feed in GUI (optional)

## Obstacle Avoidance
- Ultrasonic sensor checks distance continuously
- Performs avoidance routine when object detected
- Median filter reduces noise in measurements

## Navigation / Motor Control
- Motor driver controlled via GPIO pins
- Commands supported: `go_straight()`, `turn()`, `reverse()`, `stop()`
- Safe integration with AI and obstacle logic

## Servo Camera System
- Camera initially centered
- Rotates 90° to the right when target detected
- Returns to center after delay
- Integrated with AI logic in `CarController`

--

# Hardware Requirements & Wiring

**Required Hardware**
- Arduino (or microcontroller running Python 3.11.9)
- ESP32-CAM module
- L298N (or equivalent) Motor Driver
- 4× DC Gear Motors
- Ultrasonic sensor (HC-SR04)
- Servo motor (SG90 or MG90S)
- Power supply (batteries or regulated)

**Suggested GPIO mapping**
- Motors: GPIO 3, 6, 7, 8
- Ultrasonic Trigger: GPIO 23
- Ultrasonic Echo: GPIO 24
- Servo Signal: GPIO 12

> Adjust pins in `navigation.py`, `obstacle_avoidance.py`, and `servo.py` if needed.

---

# Software Structure

The project has the following file structure:

```text
main.py                  # Main autonomous control loop
camera_feed.py           # ESP32 video capture
ai_model.py              # AI prediction wrapper
car_controller.py        # Main car logic (AI + Servo + Driving)
obstacle_avoidance.py    # Ultrasonic sensor handling
navigation.py            # Motor movement functions
servo.py                 # Camera servo control
model.py                 # Loads Keras model
keras_model.h5           # Neural network file
labels.txt               # Labels for the model
README.md                # Documentation
```

---

# Installation

---

## 1. Set Up Python Environment

Create a Python virtual environment to isolate the project dependencies from your system Python. Activate the environment before proceeding to install packages.

---

## 2. Install Required Packages

Install the required Python packages

---

## 3. Add AI Model Files

Place the AI model files in the project root:

- `keras_model.h5` — Your trained AI model.  
- `labels.txt` — Class labels used by the AI model.

Ensure the filenames match exactly, otherwise the software will not detect them.

[![Watch the installation video](https://img.youtube.com/vi/VIDEO_ID/0.png)](https://illinoisstateuniversity-my.sharepoint.com/:v:/r/personal/elechni_ilstu_edu/Documents/Ethan%20L%20-%20Instruction%20Video.mkv?csf=1&web=1&e=BUcoqt&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D
)

---

## 4. Verify Python Version

Make sure your system uses Python version 3.11.9 or newer to ensure compatibility with TensorFlow and Keras.

---

## ✅ Summary

- Set up a Python virtual environment.  
- Install required Python packages.  
- Place `keras_model.h5` and `labels.txt` in the project root.  
- Verify that Python is version 3.11.9.

Once these steps are complete, your project is ready to run using `main.py`.

---

# Future Improvements

---

## 1. Advanced Obstacle Avoidance
- Add multiple sensors or LiDAR for 360° detection.  
- Implement path planning for complex environments.

## 2. Improved AI Detection
- Train on additional traffic signs and objects.  
- Explore lightweight AI models for faster performance.

## 3. Autonomous Navigation
- Integrate GPS or SLAM for outdoor and unknown areas.  
- Optimize routes for multiple destinations.

## 4. User Interface Upgrades
- Develop a mobile or web app for live monitoring.  
- Add manual override controls for safety.

## 5. Hardware Enhancements
- Upgrade motors, battery, and servo mechanisms.  
- Support modular sensor attachments.

## 6. Logging and Diagnostics
- Log sensor readings, AI detections, and motor actions.  
- Add error handling and performance metrics.

---

# Contributing

---

## How to Contribute

1. **Fork the repository**  
2. **Create a new branch** for your feature or fix:  
   - `git checkout -b feature-name`  
3. **Make your changes** in the new branch  
4. **Commit your changes** with clear messages  
5. **Push your branch** to your fork  
6. **Open a Pull Request** to merge your changes into the main repository  

---

## Guidelines

- Write clear, readable code and comments  
- Test your changes before submitting  
- Follow existing code style for consistency  
- Include explanations for new features in your PR description

---

## Reporting Issues

If you find a bug or want to suggest a feature:

- Open an **Issue** in the GitHub repository  
- Provide a clear description and steps to reproduce (if applicable)

---
