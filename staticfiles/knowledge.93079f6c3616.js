function getstates(){
  var url = 'https://api.covid19india.org/resources/resources.json';
  var states = []
  var statenames = document.getElementById('statenames')
  fetch(url)
  .then(function(response){
    return response.json();
  })
  .then(function(myJson){
    statenames.innerHTML = `<option value=""></option>`
    myJson.resources.forEach(myprinter);
    function myprinter(item){
      if(states.includes(item.state) == false){
        states.push(item.state)
      }
    }
    for(var i=0; i<states.length; i++){
      statenames.innerHTML += `<option value="${states[i]}">${states[i]}</option>`
    }
  })
}
function getcica(){
  var url = 'https://api.covid19india.org/resources/resources.json';
  var cities = []
  var services = []
  var statename = document.getElementById('statenames').value
  var citiname = document.getElementById('citynames')
  var categories = document.getElementById('categories')
  fetch(url)
  .then(function(response) {
      return response.json();
    })
    .then(function(myJson) {
      citiname.innerHTML = ``
      categories.innerHTML = ``
      myJson.resources.forEach(myprinter);
      function myprinter(item){
        if(item.state == statename){
          if(cities.includes(item.city) == false){
            cities.push(item.city)
          }
          if(services.includes(item.category) == false){
            services.push(item.category)
          }
        }
      }
      for(var i = 0; i<=cities.length-1; i++){
        citiname.innerHTML += `<option value="${cities[i]}">${cities[i]}</option>`  
      }
      for(var i = 0; i<=services.length-1; i++){
        categories.innerHTML += `<option value="${services[i]}">${services[i]}</option>`  
      }
    })
}

function getser(){
  var url = 'https://api.covid19india.org/resources/resources.json';
  var services = []
  var citiname = document.getElementById('citynames').value
  var categories = document.getElementById('categories')
  fetch(url)
  .then(function(response) {
      return response.json();
    })
    .then(function(myJson) {
      categories.innerHTML = ``
      myJson.resources.forEach(myprinter);
      function myprinter(item){
        if(item.city == citiname){
          if(services.includes(item.category) == false){
            services.push(item.category)
          }
        }
      }
      for(var i = 0; i<=services.length-1; i++){
        categories.innerHTML += `<option value="${services[i]}">${services[i]}</option>`  
      }
    })
}

function getall(){
  var url = 'https://api.covid19india.org/resources/resources.json';
  var statename = document.getElementById('statenames').value 
  var citiname = document.getElementById('citynames').value
  var categories = document.getElementById('categories').value
  var wait = document.getElementById('wait')
  var main = document.getElementById('tabmain')
  wait.style.display = "block"
  main.style.display = "none"
  fetch(url)
  .then(function(response) {
      return response.json();
    })
    .then(function(myJson) {
      document.getElementById('tabres').innerHTML = ``
      myJson.resources.forEach(myprinter);
      wait.style.display = "none"
      main.style.display = "block"
      function myprinter(item){
        if(item.state == statename && item.city == citiname && item.category == categories){
          tabres.innerHTML +=`<tr><td>${item.city}</td><td>${item.category}</td><td>${item.nameoftheorganisation}</td><td>${item.descriptionandorserviceprovided}</td><td>${item.phonenumber}</td></tr>`
        }
      }
    })
}