function events_clickable() {
    let modal = document.getElementById('modal');
    let events = document.getElementsByClassName('event');

    for (let i = 0; i < events.length; i++) {
        events[i].onclick = function(){
            // stuff
            modal.style.display = "block";

            document.getElementById('event-info').innerHTML = events[i].innerHTML;
            document.getElementById('event-info').querySelectorAll('.hide').forEach((node) => {
                node.classList.remove('hide');
            });
        }
    }
}

function hideSearch() {
    let form = document.getElementById('main-form');
    let hideButton = document.getElementById('hide-button');
    let showButton = document.getElementById('show-button');
    
    form.style.display = 'none';
    hideButton.style.display = 'none';
    showButton.style.display = 'block';
}

function showSearch() {
    let form = document.getElementById('main-form');
    let hideButton = document.getElementById('hide-button');
    let showButton = document.getElementById('show-button');
    
    form.style.display = 'block';
    hideButton.style.display = 'block';
    showButton.style.display = 'none';
}

function hideModal() {
    var modal = document.getElementById("modal");

    // Get the events
    var events = document.getElementsByClassName("event");
    
    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];
    
    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
      modal.style.display = "none";
    }
    
    // When the user clicks on the modal itself, close the modal
    modal.onclick = function() {
        modal.style.display = "none";
    }

    window.addEventListener("keydown", function(e) {
        if (e.key === 'Escape') {
            modal.style.display = "none";
        }
    });

    modal.style.display = "none";
}

function showModal() {
    var modal = document.getElementById("modal");

    modal.style.display = "block";
}

function quickSearch(query) {
    if (!query) {
        query = document.getElementById("event-search").value ?? '';
    }

    let input, filter, events, h, text, others, otherText, show, hits = 0;
    input = query
    filter = input.toUpperCase();
    events = document.querySelectorAll('.event');

    for (const i in events) {
        show = false;
        h = events[i].querySelector('h2');
        others = events[i].querySelectorAll('p');

        text = h.textContent || h.innerText;
        if (text.toUpperCase().indexOf(filter) > -1) {
            show = true;
        }

        for (let j = 0; j < 3; j++) {
            otherText = others[j].textContent || others[j].innerText;
            if (otherText.toUpperCase().indexOf(filter) > -1) {
                show = true;
            }
        }

        if (show) {
            events[i].style.display = "";
            hits++;
        }
        else {
            events[i].style.display = "none";
        }
    }
}

function clearFields() {
    let events = document.getElementsByClassName('event');

    let event_search = document.getElementById('event-search');
    event_search.value = '';

    for (const i in events) {
        events[i].style.display = 'block';
    }
}