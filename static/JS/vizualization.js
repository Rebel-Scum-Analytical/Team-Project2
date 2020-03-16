const personal_data = user_personal_data;
const nutrition_data = userdata_nutrition_data;
const BAR = "plot";
const selectNutrient = d3.select("#selectnutrients");



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
  
  // Initialize the city
  (function() {
    desired_nutrient = document.getElementById('selectnutrients').value = 'All';
  })();

(function(){
    
    let data = [
        {
        //   x: [],
          x: [10,20,35,40],
          y: ["Vitamin A","Vitamin C","Vitamin K","Vitamin E" ],
        //   y: [],
          type:'bar',
          orientation: 'h'
        }
      ];
    
      let layout = {
        title: "My Plot",
        xaxis: {
          title: "X-Axis",
          range: [0, 100]
        },
        yaxis: {
          title: "Y-Axis",
          
        }
      };
    
      Plotly.plot(BAR, data, layout);

      selectNutrient.on( 'change', function () {
        let desired_nutrient = selectNutrient.property("value");
        let x = [];
        let y = [];
        if( desired_nutrient == 'All')
        {

        }else if(desired_nutrient == 'Macro Nutrients'){
          x=Object.values(userdata_nutrition_data.macronutrients);
          y=Object.keys(userdata_nutrition_data.macronutrients);
        }
        else if(desired_nutrient == 'Micro Nutrients'){
          x=Object.values(userdata_nutrition_data.minerals);
          y=Object.keys(userdata_nutrition_data.minerals);
          x.push.apply(x, Object.values(userdata_nutrition_data.vitamins))
          y.push.apply(y,Object.keys(userdata_nutrition_data.vitamins))


        }
        else if(desired_nutrient == 'Calories'){

          x=Object.values(userdata_nutrition_data.calories);
          console.log(x);
          y=Object.keys(userdata_nutrition_data.calories);
          console.log(y);
          type='pie'
            // y=(Object.values(userdata_nutrition_data[desired_nutrient])/Object.values(userdata_nutrition_data[desired_nutrient])
            // x=Object.keys(userdata_nutrition_data[desired_nutrient]) 
            // x=[5,25,30,45]
            // y=["Vitamin A","Vitamin C","Vitamin K","Vitamin E" ]

        }


        Plotly.restyle(BAR, "type", [type]);
        Plotly.restyle(BAR, "x", [x]);
        Plotly.restyle(BAR, "y", [y]);
      });
    
})();



  //Handle the button click event     
const button = d3.select("#filter-btn");

button.on("click", function() {
    x=[10,20,35,40]
    y=["Vitamin A","Vitamin C","Vitamin K","Vitamin E" ]
    Plotly.restyle(BAR, "x", [x]);
    Plotly.restyle(BAR, "y", [y]);


})