let form = document.getElementById('login-form')

form.addEventListener('submit', (e) => {
    e.preventDefault()
    let formData = {
        'username': form.username.value,
        'password': form.password.value
    }

    fetch(`http://127.0.0.1:8000/api/users/token/`, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
        },
        body:JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('DATA:', data)
        if(data.access){
            localStorage.setItem('token', data.access)
            window.location = "file:///D:/Django_Check/devsearch/frontend/project-list.html"
        }
        else{
            alert('Username or Password did not work')
        }
    })
})