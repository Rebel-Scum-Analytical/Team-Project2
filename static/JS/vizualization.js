const personal_data = user_personal_data;
const nutrition_data = userdata_nutrition_data;
const BAR = "plot";
const selectNutrient = d3.select("#selectnutrients");

user_age_key = calculateAge(user_personal_data.date_of_birth);
user_calory_needs = calculateCalories(user_personal_data);
user_gender = user_personal_data.gender;


const inputField = d3.select("#datetime");
desired_date = inputField.value;
console.log(desired_date)
inputField.on("change", function() {
  desired_date =  d3.event.target.value;
  filtered_data = data.filter(function(e) {
    return e.datetime === d3.event.target.value;
  });
});

let distinctnutrients = ['Calories', 'Macro Nutrients', 'Micro Nutrients', 'All'];

var options = selectNutrient
  .selectAll('option')
	.data(distinctnutrients).enter()
	.append('option')
  .text(function (d) { return d; });
  
  // Initialize the dropdown menu
  (function() {
    desired_nutrient = document.getElementById('selectnutrients').value = 'Calories';
  })();

(function(){
      d3.select("#plot").html("")
      let plot_data = plot_calories()
      plot_data.layout.height = 700;
      plot_data.layout.width = 1200;  
      Plotly.newPlot(BAR, plot_data.data, plot_data.layout)


      selectNutrient.on( 'change', function () {
        let desired_nutrient = selectNutrient.property("value");
        d3.select("#plot").html("")

        if( desired_nutrient == 'All')
        {
          let row1 = d3.select("#plot")
                      .html("")
                     .append("div")
                     .classed("row justify-content-center", true)

          let col1 = row1.append("div")
                      .classed("col-md-6", true)
                      .attr("id", "plot1")
                    
          let col2 = row1.append("div")
                     .classed("col-md-6", true)
                     .attr("id", "plot2")

                     d3.select("#plot")
                    .append("br")
                    .append("br")

          let row2 = d3.select("#plot")
                    .append("div")
                    .classed("row justify-content-center", true)
                    .attr("id", "plot3")

          let plot_data = plot_macro()
          plot_data.layout.height = 700/2;
          plot_data.layout.width = 1200/2; 
          Plotly.newPlot("plot1", plot_data.data, plot_data.layout)   
          
          plot_data = plot_micro()
          plot_data.layout.height = 700/2;
          plot_data.layout.width = 1200/2; 
          Plotly.newPlot("plot2", plot_data.data, plot_data.layout)

          
          plot_data = plot_calories() 
          plot_data.layout.height = 700/2;
          plot_data.layout.width = 1200/2;  
          Plotly.newPlot("plot3", plot_data.data, plot_data.layout)


        }else if(desired_nutrient == 'Macro Nutrients'){

          let plot_data = plot_macro()
          plot_data.layout.height = 700;
          plot_data.layout.width = 1200;
          Plotly.newPlot(BAR, plot_data.data, plot_data.layout) 
        }
        else if(desired_nutrient == 'Micro Nutrients'){

          let plot_data = plot_micro()
          plot_data.layout.height = 700;
          plot_data.layout.width = 1200;
          Plotly.newPlot(BAR, plot_data.data, plot_data.layout)
        }
        else if(desired_nutrient == 'Calories'){  

          let plot_data = plot_calories()  
          plot_data.layout.height = 700;
          plot_data.layout.width = 1200;
          Plotly.newPlot(BAR, plot_data.data, plot_data.layout)

        }

      });
    
})();



