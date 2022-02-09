// Team Oranges :: Ishraq Mahid, Julia Nelson 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-J in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };

//adds item to the tlist
var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

//removes the item at index n
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  //weird way of defining a remove method   
  listitems[n].remove();
};

//turns the color of the last item in the list to red
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

//stripes the items that do not already have a color
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

var fibby = function() {
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
        items[i].innerText = fib(i);
    }
  
};

var facty = function() {
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
        items[i].innerText = fact(i);
    }
  
};

//insert your implementations here for...
// FIB
var fib = (n) => {
	if(n<=1){
              return n
	}
	
	else{
              return (fib(n-1) + fib(n-2))
	}
};


// FAC
var fact = (n) => {
	if(n<=1){
		return 1
	}
	
	else{
		return n * fact(n-1)
	}

}

// GCD
