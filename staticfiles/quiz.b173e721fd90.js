var no_repeat = []
var points = 0
var question = document.getElementById('question')
var answer = document.getElementById('answer')
var detail = document.getElementById("detail")
var success = document.getElementById("success")
var failed = document.getElementById("failed")
var y = document.getElementById("f-option")
var n = document.getElementById("s-option")
function togglesq() {
    var x = document.getElementById("sq");
    if (x.style.display === "none") {
        document.getElementById('chevron').innerHTML=`<i class="fas fa-chevron-down"></i>`
        x.style.display = "block";
    } else {
        document.getElementById('chevron').innerHTML=`<i class="fas fa-chevron-up"></i>`
        x.style.display = "none";
    }
}
function gn(){
    document.getElementById('startscreen').innerHTML = `
    <h1 class="primary-text">THAT'S ALRIGHT!</h1>
    <br>
    <h4 class="secondary-text">Just refresh the page when you are ready!</h4>
    <br>
    <i class="fas fa-refresh fa-3x text-center hvr-pulse"></i>
    `
    document.getElementById('startscreen').style.display = "block"
    detail.style.display = "none"
    document.getElementById('gamescreen').style.display = "none"
    document.getElementById('results').style.display = "none"

    
}
function hideme(){
    document.getElementById("startscreen").style.display = "none"
}
function checkans(ans){
    y.disabled = true;
    n.disabled = true;
    var url = 'https://raw.githubusercontent.com/tinshade/anticovid/master/main/static/quiz.json';
    fetch(url)
    .then(function(response){
    return response.json();
    })
    .then(function(myJson){
        console.log(no_repeat[no_repeat.length-1])
        if(myJson[no_repeat[no_repeat.length-1]].o == ans){
            failed.style.display = "none"
            success.style.display = "block"
            detail.className += "bgsuccess"
            detail.style.display = "block"
            points = points + 1
        }else{
            success.style.display = "none"
            failed.style.display = "block"
            detail.className += "bgfail"
            detail.style.display = "block"
        }
    })
}
function getqs(){
    y.disabled = false
    y.checked = false
    n.disabled = false
    n.checked = false
    document.getElementById('gamescreen').scrollIntoView(true);
    detail.style.display = "none"
    document.getElementById('gamescreen').style.display = "block"
    var url = 'https://raw.githubusercontent.com/tinshade/anticovid/master/main/static/quiz.json';
    fetch(url)
    .then(function(response){
    return response.json();
    })
    .then(function(myJson){
        var random = Math.floor(Math.random() * 11) + 1;
        if(no_repeat.length != 5){
            if(no_repeat.includes(random) == false){
                no_repeat.push(random)
                var data = myJson[random]
                question.innerHTML = data.q
                answer.innerHTML = data.a
                
            }else{
                getqs()
            }
        }else{
            detail.style.display = "none"
            document.getElementById('gamescreen').style.display = "none"
            document.getElementById('results').style.display = "block"
            document.getElementById('score').innerHTML = points
        }			
    });
}
    	