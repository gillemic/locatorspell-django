function events_clickable() {
    let modal = document.getElementById('modal');
    let events = document.getElementsByClassName('event');

    for (let i = 0; i < events.length; i++) {
        events[i].onclick = function(){
            // stuff
        }
    }
}