//static/js/tasks.js

document.addEventListener("DOMContentLoaded", loadTasks);


/* ---------- CREATE TASK TABLE (REUSED) ---------- */

function createTaskTable(){
    const taskListDiv = document.querySelector(".task-list");

    const emptyMsg = document.querySelector(".task-list p");
    if (emptyMsg) emptyMsg.remove();

    const table = document.createElement("table");
    table.classList.add("task-table");

    table.innerHTML = `
        <thead>
            <tr>
                <th>Title</th>
                <th>Description</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody id="task-body"></tbody>
    `;

    taskListDiv.prepend(table);

    const clear_button = document.createElement('button');
    clear_button.textContent = 'Clear All Tasks';
    clear_button.setAttribute('id','clear-all-tasks');
    clear_button.setAttribute('onclick','clearAllTasks(event)');
    taskListDiv.prepend(clear_button);

    const heading = document.createElement('h3');
    heading.textContent = 'Your Tasks';
    heading.setAttribute('id', 'task-heading');
    taskListDiv.prepend(heading);
}


/* ---------- LOAD TASKS ---------- */

async function loadTasks() {
    const response = await fetch("/tasks");
    const tasks = await response.json();

    if (tasks.length > 0){

        let task_body = document.querySelector('#task-body');

        if (!task_body) {
            createTaskTable();
            task_body = document.querySelector('#task-body');
        }

        tasks.forEach(task => {
            const row = `
                <tr data-id="${task.id}">
                    <td>${task.title}</td>
                    <td>${task.description}</td>
                    <td>${task.status}</td>
                    <td>
                        <button class="edit_button" onclick="editTask(event)">Edit</button>
                        <button class="toggle_button" onclick="toggle(event)">Toggle</button>
                        <button class="delete_button" onclick="deleteTask(event)">Delete</button>
                    </td>
                </tr>
            `;
            task_body.insertAdjacentHTML("beforeend", row);
        });

    } else{
        const taskListDiv = document.querySelector(".task-list");
        taskListDiv.innerHTML=`
        <p>No task found. Add a new task to get started.</p>`
    }
}


/* ---------- ADD TASK ---------- */

async function addTask(event) {
    event.preventDefault();

    const title = document.getElementById("title").value
    const description = document.getElementById("description").value

    const response = await fetch("/add", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title,
            description: description
        })
    });

    const data = await response.json();

    if (data.state === "info") {

        let task_body = document.querySelector('#task-body');

        if (!task_body) {
            createTaskTable();
            task_body = document.querySelector('#task-body');
        }

        const row = document.createElement('tr');
        row.classList.add('task-box');
        row.setAttribute('data-id', data.task_id);

        row.innerHTML = `
            <td>${title}</td>
            <td>${description}</td>
            <td>pending</td>
            <td>
                <button class="edit_button" onclick="editTask(event)">Edit</button>
                <button class="toggle_button" onclick="toggle(event)">Toggle</button>
                <button class="delete_button" onclick="deleteTask(event)">Delete</button>
            </td>`;

        task_body.append(row);

        showToast(data.message, data.state);
        document.getElementById("add-task-form").reset();
    }
}


/* ---------- TOGGLE STATUS ---------- */

async function toggle(event) {
    event.preventDefault();

    const row = event.target.closest("tr");
    const taskId = row.dataset.id;

    const response = await fetch(`/toggle/${taskId}`, {
        method: "POST"
    });

    const data = await response.json();

    if (data.state === "success") {
        row.children[2].innerText = data.new_status;
    }
}


/* ---------- DELETE TASK ---------- */

async function deleteTask(event) {
    event.preventDefault();

    const task_body = document.getElementById('task-body');
    const row = event.target.closest("tr");
    const taskId = row.dataset.id;

    const response = await fetch(`/delete/${taskId}`, {
        method: "POST"
    });

    const data = await response.json();

    if (data.state === "success") {
        row.remove();

        if (task_body.children.length === 0){
            document.querySelector('.task-list').innerHTML =
            `<p>No task found. Add a new task to get started.</p>`
        }

        showToast(data.message, "success");
    }
}


/* ---------- CLEAR ALL TASKS ---------- */

async function clearAllTasks(event) {
    event.preventDefault();

    const response = await fetch(`/clear`, {
        method: "POST"
    });

    const data = await response.json();

    if (data.state === "success") {
        document.querySelector('.task-list').innerHTML =
        `<p>No task found. Add a new task to get started.</p>`
    }

    showToast(data.message, "success");
}


/* ---------- EDIT TASK ---------- */

async function editTask(event){

    const row = event.target.closest("tr");
    const taskId = row.dataset.id;

    const newTitle = prompt("Enter new title", row.children[0].innerText);
    const newDesc = prompt("Enter new description", row.children[1].innerText);

    if (!newTitle || !newDesc) return;
    
    const response = await fetch(`/edit/${taskId}`,{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            title:newTitle,
            description:newDesc
        })
    });

    const data = await response.json();

    if(data.state === "success"){
        row.children[0].innerText = newTitle;
        row.children[1].innerText = newDesc;
    }
}