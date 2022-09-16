// Declarations for our song values
let song;
let playSong;

// Spotify Client Creds
const clientId = 'da1ecb0fa994487ba616a27003e92d29';
const clientSecret = 'b992a6f193e34cc59e608a995f88e8c3';

const _getToken = async () => {
    const result = await fetch('http://accounts.spotify.com/api/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + btoa(clientId + ':' + clientSecret)
        },
        body: 'grant_type=client_credentials'
    });

    // Access the data given to us by the fetch response (Promise)
    const data = await result.json();
    return data.access_token;
}

// FUnction to get song info when image figure is clicked
/**
 * @param img_index
 * @param item_index
 * 
 * Function gets a song from Spotify using the image index of our gallery. Then
 * it finds the correct item_index inside of the JSON response data from Spotify
 * which will produce a preview URL that that will be used to play our selected song.
 */

async function clickedEvent(img_index, item_index){
    // Get track name
    let track = document.getElementsByTagName('img')[img_index].attributes[1].value;

    // Get our token
    let token = await _getToken();

    let headers = new Headers([
        ['Content-Type', 'application/json '],
        ['Accept', 'application/json'],
        ['Authorization', `Bearer ${token}`]
    ]);

    let request = new Request(`http://api.spotify.com/v1/search?q=${track}&type=track&limit=15`, {
        method: 'GET',
        mode: 'no-cors',
        headers: headers
    });

    let result = await fetch(request);

    let response = await result.json();

    console.log(response);
    let song = response.tracks.items[item_index].preview_url;

    // Before we play a song, first check if playSong is True, and if so, stop it
    if (playSong) {
        stopSnippet();
    }

    songSnippet(song);
}

/**
 * @param id
 * @param event 
 * 
 * id = image for gallery image
 * event = Mouse event given by the action from our user
 * 
 * Our function will produce songs from the clickedEvent based on the index of the image
 */

function getSong(id, event){
    switch(id){
        case 'fig1': { // Noticing Icarus
            event.stopPropagation();
            clickedEvent(0,0);
            break;
        }
        case 'fig2': { // Mountain Brews
            event.stopPropagation();
            clickedEvent(1,0);
            break;
        }
        case 'fig3': { // Petey
            event.stopPropagation();
            clickedEvent(2,0);
            break;
        }
        case 'fig4': { // Novo Amor
            event.stopPropagation();
            clickedEvent(3,0);
            break;
        }
        case 'fig5': { // Sufjan
            event.stopPropagation();
            clickedEvent(4,0);
            break;
        }
        case 'fig6': { // Head Hunters
            event.stopPropagation();
            clickedEvent(5,0);
            break;
        }
    }
}

/**
 * @param url
 * 
 * url is the song preview url
 * 
 * function will return an audio clip given by the preview url
 */

function songSnippet(url){
    playSong = new Audio(url);
    return playSong.play();
}

/**
 * NO PARAMS
 * 
 * Function returns an event to stop the song snippet
 */

function stopSnippet() {
    return playSong.pause();
}