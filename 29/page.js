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
    console.log(e.offsetX);
    console.log(e.offsetY);


    ctx.beginPath();
    ctx.strokeStyle = 'blue';
    ctx.rect(e.offsetX, e.offsetY, 100, 150);
    ctx.fillStyle = "red";
    ctx.fill();

}

var drawCircle = function(e){
    /////
    console.log(e.offsetX);
    console.log(e.offsetY);


    ctx.beginPath();
    ctx.strokeStyle = 'blue';
    ctx.arc(e.offsetX, e.offsetY, 50, 0, 2 * Math.PI);
    ctx.fillStyle = "red";
    ctx.fill();

}

var draw = function(e){
    if(mode == "rect"){
        drawRect(e);
    }
    else if(mode == "circ"){
        drawCircle(e);
    }
}

var wipeCanvas = () => {
    ctx.clearRect(0, 0, c.width, c.height);
}

var bToggler = document.getElementById("buttonToggle");
var clearer = document.getElementById("buttonClear");

bToggler.addEventListener('click',toggleMode);
clearer.addEventListener('click',wipeCanvas);
addEventListener('mouseup',draw);