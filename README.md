# Flask Task API

This is a simple REST API built with Flask that supports CRUD operations for a "Task" entity using in-memory storage. A simple frontend html file has also been made for user input

## Features

- Create, read, update, and delete tasks
- Filter tasks by completion status (`is_completed`)
- In-memory data (no database setup required)

## Requirements

- Python 3.7+
- Flask
- flask-cors

## Setup & Run

1. **Clone the repo**

   ```bash
   git clone https://github.com/Shabbir05/webinix_task.git
   cd webinix_task.git
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**

   ```bash
   python main.py
   ```

4. **Visit in browser or use tools like Postman**
   ```
   http://127.0.0.1:5000/tasks
   ```

5. **Open the front end part by double-clicking on the index.html file**
   ```
   index.html
   ```
