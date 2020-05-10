function getstates(){
var url = 'https://api.covid19india.org/zones.json';
var states = []
var statenames = document.getElementById('statenames')
fetch(url)
.then(function(response){
    return response.json();
})
.then(function(myJson){
    statenames.innerHTML = `<option value="ALL">All States</option>`
    myJson.zones.forEach(myprinter);
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
function getcity(){
var url = 'https://api.covid19india.org/zones.json';
var cities = []
var cities2 = []
var statename = document.getElementById('statenames').value
var citiname = document.getElementById('citynames')
fetch(url)
.then(function(response) {
    return response.json();
    })
    .then(function(myJson) {
    citiname.innerHTML = `<option value="ALL">All Districts</option>`
    myJson.zones.forEach(myprinter);
    function myprinter(item){
        if(cities2.includes(item.district) == false){
            cities2.push(item.district)
        }
        
        if(item.state == statename){
        if(cities.includes(item.district) == false){
            cities.push(item.district)
        }
        }
    }
    for(var i = 0; i<=cities.length-1; i++){
        citiname.innerHTML += `<option value="${cities[i]}">${cities[i]}</option>`  
    }
    })
    console.log(cities2)
}
function getzones(){
var url = 'https://api.covid19india.org/zones.json';
var statename = document.getElementById('statenames').value 
var citiname = document.getElementById('citynames').value
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
    myJson.zones.forEach(myprinter);
    wait.style.display = "none"
    main.style.display = "block"
    var zone = ''
    function myprinter(item){
        if(statename == "ALL"){
            if(item.zone == "Red"){
                zone = `<td style="font-weight:700;color: red">${item.zone}</td>`
            }
            else if(item.zone == "Orange"){
                zone = `<td style="font-weight:700;color: #FFA500">${item.zone}</td>`
            }
            else{
                zone = `<td style="font-weight:700;color: green">${item.zone}</td>`
            }
            tabres.innerHTML +=`<tr><td>${item.state}</td><td>${item.district}</td>${zone}<td class="source"><a href='${item.source}'>${item.source}</a></td><td class="lup">${item.lastupdated}</td></tr>`
        }
        if(item.state == statename && item.district == citiname){
            if(item.zone == "Red"){
                zone = `<td style="font-weight:700;color: red">${item.zone}</td>`
            }
            else if(item.zone == "Orange"){
                zone = `<td style="font-weight:700;color: #FFA500">${item.zone}</td>`
            }
            else{
                zone = `<td style="font-weight:700;color: green">${item.zone}</td>`
            }
            tabres.innerHTML +=`<tr><td>${item.state}</td><td>${item.district}</td>${zone}<td class="source"><a href='${item.source}'>${item.source}</a></td><td class="lup">${item.lastupdated}</td></tr>`
        }
        if(citiname == "ALL"){
            if(item.state == statename){
                if(item.zone == "Red"){
                    zone = `<td style="font-weight:700;color: red">${item.zone}</td>`
                }
                else if(item.zone == "Orange"){
                    zone = `<td style="font-weight:700;color: #FFA500">${item.zone}</td>`
                }
                else{
                    zone = `<td style="font-weight:700; color: green">${item.zone}</td>`
                }
                tabres.innerHTML +=`<tr><td>${item.state}</td><td>${item.district}</td>${zone}<td class="source"><a href='${item.source}'>${item.source}</a></td><td class="lup">${item.lastupdated}</td></tr>`	
            }
        }
        
    }
    })
}