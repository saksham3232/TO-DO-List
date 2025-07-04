# 📝 To-Do List App (FastAPI + Streamlit)

A simple, minimal full-stack To-Do List web application built using **FastAPI** (Python backend) and **Streamlit** (Python frontend). This project demonstrates CRUD operations (Create, Read, Update, Delete) on To-Do items with an interactive web UI.

---

## ✨ Features

- **Create** new To-Do items with title and description
- **View** all To-Do items in an organized layout
- **Update** existing To-Do items by ID
- **Delete** To-Do items by ID
- **Real-time UI**: Instant feedback and automatic refreshes after actions

---

## 🚀 Tech Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Frontend:** [Streamlit](https://streamlit.io/) (Python)
- **HTTP Client:** [requests](https://docs.python-requests.org/en/latest/)
- **Data Storage:** In-memory Python dictionary (for demonstration)

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/saksham3232/TO-DO-List.git
cd TO-DO-List
```

### 2. Install dependencies

```bash
pip install fastapi uvicorn streamlit requests
```

### 3. Start the FastAPI backend server

```bash
uvicorn main:app --reload
```
By default, this will run on `http://localhost:8000`.

### 4. Run the Streamlit frontend

In a **new terminal window/tab**:

```bash
streamlit run app.py
```
The Streamlit app will open in your browser (usually at `http://localhost:8501`).

---

## 🛠️ Project Structure

```
.
├── app.py       # Streamlit frontend
├── main.py      # FastAPI backend
└── README.md    # Project documentation
```

---

## 📋 API Endpoints

- `POST /todos/` : Create a new To-Do
- `GET /todos/` : Get all To-Dos
- `GET /todos/{id}` : Get a specific To-Do by ID
- `PUT /todos/{id}` : Update a To-Do by ID
- `DELETE /todos/{id}` : Delete a To-Do by ID

All endpoints use JSON payloads.

---

## 🎯 Usage

- **Add a To-Do**: Fill out the ID, Title, and Description and click "Add To-Do".
- **View All**: All To-Do items are displayed with their details.
- **Update a To-Do**: Enter the To-Do ID, new Title, and Description, then click "Update To-Do".
- **Delete a To-Do**: Enter the To-Do ID and click "Delete To-Do".

---

## ⚠️ Notes

- The backend uses an **in-memory Python dictionary** (`todo_list`) so data will reset when the backend restarts.
- Make sure the FastAPI server is running before starting the Streamlit app.
- The API base URL in `app.py` is set to `http://localhost:8000` by default.

---

## 🙋‍♂️ Author

- [saksham3232](https://github.com/saksham3232)

---

## ⭐️ Show your support

If you like this project, please give it a ⭐️ on [GitHub](https://github.com/saksham3232/TO-DO-List)!