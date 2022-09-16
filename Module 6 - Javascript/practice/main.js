// Switch case

let day = new Date().getDay();
let literal_day = new Date().toString();

console.log(day);
console.log(literal_day);


// Switch case Statement Syntax
switch(day){
    case 0:
        console.log('Go to church');
        break;
    case 1:
        console.log('It is Monday');
        break;
    case 2:
        console.log('It is Tuesday');
        break;
    case 3:
        console.log('It is Wednesday');
        break;
    case 4:
        console.log('It is Thursday');
        break;
    case 5:
        console.log('It is Friday');
        break;
    case 6:
        console.log('It is Saturday');
        break;
    default:
        console.log("We don't have a case for that")
        break;
}

// Creation of Objects in Javascript
// A simple JS Object

let person = {
    name: 'John',
    age: 28,
    fav_color: 'Red'
}

// Accessing data in our object
console.log(person['name']);  // Bracket notation
console.log(person.age);      // Dot notation

// Complex JS Object
let person2 = {
    name: 'Max',
    age: 31,
    prog_languages: ['JavaScript', 'Python', 'C++', 'Java'],
    fav_color: 'Blue',
    teams: [
        {
            baseball: 'Chicago White Sox',
            football: 'Chicago Bears',
            hockey: 'Chicago Blackhawks',
            basketball: ['Chicago Bulls', 'Chicago Sky'],
            soccer: ['Chicago Fire', 'Naperville Yellowjackets']
        },
        {
            baseball: 'Toronto Bluejays',
            football: 'LA Rams',
            basketball: 'Milwaukee Bucks',
            soccer: ['Manchester United', 'Liverpool']
        }
    ]
}

console.log(person2.prog_languages[2]);
console.log(person2['prog_languages'][2][0]);
console.log(person2.teams[1].soccer[0]);

// JS Object Prototype Methods -- Object Literal
console.log(Object.keys(person2));
console.log(Object.values(person2));

// Sad Path of looping through objects in JS
for(let i = 0; i < person.length; i++) {
    console.log(person2[i]);
}

// Happy path of looping through object in JS -- looking for keys
for(let i = 0; i < Object.keys(person2).length; i++) {
    console.log(Object.keys(person2)[i]);
}

// List Values from the person2 Object that are arrays
for(let i = 0; i < Object.keys(person2).length; i++) {
    if(Array.isArray(Object.values(person2)[i])) {
        console.log(Object.values(person2)[i]);
    }
}



// Create our own Object prototypes -- using ES5 method syntax
function Car(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;

    // A method inside of a JS Prototype
    this.printInfo = function(wheels = 0, color){
        console.log(`This is a ${this.year}, ${this.make}, ${this.model} and has ${wheels} and the color is ${color}`);

        return 'Returned value'
    }
}

// Created an instance of a prototype
let my_car = new Car('Honda', 'CR-V', 2019);

// Call the prototype method
console.log(my_car.printInfo(4, 'Gun Metal'));

// JS Classes
class Human{
    constructor(name, age, gender) {
        this.age = age;
        this.name = name;
        this.gender = gender;
    }

    printInfo(){
        return `Name: ${this.name} \n Age: ${this.age} \n Gender: ${this.gender}`;
    }
}

let wilma = new Human('Wilma', 25, 'Female');

// Use printInfo from the newly instantiated wilma (Human) class
console.log(wilma.printInfo());

// JS inheritance using Classes
class Baby extends Human{
    constructor(name, age, gender, walking) {
        super(name, age, gender);
        this.walking = walking;
    }
    
    isBabyWalking() {
        if(this.walking == true) {
            return 'Baby is walking';
        } else {
            return 'Baby is not walking yet';
        }
    }
}

// Create an instantiated value for baby
let caleb = new Baby('Caleb', 1, 'Male', true);
console.log(caleb.printInfo());
console.log(caleb.isBabyWalking());


// JS Closures

// A closure is a self-invoking function that only runs once
// One of the most important parts is that it has private data inside of it

// Closures are also a variable data type


let newAdd = function(outer_var){
    let innerAdd = function(inner_var) {
        return outer_var + inner_var;
    };

    return innerAdd;
};

let addFive = new newAdd(5);
let addSix = new newAdd(6);

console.log(addFive(3));
console.dir(addFive);

let countUp = ( function() {
    let counter = 0; // This will be our private variable
    console.log('Hit');
    return function() { return counter ++}
}) ();

console.log(countUp());
console.log(countUp());
console.log(countUp());
console.dir(countUp);
console.log(countUp());

let addNames = ( function () {
    let names = [];
    console.log('Adding names');
    return function (name) {
        console.log(names);
        return names.push(name);
    }
}) ();

console.log(addNames('Adam'));
console.log(addNames('Jenifer'));
console.dir(addNames);
console.log(addNames('Levi'));
console.log(addNames('Annabelle'));
console.log(addNames('Easton'));



// Async JS Section //
// -- JS Callbacks -- //

/* 
    Simply put: A Callback is a function that is to be executed after another
    function has finished its execution - hence the name callback.

    More Complex Definition: In JS, functions are objects. Because of this,
    functions can take other functions as arguments(parameters), and can return functions
    by other functions.

    Functions that do this are called "higher - Order functions". Any function,
    that is passed as an argument is called a "Callback function".

    Sooooo... why do we need them?

    The reason for this is, because of the JS Event Loop. In a nutshell
    JS is an event driven language so this means, that instead of waiting for
    a response before moving on, JS will keep executing while listening for other events.
*/

// Basic example

function first(){
    console.log(1);
}

function section() {
    console.log(2);
}

first();
section();

// But what if we delay the execution?

function firstDelayed() {
    // Simulate the delay
    setTimeout(function() {
        console.log(1);
    }, 5000);
}

function secondDelayed() {
    console.log(2);
}

firstDelayed();
secondDelayed();

// Callback function syntax
function doHomework(subject, callback) {
    alert(`Starting my ${subject} homework`);
    callback();
}

// doHomework('Javascript', function () {
//     console.log('Done with homework');
// });


/* 
    Though Callbacks give us more functionality... they also introduce
    their own problem: Callback Hell

    Somthing that looks like this:
    function1( () => {
        function2( () => {
            function3 ( () => {
                function4( () => {
                    // Maybe do something here...
                })
            })
        })
    })
*/

// JS promises
const isEvenNumber = (num) => {
    return new Promise( (resolve, reject) => {
        if(num % 2 == 0) {
            resolve(true);
        } else{
            reject(false);
        }
    })
}

// Using the JS Promise
isEvenNumber(10)
// Happy path (resolve)
.then( (result) => {
    console.log(`Even number: ${result}`)
})
// Sad rejected path
.catch( (error) => {
    console.log(`Odd number: ${error}`)
});

console.dir(isEvenNumber());

// Another example with promises - using Async/Await
function increaseSalary(base, increase) {
    const new_salary = base + increase;
    console.log(`New Salary: ${new_salary}`);
    return new_salary;
}

// Write a function to add to the base salary slowly
function slowAddition(n1, n2) {
    return new Promise( (resolve) => {
        setTimeout( () => resolve(n1 + n2), 2000);
    });
}

function increaseSlowSalary(base, increase) {
    const newSalary = slowAddition(base, increase);
    console.log(`New Salary: ${newSalary}`);
    return newSalary;
}

async function asyncIncreaseSalary(base, increase) {
    const newSalary = await slowAddition(base, increase);
    console.log(`The new salary is: ${newSalary}`);
    return newSalary;
}

asyncIncreaseSalary(50000, 5000);