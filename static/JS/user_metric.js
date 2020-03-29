function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  listfood(newSample);
}

function listfood(new_breakfast) {
 
 url = `/user_metrics/${new_breakfast}`;
 

  let data = d3.json(url).then(function(new_breakfast){
    console.log("I am in user_metric.js")
    // Use d3 to select the panel with id of `#food_data`
    let selection = d3.select("#comment");
    selection.html("");
      // Use `.html("") to clear any existing data
  
      // Use `Object.entries` to add each key and value pair to the panel
      // Hint: Inside the loop, you will need to use d3 to append new
      // tags for each key-value in the metadata.
      var row = d3.select("#comment")
      .selectAll('li')
      .data(data)
      
      row          
      .enter()
      .append("li")
      .text(function(d){return d.key + d.value})
    
      
})
};


