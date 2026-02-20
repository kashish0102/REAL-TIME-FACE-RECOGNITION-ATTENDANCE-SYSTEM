# Real-Time Face Recognition Attendance System

## Overview

This project is a real-time face recognition attendance system that identifies individuals from a live webcam feed and automatically updates attendance records in Firebase.
It uses deep-learning face embeddings for identity matching and integrates with Firebase Realtime Database and Cloud Storage for storing student metadata and images.

---

## Features

* Real-time face detection from webcam stream
* Face encoding generation using deep-learning embeddings
* Distance-based similarity matching for identification
* Automatic attendance update with timestamp validation
* Firebase Realtime Database integration for student records
* Firebase Storage integration for profile images
* Graphical UI with bounding boxes and student information display

---

## Tech Stack

Python
OpenCV
face_recognition
Firebase Realtime Database
Firebase Storage
NumPy
cvzone

---

## Project Structure

Main.py
Runs the real-time recognition system and handles attendance updates

EncodeGenerator.py
Generates face encodings from stored student images and uploads images to Firebase

AddDatatoDatabase.py
Adds initial student metadata into Firebase database

Resources/
Contains UI assets and mode images

Images/
Contains student face images used for encoding

---

## How It Works

1. Student images are loaded and converted into face embeddings
2. Embeddings are stored locally for fast matching
3. Webcam frames are captured in real time
4. Faces are detected and compared against known embeddings
5. If a match is found:

   * Student data is fetched from Firebase
   * Attendance count is updated
   * Timestamp is refreshed to prevent duplicate entries

---

## Run Locally

### 1. Install dependencies

### 2. Setup Firebase credentials

### 3. Prepare student images

Add student face images inside the Images folder.
Each filename should match the student ID.

### 4. Generate encodings

python EncodeGenerator.py

### 5. Add sample student data

python AddDatatoDatabase.py

### 6. Start the recognition system

python Main.py

---

## Important Notes

This project was built as a practical implementation of a real-time computer vision attendance workflow.
