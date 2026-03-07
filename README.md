# 📋 Flask To-Do Web Application

A full-stack **task management web application** built using **Flask, JavaScript, and PostgreSQL**.
The application allows users to register, log in, and manage their daily tasks with dynamic updates using the Fetch API (AJAX).

---

## 🚀 Live Demo

Live Application:
https://to-do-flask-app-4vev.onrender.com

---

## 📸 Screenshots

### Register Page
![Register Page](screenshots/(1)Register.png)

### Registration successful
![Registration Successful](screenshots/(2)Registration-successful.png)

### Login Page
![Login Page](screenshots/(3)Login.png)

### Login successful
![Login Successful](screenshots/(4)Login-successful.png)

### Adding Tasks
![Before Adding](screenshots/(5)Adding%20task-1.png)
![After Adding](screenshots/(8)Adding%20task-2-done.png)

### Task Management
![Toggle Status](screenshots/(9)toggle%20status.png)
![Delete Tasks](screenshots/(10)Delete%20task.png)
![Edit Task](screenshots/(11)Edit%20task.png)
![Clear All Tasks](screenshots/(13)All%20tasks%20cleared.png)

### Logout
![Logout](screenshots/(14)Logged%20out.png)

---

## 📌 Features

* User Registration and Login
* Secure Password Hashing
* Session-based Authentication
* Create Tasks
* Edit Tasks
* Delete Tasks
* Toggle Task Status (Pending / Completed)
* Clear All Tasks
* Dynamic Task Loading using Fetch API
* Toast Notifications for User Feedback
* Responsive Task Table UI

---

## 🛠️ Tech Stack

### Backend

* Flask
* SQLAlchemy
* Gunicorn

### Frontend

* HTML5
* CSS3
* JavaScript
* Fetch API (AJAX)

### Database

* PostgreSQL

### Deployment

* Render
* GitHub

---

## 📂 Project Structure

```
To_Do_Flask_App
│
├── static
│   ├── css
│   └── js
│       └── tasks.js
│
├── templates
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation (Run Locally)

### 1️⃣ Clone the repository

```
git clone https://github.com/anupam311/To_Do_Flask_App.git
cd To_Do_Flask_App
```

---

### 2️⃣ Create a virtual environment

```
python -m venv venv
```

Activate it

**Windows**

```
venv\Scripts\activate
```

**Mac / Linux**

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Configure environment variables

Set the database URI

```
SQLALCHEMY_DATABASE_URI=your_database_url
```

Example

```
postgresql://username:password@host:port/database
```

---

### 5️⃣ Run the application

```
python app.py
```

The app will start on

```
http://127.0.0.1:5000
```

---

## 📖 API Routes

| Route          | Method | Description        |
| -------------- | ------ | ------------------ |
| `/tasks`       | GET    | Fetch all tasks    |
| `/add`         | POST   | Add a new task     |
| `/toggle/<id>` | POST   | Toggle task status |
| `/delete/<id>` | POST   | Delete a task      |
| `/edit/<id>`   | POST   | Edit a task        |
| `/clear`       | POST   | Clear all tasks    |

---

## 👨‍💻 Author

**Anupam Chaudhary**

GitHub:
https://github.com/anupam311

---

## 📜 License

This project is created for educational and portfolio purposes.
