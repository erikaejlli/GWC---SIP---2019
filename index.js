console.log("Hello world")

//sets i to 0 then adds 2 each time till 20
var i = 0;
for(i = 0; i <= 20; i += 2){
  console.log(i);
}

i = 0
while(i <= 20){
  console.log(i)
  i =+ 2;
}

i = 0
while(i <= 20){
  if(i % 2 == 0){
    console.log(i);
  }
  i += 1;
}

function getTemp(){
  return 22.5;
}


var temperature = getTemp2();
console.log(temperature);

funtions getTemp2(type){
  if (type == "c"){
    alert("omg whatttt");
    return 22.5;
  }
  if (type == "f"){
    alert("oh nooooo");
    return 100;
  }
}

console.log(getTemp2("f"))
console.log(getTemp2("c"))
