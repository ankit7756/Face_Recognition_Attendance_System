# 👨‍🎓 Face Recognition Based Attendance Management System

A smart attendance management system that combines **AI-powered face recognition** with a **web-based dashboard** to automate and streamline the process of recording and managing student attendance.  

This project was developed as a **college group project** by a team of 4 ( Ankit Sharma, Pratik Neupane, Shreeya Poudel, Samekshya Baniya ), to demonstrate the practical application of Artificial Intelligence in solving real-world problems like classroom attendance.  

---

## 📌 About the Project

This system integrates two main parts:

1. **Face Recognition Model (Python)**  
   - Captures student faces through a webcam.  
   - Compares live faces with pre-saved images in the database.  
   - Automatically logs attendance in a CSV file if a match is found.  
   - Prevents duplicate entries for the same day.

2. **Web Application (MERN Stack)**  
   - Provides separate dashboards for **Admin, Teachers, and Students**.  
   - Allows admins/teachers to view, manage, and download attendance reports.  
   - Students can log in to check their attendance records.  
   - API integration with the Python model for automated data transfer.

The system is currently a **local prototype** for demonstration purposes but can be scaled into a cloud-based, real-time attendance management platform.

---

## 🧠 Technologies Used

### 🔹 Backend
- **Node.js** & **Express.js** – REST API and server-side logic  
- **MongoDB** – Database for storing user and attendance data  
- **dotenv** – Environment variable management

### 🔹 Frontend
- **React.js** – User interface and dashboards  
- **React Router** – Navigation and routing  
- **Axios** – API calls to backend services

### 🔹 AI/Model
- **Python 3.8** – Compatible with the `face_recognition` library  
- **OpenCV** – Real-time image capture and processing  
- **dlib** – Underlying library for facial recognition  
- **face_recognition** – High-level API for facial matching  
- **CSV** – Stores attendance logs locally

---

## ✅ Features

- **Face Recognition Model**
  - Real-time face detection via webcam
  - Matching against stored images
  - Automatic attendance logging with name, date, and time
  - Duplicate prevention for same-day entries

- **Web Dashboard**
  - Admin, Teacher, and Student login system
  - Attendance history view and filtering
  - Data visualization for quick insights
  - Downloadable attendance reports
  - Role-based access control

- **System Integration**
  - Python model generates encoded face data and logs attendance
  - Backend processes and stores attendance data in MongoDB
  - Frontend fetches and displays data for users

---
