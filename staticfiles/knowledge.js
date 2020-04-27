function disclaimer() {
  var x = document.getElementById("dd");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

var wait = document.getElementById('wait')
var notfoundre =  document.getElementById('notfoundre')

function getme(){
	document.getElementById('tabres').innerHTML = ""  
  wait.style.display = "block"
	var url = 'https://api.covid19india.org/resources/resources.json';
  	fetch(url)
    .then(function(response) {
      return response.json();
    })
    .then(function(myJson) {
      myJson.resources.forEach(myprinter);
      wait.style.display = "none"
      notfoundre.style.display = "none"
      document.getElementById("tabmain").style.display = "block"
      function myprinter(item){
      	var stinp = document.getElementById('sts').value
      	var ciinp1 = document.getElementById('state').value
        var ciinp = ciinp1.trim()
	      var catinp = document.getElementById('service').value
	      var tabres = document.getElementById('tabres')
        if(stinp == ""){
          stinp = "ALL"
        }
        if(ciinp == ""){
          ciinp = "ALL"
        }
        if(catinp == ""){
          catinp = "ALL"
        }
        if(stinp == "ALL" && ciinp == "ALL" && catinp != "ALL"){
          if(item.state == stinp && item.category == catinp ){
            tabres.innerHTML +=`<tr><td>${item.city}</td><td>${item.category}</td><td class="org">${item.nameoftheorganisation}</td><td class="des">${item.descriptionandorserviceprovided}</td><td>${item.phonenumber}</td></tr>`
          }else{
            tabres.innerHTML =`<h1>No Results</h1>`
          }          
        }else if(stinp == "ALL" && ciinp != "ALL" && catinp != "ALL"){
          if(item.state == stinp && item.city == ciinp && item.category == catinp ){
            tabres.innerHTML +=`<tr><td>${item.city}</td><td>${item.category}</td><td class="org">${item.nameoftheorganisation}</td><td class="des">${item.descriptionandorserviceprovided}</td><td>${item.phonenumber}</td></tr>`
          }else{
            tabres.innerHTML =`<h1>No Results</h1>`
          }
        }
        if(stinp !="ALL"){
         if(ciinp == "ALL" && catinp == "ALL" ){
            if (item.state == stinp){
              tabres.innerHTML +=`<tr><td>${item.city}</td><td>${item.category}</td><td class="org">${item.nameoftheorganisation}</td><td class="des">${item.descriptionandorserviceprovided}</td><td>${item.phonenumber}</td></tr>`
            }
          }else if(ciinp !="ALL" && catinp == "ALL"){
            if(ciinp != item.city){
              document.getElementById("tabmain").style.display = "none"
              notfoundre = "block"
              return
            }else{
              if(item.city == ciinp){
                tabres.innerHTML +=`<tr><td>${item.city}</td><td>${item.category}</td><td class="org">${item.nameoftheorganisation}</td><td class="des">${item.descriptionandorserviceprovided}</td><td>${item.phonenumber}</td></tr>`
              }
            }
          }else if(ciinp !="ALL" && catinp != "ALL"){
            if(item.city == ciinp){
              if(item.category == catinp){
                tabres.innerHTML +=`<tr><td>${item.city}</td><td>${item.category}</td><td class="org">${item.nameoftheorganisation}</td><td class="des">${item.descriptionandorserviceprovided}</td><td>${item.phonenumber}</td></tr>`
              }
            }else{
              tabres.innerHTML = `<h1>NO RESULTS</h1>`
            }
          }else if(ciinp == "ALL" && catinp != "ALL"){
            if(item.category == catinp){
              if(item.state == stinp && item.category == catinp){
                tabres.innerHTML +=`<tr><td>${item.city}</td><td>${item.category}</td><td class="org">${item.nameoftheorganisation}</td><td class="des">${item.descriptionandorserviceprovided}</td><td>${item.phonenumber}</td></tr>`
              }
            }else{
              document.getElementById("tabmain").style.display = "none"
              document.getElementById('notfoundre').style.display = "block"
            }
            
          }
        }
      	
      }
    
  });
}