function plot_calories(){
    let data = userdata_nutrition_data.calories;
    let total = data.total;
    delete data.total;
    

    let data1 = [{
      values:  Object.values(data),
      labels : Object.keys(data),
      type: 'pie',
      //hovertext: Object.values(data)
    }]
    var layout = { 
      
      title: `Total Calories consumed ${total}`,
      paper_bgcolor: "#949291"
    }

    return(data= {
        data:data1,
        layout:layout
    })


}

function plot_micro(){
    
    let y1=Object.keys(userdata_nutrition_data.minerals);
    y1.push.apply(y1,Object.keys(userdata_nutrition_data.vitamins))
    

    let percentage_values = []
    let y2 =[]
    let query_data3={            
      gender: user_gender,
      age_key: "unit"
    }
    let query_data1={
      age_key :user_age_key,
      gender: user_gender,
    }
    Object.keys(userdata_nutrition_data.minerals).forEach(function(key){          
      query_data1.nutrient = key;
      query_data3.nutrient = key;
      percentage_values.push(userdata_nutrition_data.minerals[key]*100 / dri_micro_nutrient_minerals(query_data1));
      //y2.push(dri_micro_nutrient_minerals(query_data3))
      y2.push(`Current Value : ${userdata_nutrition_data.minerals[key]}, Max value : ${dri_micro_nutrient_minerals(query_data1)} ${dri_micro_nutrient_minerals(query_data3)}`)

    })

   let query_data2={
      age_key :user_age_key,
      gender: user_gender,
    }
    Object.keys(userdata_nutrition_data.vitamins).forEach(function(key){          
        query_data2.nutrient = key;
        query_data3.nutrient = key;
        percentage_values.push(userdata_nutrition_data.vitamins[key]*100 / dri_micro_nutrient_vitamins(query_data2));
        y2.push(`Current Value : ${userdata_nutrition_data.vitamins[key]}, Max value : ${dri_micro_nutrient_vitamins(query_data2)} ${dri_micro_nutrient_vitamins(query_data3)}`)
      })

    var trace1 ={
      x : percentage_values,
      y : y1,
      type :'bar',
      orientation: 'h',
      text:y2.flat()
    }
        
      let data1 = [trace1];
      var layout = {
        title: "User Micro Nutrient intake as a Percent of RDA of Nutrient ",
        yaxis: {
          autotick: false,
          ticks: 'outside',
          tick0: 0,
          dtick: 0.25,
          ticklen: 8,
          tickwidth: 4,
          tickcolor: '#000',
          tickangle: 315,
         
        },
        // height: 100,
        // width: 1200,
        paper_bgcolor: "#fed8b1"
    }

        return(data= {
            data:data1,
            layout:layout
        })
}

function plot_macro(){
    let percentage_values = []
    let text = []
    let query_data3={            
            gender: user_gender,
            age_key: "unit"
          }

    let query_data={
            age_key :user_age_key,
            gender: user_gender,
          }
          Object.keys(userdata_nutrition_data.macronutrients).forEach(function(key){
          
            query_data.nutrient = key;
            query_data3.nutrient = key;
            percentage_values.push(userdata_nutrition_data.macronutrients[key]*100 / dri_macro_nutrient(query_data));
            text.push(`Current Value : ${userdata_nutrition_data.macronutrients[key]} , 
            Max Value: ${dri_macro_nutrient(query_data)} ${dri_macro_nutrient(query_data3)} `)
            })

        let data1 =[{
            x:percentage_values,
            y:Object.keys(userdata_nutrition_data.macronutrients),
            type:'bar',
            orientation: 'h',
            text:text

          }]

          var layout = {
            title: "User Macro Nutrient intake as a Percent of RDA of Nutrient ",
            yaxis: {
              autotick: false,
              ticks: 'outside',
              tick0: 0,
              dtick: 0.25,
              ticklen: 8,
              tickwidth: 4,
              tickcolor: '#000',
              tickangle: 315,
              
            },
            paper_bgcolor: "#fed8b1"
           }

           return(data= {
            data:data1,
            layout:layout
        })
}