console.log(document.getElementsByTagName('h1')[0].innerHTML = "new text");

let colorButton = document.getElementById("colorButton");
let headerNotAButton = document.getElementsByTagName("h1")[0];
console.log(colorButton);

function colorChange() {
    let headerText = document.getElementsByTagName("h1")[0].innerHTML;
    if(headerText == "new text"){
        document.getElementsByTagName("h1")[0].className = 'colorChange';
    } else {
        headerText = "something else";
    }
}

// Change the text color via click even listener in JS
colorButton.addEventListener('click', colorChange);

// Adding a new button in JS
let button = document.createElement('button');
let buttonDisplay = document.createElement("h2");
// Add inner text to button
button.innerHTML = 'I am alive!';
document.body.append(button);

button.addEventListener('click', function() {
    buttonDisplay.innerHTML = "More JS info here...";
    document.body.append(buttonDisplay);
})

// Grab copied text -- then place into a clipboard
const source = document.querySelector('div.source');
source.addEventListener('copy', ( event ) => {
    console.log(ClipboardEvent);
    const selection = document.getSelection();
    event.clipboardData.setData('text/plain', selection.toString().toUpperCase());
    event.preventDefault();
})

// Grabbing Form Data from a Submit event
const form = document.querySelector("#testDataForm");

// Add event listener for submit event
form.addEventListener('submit', ( event ) => {
    event.preventDefault();
    let queryFirst = document.querySelector('#firstName');
    let queryLast = document.querySelector('#lastName');
    let firstName = event.path[0][0].value;
    let lastName = event.path[0][1].value;
    console.log(event);
    console.log(firstName, lastName);
    console.log(`This came from the query selector: ${queryFirst.value}, ${queryLast.value}`);
    document.body.append(firstName, lastName);
})