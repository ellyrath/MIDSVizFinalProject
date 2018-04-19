function timeSeriesChart() {
    var margin = { top: 20, right: 20, bottom: 20, left: 20 },
        width = 760,
        height = 120,
        xValue = function(d) { return d[0]; },
        yValue = function(d) { return d[1]; },
        xScale = d3.scaleTime(),
        yScale = d3.scaleLinear(),
        bisectDate = d3.bisector(function(d) { return d.date; }).left,
        // xAxis = d3.svg.axis().scale(xScale).orient("bottom").tickSize(6, 0),
        xAxis = d3.axisBottom(xScale).tickSize(6, 0),
        area = d3.area().x(X).y0(height).y1(Y),
        line = d3.line().x(X).y(Y);

    function chart(selection) {
        selection.each(function(data) {

            // Convert data to standard representation greedily;
            // this is needed for nondeterministic accessors.
            data = data.map(function(d, i) {
                return [xValue.call(data, d, i), yValue.call(data, d, i)];
            });

            // Update the x-scale.
            xScale
                .domain(d3.extent(data, function(d) { return d[0]; }))
                .range([0, width - margin.left - margin.right]);

            // Update the y-scale.
            yScale
                .domain([0, d3.max(data, function(d) { return d[1]; })])
                .range([height - margin.top - margin.bottom, 0]);

            // Select the svg element, if it exists.
            var svg = d3.select(this).selectAll("svg").data([data]);

            // Otherwise, create the skeletal chart.
            var gEnter = svg.enter().append("svg").append("g");
            gEnter.append("path").attr("class", "area");
            gEnter.append("path").attr("class", "line");
            gEnter.append("g").attr("class", "x axis");


            // Update the outer dimensions.
            svg.attr("width", width)
                .attr("height", height);

            // Update the inner dimensions.
            var g = svg.select("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

            // Update the area path.
            g.select(".area")
                .attr("d", area.y0(yScale.range()[0]));

            // Update the line path.
            g.select(".line")
                .attr("d", line);

            // Update the x-axis.
            g.select(".x.axis")
                .attr("transform", "translate(0," + yScale.range()[0] + ")")
                .call(xAxis);

            // Tooltip

            var focus = svg.append("g")
                .attr("class", "focus")
                .style("display", "none");

            focus.append("circle")
                .attr("r", 4.5);

            focus.append("text")
                .attr("x", 9)
                .attr("dy", ".35em");

            svg.append("rect")
                .attr("class", "overlay")
                .attr("width", width)
                .attr("height", height)
                .on("mouseover", function() { focus.style("display", null); })
                .on("mouseout", function() { focus.style("display", "none"); })
                .on("mousemove", mousemove);

            function mousemove() {
                var x0 = xScale.invert(d3.mouse(this)[0]),
                    i = bisectDate(data, x0, 1),
                    d0 = data[i - 1],
                    d1 = data[i],
                    d = x0 - d0.date > d1.date - x0 ? d1 : d0;
                focus.attr("transform", "translate(" + xScale(d[0]) + "," + yScale(d[1]) + ")");
                focus.select("text").text(d.count);
            }
        });
    }

    // The x-accessor for the path generator; xScale ∘ xValue.
    function X(d) {
        return xScale(d.date);
    }

    // The x-accessor for the path generator; yScale ∘ yValue.
    function Y(d) {
        return yScale(d.count);
    }

    chart.margin = function(_) {
        if (!arguments.length) return margin;
        margin = _;
        return chart;
    };

    chart.width = function(_) {
        if (!arguments.length) return width;
        width = _;
        return chart;
    };

    chart.height = function(_) {
        if (!arguments.length) return height;
        height = _;
        return chart;
    };

    chart.x = function(_) {
        if (!arguments.length) return xValue;
        xValue = _;
        return chart;
    };

    chart.y = function(_) {
        if (!arguments.length) return yValue;
        yValue = _;
        return chart;
    };

    return chart;
}