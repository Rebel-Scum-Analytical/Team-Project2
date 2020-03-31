// Select the button
let button = d3.select("#search-btn").on("click", function() {
// Select the food item entered
let inputFood = d3.select("#foodsearch").property("value"); 
// Display the input food item in search box
console.log("Entered food item is: "+ inputFood);
//  Error handling for blank input date
if (inputFood == '') {
    alert("Please enter a food item name in the search box");
    }

// Code to append data for the entered data in filter box 
else{
    // Filter Data with food description equal to input food item details
    let filteredData = data.filter(e => e.Shrt_Desc === inputFood);
    //  Display the filtered data for the entered food details on the web page
    console.log("filtered food item is: " , filteredData);
    // Error handling for food item not present in data.js file
    if (filteredData.length === 0){
        alert("No nutrition information present for the entered food item")}
    else {    
    // Code to add table header
    // <tr>
              
    //                   <th scope="row">Totals</th>
    //                       <td>0</td>                  
    //                       <td>-</td>
    //                       <td>-</td>
    //                       <td>-</td>
    //                       <td>0</td>                  
    //                       <td>0</td>
    //                 </tr>

        // let tbody = d3.select("tbody");

        
        // let row = tbody.append("tr", true)
        // let rowTh = row.append("th").attr("scope", "true")
        // rowTh.text("Shrt_Desc");
        // row.append("td").text(e.Shrt_Desc)



        // row.append("td").text("Energy")
        // row.append("td").text("Carbohydrate")
        // row.append("td").text("Protein")
        // row.append("td").text("Lipid_Total")
        // row.append("td").text("Fiber")
        // row.append("td").text("Sugar_Total")

    filteredData.forEach(e => {
        // Append one table row with nutrition info for the food entered when button is clicked

        
        // let row = d3.select("tbody").append("tr", true)
        // row.append("td").text(e.Shrt_Desc)
        // row.append("td").text(e.Energy)
        // row.append("td").text(e.Carbohydrate)
        // row.append("td").text(e.Protein)
        // row.append("td").text(e.Lipid_Total)
        // row.append("td").text(e.Fiber)
        // row.append("td").text(e.Sugar_Total)    

        let tbodyElem = d3.select("tbody")
        tbodyElem.html("")

        addNutriRow(tbodyElem,"Shrt_Desc", e.Shrt_Desc);
        addNutriRow(tbodyElem,"Energy", e.Energy);
        addNutriRow(tbodyElem,"Carbohydrate", e.Carbohydrate);
        addNutriRow(tbodyElem,"Protein", e.Protein);
        addNutriRow(tbodyElem,"Lipid_Total", e.Lipid_Total);
        addNutriRow(tbodyElem,"Fiber", e.Fiber);
        addNutriRow(tbodyElem,"Sugar_Total", e.Sugar_Total);

            })
        }    

        document.getElementById("nutriFacts").style.visibility = "visible";
        // d3.select("#nutriFacts").style.attr("visibility","visible")

    }

});

function addNutriRow(tbodyElem, label, value){
    let row = tbodyElem.append("tr", true)
    let rowTh = row.append("th").attr("scope", "true")
    rowTh.text(label);
    row.append("td").text(value)
}