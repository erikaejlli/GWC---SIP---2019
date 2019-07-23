// console.log("Hello World");
//
// var h1tag = document.getElementsByTagName("h1")[0];
//
// var loc = document.getElementsByClassName("headings")[3];

var adjectives = ["EXO" , "ATEEZ" , "TWICE" , "LOONA" , "NCT" , "STRAY KIDS" , "GOT7"];
var pos = 0;
var loc = document.getElementById("adjective");

function changeAdj(){
  loc.innerHTML = adjectives[pos];
  pos ++;
  if (pos >= adjectives.length){
    pos = 0;
  }
}

// Math.random()
var x = document.getElementsByTagName("body")[0]

function colorfulBackground(){
  x.setAttribute("style", `background-color:rgb(${Math.floor(Math.random()*256)},${Math.floor(Math.random()*256)},${Math.floor(Math.random()*256)})`)

}

// x.setAttribute("onmousehover", colorfulBackground());

var listOfFonts = ["'Jacques Francois Shadow', cursive;" , "'Barriecito', cursive;" , "'Snowburst One', cursive;"];
var pos2 = 0;

var loc2 = document.getElementById("wordBio");

function changeFont(){
  // console.log("work")
  pos2 ++;
  if (pos2 >= listOfFonts.length){
    pos2 = 0;
  }
  loc2.setAttribute("style", `font-family:${listOfFonts[pos2]}`)
}
