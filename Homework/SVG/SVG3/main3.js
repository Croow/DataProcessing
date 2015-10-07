window.onload = function() {
        var population = loadJSON();
        fillColors(population, colors);
        draw();
        draw_legend(colors);
      }

'use strict'

      // Define a function to load the data
      function loadJSON(){
        var data = document.getElementById('population').value;
        var data_array = JSON.parse(data);
        return data_array;
      };

      // Define a function to fill the countries with colors
      function fillColors(data_array, colors) {
        var population = [0, 2000000, 5000000, 10000000, 15000000, 20000000, 30000000, 40000000, 50000000];

        // Fill the first 8 colors
        for (var i = 0; i < population.length - 1; i++){
          for (var j = 0; j < data_array.length; j++) {
           var country = document.getElementById( data_array[j][0] );
            if (population[i] <= data_array[j][1] && data_array[j][1] <= population[i+1]) {

              // If the country has more than one piece fill all the pieces
              if (country.tagName === 'g'){
                var paths = country.getElementsByTagName('path');
                for (var q = 0; q < paths.length; q++){
                    paths[q].style.fill = colors[i];
                  };

              // If the country has just one piece fill that one piece
              } else {
                country.style.fill = colors[i];
              };
            };
          };
        };

        // Fill the last color
        for (var i = 0; i < data_array.length; i++) {
          var country = document.getElementById( data_array[i][0] );
          if (population[population.length - 1] <= data_array[i][1]) {

            // If the country has more than one piece fill all the pieces
            if (country.tagName === 'g'){
              var paths = country.getElementsByTagName('path');
              for (var j = 0; j < paths.length; j++){
                    paths[j].style.fill = colors[colors.length-1];
                };

            // If the country has just one piece fill that one piece
            } else {
              country.style.fill = colors[colors.length-1];
            };
          };
        };
      };


      // Define a function to draw the legend
      function draw_legend(colors) {
        // Find the canvas elements
        var canvas = document.getElementById('canvas');
        var width = document.getElementById('canvas').getAttribute("width");
        var borders = ["< 2000000", "2000000 - 5000000", "5000000 - 10000000", "10000000 - 15000000", "15000000 - 20000000", "20000000 - 30000000", "30000000 - 40000000", "40000000 - 5000000", "> 5000000"];
        if (canvas.getContext){
          var context = canvas.getContext('2d');
  
          // Draw the outlining
          context.beginPath();
          context.moveTo(width - 400, 170);
          context.lineTo(width - 150, 170);
          context.lineTo(width - 150, 520);
          context.lineTo(width - 400, 520);
          context.lineTo(width - 400, 170);
          context.stroke()

          // Draw the lines
          for (var i = 0; i < colors.length; i++){
            context.beginPath();
            context.moveTo(width - 380, i * 35 + 205);
            context.lineTo(width - 340, i * 35 + 205);
            context.lineWidth = 8;
            context.strokeStyle = colors[i];
            context.stroke()
          };
          
          // Draw the text
          for (var i = 0; i < borders.length; i++){
            context.font = "16px serif";
            context.fillText(borders[i], width - 335, i * 35 + 210);
          };
        };
      };

      // Define a function to write the needed text
      function draw() {
        var ctx = document.getElementById('canvas').getContext('2d');
        ctx.font = "12px serif";
        ctx.fillText("Type of color: #FFFFFF (white) and #000000 (black) mixed", 10, 50);
        ctx.fillText("Dark for high population, light for low population", 10, 62);
        ctx.fillText("The opponent-process theory suggests that the colors black, white, red, green,", 10, 80)
        ctx.fillText("yellow, and blue are special.From these colors black and white are the best options", 10, 92)
        ctx.fillText("because the luminance channel has much greater capacity to convey detailed", 10, 104)
        ctx.fillText("information than the chromatic channels. Thepatterns show that we can still see", 10, 116)
        ctx.fillText("large shapes represented chromatically, but the fine pattern is much harder to", 10, 128)
        ctx.fillText("see expressed through chromatic differencesthan when expressed through black-white differences.", 10, 140)
      };


      // Define the needed variables
      var colors = ['#F2F2F2', '#D9D9D9', '#BFBFBF', '#A6A6A6', '#8C8C8C', '#737373', '#595959', '#595959', '#262626'];
      