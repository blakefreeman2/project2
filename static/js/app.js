// from data.js
var tableData = data;

// YOUR CODE HERE!

// Need to select "tbody" in the index.html page using d3
var tbody = d3.select("tbody");

// Build a table every time we call the table
// Clear out table first every time is called
function masterTable(ufoData) {
    tbody.html("");
    ufoData.forEach((ufoObjects) => {
        var row = tbody.append("tr");
        // only need value since we already have the keys set-up
        Object.values(ufoObjects).forEach((value) => {
            var cell = row.append("td");
            cell.text(value);
        })
    }) 
}

// pass in tableData to the created function to see on .html page
masterTable(tableData);

// select button and locate the #filter-btn (this is a ID so use # symbol)
var press = d3.select("#filter-btn");

// activate button (Enter a Date)
press.on("click", function() {
    // prevent page from refreshing (stops the page from clearing out inputs)
    d3.event.preventDefault();
    // use .property("value") to grab value at the time the button is clicked
    var dateInput = d3.select("#datetime").property("value");
    var cityInput = d3.select("#city").property("value");
    var stateInput = d3.select("#state").property("value");
    var countryInput = d3.select("#country").property("value");
    var shapeInput = d3.select("#shape").property("value");

    // allows for individual filters
    var filteredData = tableData
    if(dateInput) {
        filteredData = filteredData.filter(row => row.datetime === dateInput);
    }
    if(cityInput) {
        filteredData = filteredData.filter(row => row.city === cityInput);
    }
    if(stateInput) {
        filteredData = filteredData.filter(row => row.state === stateInput);
    }
    if(stateInput) {
        filteredData = filteredData.filter(row => row.country === countryInput);
    }
    if(stateInput) {
        filteredData = filteredData.filter(row => row.shape === shapeInput);
    };
    console.log(filteredData)
    
    

    // pass in masterTable again but with newly created filteredData function
    masterTable(filteredData)
})


