const form = document.getElementById('p-form')
const name = document.getElementById('id_name')
const username = document.getElementById('id_username')
const img = document.getElementById('id_img')

const url = "http://127.0.0.1:8000/create/"

const csrf = document.getElementsByName('csrfmiddlewaretoken')

console.log(csrf)



form.addEventListener('submit', e=>{
  e.preventDefault()

  const fd = new FormData()
  fd.append('csrfmiddlewaretoken', csrf[0].value)
  fd.append('name', name.value)
  fd.append('username', username.value)
  fd.append('img', img.files[0])

  $.ajax({
    type: 'POST',
    url: url,
    enctype: 'multipart/form-data',
    data: fd,
    success: function(response){
        console.log(response)
    },
    error: function(error){
        console.log(error)
    },
    catch: false,
    contentType: false,
    processData: false,
  });
});