//rerieve node in DOM via ID
var c = document.getElementById("slate");
console.log(c);
//instantiate a CanvassRenderingContext2D object
var ctx = c.getContext("2d");
console.log(ctx)
//init global state variable
var mode = "rect";

var toggleMode = (e) => {
    console.log("original mode: " + mode);
    if(mode == "rect"){
        mode = "circ"
    }
    else if (mode == "circ"){
        mode = "rect";
    }
    else{
        console.log("houston, we've got a problem");
    }

}

var drawRect = function(e){
    /////
}

var drawCircle = function(e){
    //////
}

var draw = function(e){
    ///////
}

var wipeCanvas = () => {
    /////
}

c.addEventListener('click',draw);
var bToggler
