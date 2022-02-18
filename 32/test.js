//rerieve node in DOM via ID
var c = document.getElementById("slate");
console.log(c);

let move = document.getElementById("buttonMove");
let stop = document.getElementById("buttonStop");

//instantiate a CanvassRenderingContext2D object
var ctx = c.getContext("2d");
ctx.fillStyle = "blue";
ctx.strokeStyle = "blue";


console.log(ctx)
//init global state variable
let frame = 0;
let direction = 1;
let formerDirection = 1;

//https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Basic_animations

let draw = () => {
    drawCircle()

    window.requestAnimationFrame(draw)
}

let drawCircle = () => {
    ctx.clearRect(0, 0, c.width, c.height);
    ctx.beginPath();
    ctx.strokeStyle = 'blue';
    if (frame > c.width / 2 || frame < 0) {
        direction *= -1;
        if (frame < 0) {
            frame *= -1;
        }
    }
    console.log(frame);
    let rgb = [0, 0, 0];


    let total = c.width;
    let scaleValue = frame;

    if (direction < 0) {
        scaleValue = c.width - scaleValue;
    }
    console.log("Scalevalue = " + scaleValue);
    console.log("Index = " + Math.floor(scaleValue / (total / 3)));
    console.log("Width " + c.width);
    rgb[Math.floor(scaleValue / (total / 3))] = (scaleValue % total) / (total / 3) * 255;

    ctx.arc(c.width / 2, c.height / 2, frame, 0, 2 * Math.PI);

    ctx.fillStyle = `rgb(${rgb[0]},${rgb[1]},${rgb[2]})`;
    ctx.fill();
    frame += 1 * direction;
    if (direction != 0) {
        formerDirection = direction;
    }
}

let pause = () => {
    direction = 0;
}

let unpause = () => {
    direction = formerDirection;
}

let leMove = () => {
    if (direction != 0) {
        direction *= 1.01;
    }
    else {
        unpause();
    }
}

move.addEventListener('click', leMove);
stop.addEventListener('click', pause);
//draw();

var img = new Image();   // Create new img element
img.src = 'orang.png';
var requestID;

let x = 0;
let y = 0;
let vx = 5;
let vy = 5;


let drawDVD = () => {
    ctx.clearRect(0,0,c.width,c.height);
    ctx.drawImage(img, x, y, 120, 50);
    x += vx;
    y += vy;
    if(x < 0 || x > c.width-120 ){
        vx *= -1;
    }
    if (y < 0|| y > c.height-50){
        vy *= -1;
    }
    //window.cancelAnimationFrame(requestID);
    window.requestAnimationFrame(drawDVD);
}
img.onload = function () {
    drawDVD();
};
