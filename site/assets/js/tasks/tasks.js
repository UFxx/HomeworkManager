const openTask = document.querySelectorAll('.task .fa-chevron-down');

openTask.forEach(el => {
    el.addEventListener('click', () => {
        el.parentElement.parentElement.classList.toggle('task-close');
        el.classList.toggle('expand-task-opened');
    })
})