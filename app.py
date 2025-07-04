import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

st.set_page_config(page_title="To-Do List App", page_icon="📝")
st.title("📝 To-Do List App (FastAPI + Streamlit)")

# Create a new To-Do
st.header("➕ Create a New To-Do Item")
todo_id = st.number_input("ID", min_value=1, step=1, key="create_id")
todo_title = st.text_input("Title", key="create_title")
todo_description = st.text_area("Description", key="create_description")
if st.button("Add To-Do"):
    response = requests.post(
        f"{BASE_URL}/todos/",
        json={"id": todo_id, "title": todo_title, "description": todo_description}
    )
    if response.status_code == 200:
        st.success("✅ To-Do item added successfully!")
        st.rerun()
    else:
        st.error(f"❌ Error: {response.json().get('detail')}")

# View all To-Do items
st.header("📋 All To-Do Items")
response = requests.get(f"{BASE_URL}/todos/")
if response.status_code == 200:
    todos = response.json()
    if not todos:
        st.info("No To-Do items found.")
    else:
        for todo in todos:
            with st.expander(f"📌 {todo['title']} (ID: {todo['id']})"):
                st.write(f"📄 Description: {todo['description']}")
else:
    st.error("❌ Failed to fetch To-Do items.")

# Update a To-Do
st.header("✏️ Update To-Do Item")
update_id = st.number_input("Enter To-Do ID to update", min_value=1, step=1, key="update_id")
new_title = st.text_input("New Title", key="update_title")
new_description = st.text_area("New Description", key="update_description")
if st.button("Update To-Do"):
    response = requests.put(
        f"{BASE_URL}/todos/{update_id}",
        json={"id": update_id, "title": new_title, "description": new_description}
    )
    if response.status_code == 200:
        st.success("✅ To-Do item updated successfully!")
        st.rerun()  # Force refresh after update
    else:
        st.error(f"❌ Error: {response.json().get('detail')}")

# Delete a To-Do
st.header("🗑️ Delete To-Do Item")
delete_id = st.number_input("Enter To-Do ID to delete", min_value=1, step=1, key="delete_id")
if st.button("Delete To-Do"):
    response = requests.delete(f"{BASE_URL}/todos/{delete_id}")
    if response.status_code == 200:
        st.success("🧹 To-Do item deleted successfully!")
        st.rerun()  # Force refresh after delete
    else:
        st.error(f"❌ Error: {response.json().get('detail')}")