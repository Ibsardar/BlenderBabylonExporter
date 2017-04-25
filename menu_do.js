/* ================================= *
 * By:              Ibrahim Sardar   *
 * Filename:        "do.js"          *
 * Date Created:    4/18/2017        *
 * ================================= */



// returns false if browser does not support local storage
function checkLocalStorage() {
    if(typeof(Storage) === 'undefined'){
        alert("\n\n\nYour browser does not support local storage.\nPlease try a different browser.\n\n\n");
        console.log("Browser does not support local storage.");
        return false;
    }
    return true;
}

// set local storage
function setLocalStorage(storageVar,objVar) {
    localStorage.setItem(storageVar, JSON.stringify(objVar));
}

// get local storage
function getLocalStorage(storageVar) {
    return JSON.parse(localStorage.getItem(storageVar));
}

// redirect to webpage
function goto(url="") {
    window.location.assign(url);
}

// saves all notes to local storage
function save(obj='') {
    if(!checkLocalStorage()) {
		return;
	}
    var note_list = [];
    switch(obj) {
        case '':
            return;
        case 'note':
            var containers = document.getElementsByClassName('note-container');
            var i=0;
            var n=containers.length;
            for (i=0; i<n; i++) {
                var title = containers[i].getElementsByClassName('note-title')[0].textContent;
                var text  = containers[i].getElementsByClassName('note')[0].textContent;
                var note = {'title' : title, 'text' : text};
                note_list.push(note);
            }
            break;
        default:
            return;
    }
    setLocalStorage('iboard_saved_notes', note_list);
}

// #########TODO#########
function load(obj='') {
    if(!checkLocalStorage()) {
		return;
	}
    switch(obj) {
        case '':
            return;
        case 'notes':
            // #########TODO#########
            break;
        default:
            return;
    }
}

// allign's the notes depending on input
function align(type='center') {
    document.getElementsByClassName('notes-container')[0].style.textAlign = type;
}

// adds to document
function add(obj='') {
    switch(obj) {
        case '':
            return;
        case 'note':
            container = document.getElementsByClassName('notes-container')[0];
            var note = document.createElement("SPAN");
            var title = document.createElement("TEXTAREA");
            var pad = document.createElement("DIV");
            var text = document.createElement("TEXTAREA");
            note.className    = "note-container";
            title.className   = "note-title";
            title.placeholder = "<Title Here>";
            pad.className     = "vpad1";
            text.className    = "note";
            text.placeholder  = "<Text Here>";
            note.appendChild(title);
            note.appendChild(pad);
            note.appendChild(text);
            container.appendChild(note);
            break;
        default:
            return;
    }
}

// clears value
function clr(obj='',focus=null) {
    switch(obj) {
        case '':
            return;
        case 'note':
            if (focus.className == "note-container") {
                focus.getElementsByClassName('note-title')[0].value = '';
                focus.getElementsByClassName('note')[0].value = '';
            }
            break;
        default:
            return;
    }
}

// removes from document
function del(obj='',focus=null) {
    switch(obj) {
        case '':
            return;
        case 'note':
            if (focus.className == "note-container") {
                focus.parentElement.removeChild(focus);
            }
            break;
        default:
            return;
    }
}
