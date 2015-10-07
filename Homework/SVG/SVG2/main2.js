window.onload = function() {
        changeColor("it", '#00FF00');
        changeColor("es", "#00FF00");
        changeColor("no", "#00FF00");

      }

function changeColor(id, color) {
    var country = document.getElementById( id );
    if (country.tagName === 'g'){
        var paths = country.getElementsByTagName('path');
        for (var i = 0; i < paths.length; i++){
          paths[i].style.fill = color
          };
    } else {
        country.style.fill = color
    }
}