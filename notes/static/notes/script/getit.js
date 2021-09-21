function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

//Extrair cookies para csrf  - https://docs.djangoproject.com/en/3.2/ref/csrf/
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');


function editNote(id) {
  document.getElementById('hidden-id').value = id;
  document.querySelector('.curtain').style.display ='flex';
}


//https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_forms_through_JavaScript
function deleteNote(id) {
  document.getElementById('delete-note-'+id).submit();

  /*
  const form = document.getElementById('delete-note-'+id);
  const XHR = new XMLHttpRequest();

  // Bind the FormData object and the form element
  const FD = new FormData( form );

  // Set up our request
  XHR.open("POST", "delete");
  XHR.setRequestHeader('X-CSRF-TOKEN', csrftoken);

  // The data sent is what the user provided in the form
  XHR.send( FD );
 */
}



document.querySelector(".exit").addEventListener('click',
  function(){
    document.querySelector('.curtain').style.display ='none'
  })


document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
});
