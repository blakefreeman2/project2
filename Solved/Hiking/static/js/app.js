// from data.js
d3.json('/api/hiking', function (error,tableData) {

    var minLength = 0;
    var maxLength = 0;
    var difficulty = "";

    // Need to select "tbody" in the index.html page using d3
    var tbody = d3.select("tbody");

    // Build a table every time we call the table
    // Clear out table first every time is called
    function masterTable(trailData) {
        tbody.html("");
        trailData.forEach((trailObjects) => {
            var cityName = trailObjects.location.split(',')[0];
            var row = tbody.append("tr");
            // only need value since we already have the keys set-up

                row.append("td").text(trailObjects.name);
                row.append("td").text(cityName);
                // row.append("td").text(trailObjects.length);
                row.append("td").text(trailObjects.difficulty);
                // row.append("td").text(trailObjects.stars);
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
        var cityInput = d3.select("#city").property("value");
        var nameInput = d3.select("#trailname").property("value");
        var difficultyInput = difficulty;
        // var lengthInput = d3.select("#country").property("value");

        // allows for individual filters
        var filteredData = tableData
        
        if(cityInput) {
            filteredData = filteredData.filter(row => row.location === cityInput);
            console.log(filteredData)
        }
        if(nameInput) {
            filteredData = filteredData.filter(row => row.name === nameInput);
        }
        if(difficultyInput) {
            filteredData = filteredData.filter(row => row.difficulty === difficultyInput);
        }
        // if(lengthInput) {
        //     filteredData = filteredData.filter(row => row.country === lengthInput);
        // };
        console.log(filteredData)
        
        

        // pass in masterTable again but with newly created filteredData function
        masterTable(filteredData)
    })


    function handleLengthChange(control) {
        var length = control.value;
        var splitLength = length.split('-');
        minLength = splitLength[0];
        maxLength = splitLength[1];
        console.log("minLength is ", minLength);
        console.log("maxLength is ", maxLength);
    }

    function handleDifficultyChange(control) {
        difficulty = control.value;
    }
});