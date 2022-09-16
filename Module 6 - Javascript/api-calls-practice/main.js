// Get our ranger data
const getData = async () => {
    let response = await axios.get("https://my-json-server.typicode.com/CodingTemple/Power-Rangers-API-Json/rangers");
    console.log(response.data);
    return response.data;
}

// Create constants to hold DOM elements
const DOMElements = {
    rangerList : '.ranger-list'
}

// Create the Rnager List HTML
const createList = ( id, name ) => {
    const html = `<a href="#" class="list-group-item list-group-item-action list-group-item-light" id="${id}"> ${name} </a>`;
    document.querySelector(DOMElements.rangerList).insertAdjacentHTML('beforeend', html);
}

// Functions to load data and display the HTML
const loadData = async () => {
    const rangers = await getData();

    rangers.forEach( element => createList(element.id, element.name));
}

const clearData = () => {
    document.querySelector(DOMElements.rangerList).innerHTML = '';
}