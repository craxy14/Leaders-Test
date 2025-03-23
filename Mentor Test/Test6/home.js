const form = document.getElementById("taskForm")
const resultDiv = document.getElementById("resultDiv")
const profileH1 = document.getElementById("profileH1")

profileH1.innerHTML = `Hello, ${JSON.parse(localStorage.getItem("Users")).username[0].toUpperCase() + JSON.parse(localStorage.getItem("Users")).username.slice(1,)}! Add Tasks:`

const removeTask = (button) => {
    button.parentElement.remove();

    const tasks1 = JSON.parse(localStorage.getItem("Tasks"));

    const itemName = button.parentElement.firstElementChild.firstChild.textContent;
    const updatedTasks = tasks1.filter((task) => task.taskName !== itemName);

    console.log(updatedTasks)
    localStorage.setItem("Tasks", JSON.stringify(updatedTasks));
}


const loadRender = () => {
    resultDiv.innerHTML = ""
    loadTasks = JSON.parse(localStorage.getItem("Tasks"))

    if(!loadTasks){
        resultDiv.innerHTML += `
        <h2>No tasks yet!</h2>
        `
    }else {
        for(let i = 0; i < loadTasks.length; i++){
            resultDiv.innerHTML += `
        <div id="taskDiv">
            <p id="taskNameP">${loadTasks[i].taskName}</p>
            <p id="taskDescP">${loadTasks[i].taskDesc}</p>
            <p id="date">${new Date()}</p>
            <button id="removeBtn" onclick="removeTask(this)">Remove Task</button>
        </div>`
        }
    }
}

window.onload = loadRender() 

form.addEventListener("submit", (e) => {
    e.preventDefault();

    let tasks = JSON.parse(localStorage.getItem("Tasks")) || []
    console.log(tasks)

    const newTask = {
        taskName: form.taskName.value,
        taskDesc: form.taskDesc.value
    };

    tasks.push(newTask);

    localStorage.setItem("Tasks", JSON.stringify(tasks));
    displayTasks(JSON.parse(localStorage.getItem("Tasks")))
    form.reset()
});

const displayTasks = (tasksArr) => {
    resultDiv.innerHTML = ""
    
    for(let i = 0; i < tasksArr.length; i++){
        resultDiv.innerHTML += `
    <div id="taskDiv">
        <p id="taskNameP">${tasksArr[i].taskName}</p>
        <p id="taskDescP">${tasksArr[i].taskDesc}</p>
        <p id="date">${new Date()}</p>
        <button id="removeBtn">Remove Task</button>
    </div>`
    }
}