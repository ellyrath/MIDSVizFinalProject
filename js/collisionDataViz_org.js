// get the data
var collision = [];

function sortCollisionData(){
  collision.sort(function(a,b) {return (new Date(a.date) > new Date(b.date)) ? 1 : ((new Date(b.date) > new Date(a.date)) ? -1 : 0);} );
}

function hideSpinner(){
  $('#spinner').hide();
}

function drawVizualization(){

// set the dimensions and margins of the graph
var margin = {top: 20, right: 20, bottom: 30, left: 100},
    width = 1500 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

// parse the date / time
// var parseTime = d3.timeParse("%m/%d/%Y"),
var parseTime = d3.timeParse("%Y%m%d"),
    bisectDate = d3.bisector(function(d) { return d.date; }).left;

// set the ranges
var x = d3.scaleTime().range([0, width]);
var y = d3.scaleLinear().range([height, 0]);

// define the area
var area = d3.area()
    .x(function(d) { return x(d.date); })
    .y0(height)
    .y1(function(d) { return y(d.count); });

// define the line
var valueline = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.count); });

var svg = d3.select("#collisionData").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + ", " + margin.top + ") ");


// d3.csv("NYPD_Motor_Vehicle_Collisions.csv ", function(error, data) {
d3.csv("accidentsperday.csv ", function(error, data) {
  if (error) throw error;

  // var collisionDict = {};
  // for (var i =0; i < data.length; i++){
  //       data[i].date = parseTime(data[i].date);
  //   if (data[i].date in collisionDict){
  //     collisionDict[data[i].date] = ++collisionDict[data[i].date];
  //   }else{
  //     collisionDict[data[i].date] = 1;
  //   }
  // }
  // for (var item in collisionDict){
  //   collision.push({date: new Date(item), count:collisionDict[item]});
  // }

    data.forEach(function(d) {
      d.date = parseTime(d.date);
      d.count = +d.count;
  });

  // sortCollisionData();
  // scale the range of the data
  x.domain(d3.extent(data, function(d) { return d.date; }));
  y.domain([0, d3.max(data, function(d) { return d.count; })]);

  // add the area
  svg.append("path")
     .data([data])
     .attr("class", "area")
     .attr("d", area);

  // add the valueline path.
  svg.append("path")
      .data([data])
      .attr("class", "line")
      .attr("d", valueline);

  // add the X Axis
  svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x))
      .append("text")
      .attr("x", width/2)
      .attr("y", 20)
      .attr("dy", ".71em")
      .style("text-anchor", "middle")
      .style("fill", "black")
      .text("Year");

  // add the Y Axis
  svg.append("g")
      .call(d3.axisLeft(y))
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .style("fill", "black")
      .text("Number of collisions");

//Tooltip
  var focus = svg.append("g")
      .attr("class", "focus")
      .style("display", "none");

  focus.append("circle")
      .attr("r", 4.5);

  focus.append("rect")
      .attr("class", "tooltip")
      .attr("width", 100)
      .attr("height", 50)
      .attr("x", 10)
      .attr("y", -22)
      .attr("rx", 4)
      .attr("ry", 4);

  focus.append("text")
      .attr("class", "tooltip-date")
      .attr("x", 18)
      .attr("y", -2);

  focus.append("text")
      .attr("x", 18)
      .attr("y", 18)
      .text("Collisions:");

  focus.append("text")
      .attr("class", "tooltip-count")
      .attr("x", 95)
      .attr("y", 18);      

  svg.append("rect")
      .attr("class", "overlay")
      .attr("width", width)
      .attr("height", height)
      .on("mouseover", function() { focus.style("display", null); })
      .on("mouseout", function() { focus.style("display", "none"); })
      .on("mousemove", mousemove);

  function mousemove() {
    var x0 = x.invert(d3.mouse(this)[0]),
        i = bisectDate(data, x0, 1),
        d0 = data[i - 1],
        d1 = data[i],
        d = x0 - d0.date > d1.date - x0 ? d1 : d0;
    focus.attr("transform", "translate(" + x(d.date) + "," + y(d.count) + ")");
    // focus.select("text").text(d.count);
    focus.select(".tooltip-date").text(d.date.toLocaleDateString());
    focus.select(".tooltip-count").text(d.count);    
  }      

  hideSpinner();

});
}

drawVizualization();