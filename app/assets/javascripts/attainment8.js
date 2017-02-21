(function(){

  function drawOverallChart(){
    Highcharts.chart('container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Attainment 8 Scores by Ethnicity'
        },
        subtitle: {
            text: 'Source: Department for Education'
        },
        xAxis: {
            categories: ['Black', 'White', 'Mixed', 'Asian', 'Other'],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Mean GCSE grade',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            valueSuffix: ' average'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        legend: {
            // layout: 'vertical',
            // align: 'right',
            // verticalAlign: 'top',
            // x: -40,
            // y: 80,
            // floating: true,
            // borderWidth: 1,
            // backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
            // shadow: true
            enabled:false
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'All',
            data: [4.89, 4.98, 5.06, 5.29, 6.3]
        }]
    });
}






function drawOverallChartWithSubgroups(){
    Highcharts.chart('container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Attainment 8 Scores by Ethnicity'
        },
        subtitle: {
            text: 'Source: Department for Education'
        },
        xAxis: {
            categories: ['White', 'White British', 'Irish', 'Traveller of Irish heritage', 'Gypsy/Roma', 'Any other white background',
                        'Mixed', 'White and Black Caribbean', 'White and Black African', 'White and Asian', "Any other mixed background",
                        'Asian', 'Indian', 'Pakistani', 'Bangladeshi', 'Any other Asian background',
                        'Black', 'Black Caribbean', 'Black African', 'Any other black background',
                        'Chinese', 'Any other ethnic group', 'Unclassified'],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Mean GCSE grade',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            valueSuffix: ' average'
        },
        credits: {
            enabled: false
        },
        legend: {
            reversed: true
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true,
                    inside: false,
                    color: '#000000',
                    formatter: function() {
                        console.log(this);
                        if (this.y > 0) {
                            return this.y;
                        } else {
                            return '';
                        }
                    }
                }
            },
            series: {
                stacking: 'normal'
            }
        },
        series: [{
            name: 'Minor Categories',
            data: [0, 4.97, 5.45, 2.93, 2.04, 4.95,
                    0, 4.63, 5.02, 5.45, 5.18,
                    0, 5.7, 4.85, 5.21, 5.5,
                    0, 4.54, 5.03, 4.70,
                    0, 5.01, 4.4],
            pointWidth: 16
        },{
            name: 'Major Categories',
            data: [4.97, 0, 0, 0, 0, 0,
                    5.05, 0, 0, 0, 0,
                    5.25, 0, 0, 0, 0,
                    4.87, 0, 0, 0,
                    6.24, 0, 0],
            pointWidth: 16
        }]
    });
}





  function drawGenderChart(){
    Highcharts.chart('gender-container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Attainment 8 Scores by Ethnicity and Gender'
        },
        subtitle: {
            text: 'Source: Department for Education'
        },
        xAxis: {
            categories: ['Black', 'White', 'Mixed', 'Asian', 'Other', 'All'],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Mean GCSE grade',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            valueSuffix: ' average'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        legend: {
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'Male',

            data: [4.59, 4.76, 4.82, 5.09, 6.09, 4.78]
        },{
            name: 'Female',
            data: [5.19, 5.20, 5.31, 5.50, 6.51, 5.24]
        }]
    });
}






function drawHeatMap() {

Highcharts.chart('heatmap-container', {

    chart: {
        type: 'heatmap',
        marginTop: 40,
        marginBottom: 80,
        plotBorderWidth: 1
    },


    title: {
        text: 'GCSE Average Grade by Race and Region'
    },

    xAxis: {
        categories: ['White', 'Black', 'Asian', 'Mixed', 'Other', 'All']
    },

    yAxis: {
        categories: ['North East', 'North West', 'Yorkshire and the Humber', 'East Midlands', 'West Midlands', 'East', 'London', 'Inner London', 'Outer London', 'South East', 'South West', 'England'],
        title: null
    },

    colorAxis: {
        stops: [
            [0, '#f26c43'],
            [0.4, '#ffffff'],
            [1.8, '#5ca0ff']
        ],
        min: 4
    },

    legend: {
        align: 'right',
        layout: 'vertical',
        margin: 0,
        verticalAlign: 'top',
        y: 25,
        symbolHeight: 280
    },

    tooltip: {
        formatter: function () {
            return '<b>' + this.series.xAxis.categories[this.point.x] + '</b> in <b>' + this.series.yAxis.categories[this.point.y] + '</b><br\>' +
this.point.value +
'</b> average <br>';
        }
    },

    series: [{
        name: 'Sales per employee',
        borderWidth: 1,
        data: [[0, 0, 4.86], [1, 0, 5.23], [2, 0, 5.31], [3, 0, 5.1], [4, 0, 6.12], [5, 0, 4.87], [0, 1, 4.92], [1, 1, 4.95], [2, 1, 5.12], [3, 1, 4.86], [4, 1, 6.19], [5, 1, 4.94], [0, 2, 4.92], [1, 2, 4.81], [2, 2, 4.77], [3, 2, 4.67], [4, 2, 6.31], [5, 2, 4.89], [0, 3, 4.86], [1, 3, 4.84], [2, 3, 5.21], [3, 3, 4.75], [4, 3, 6.12], [5, 3, 4.89], [0, 4, 4.9], [1, 4, 4.85], [2, 4, 5.08], [3, 4, 4.75], [4, 4, 6.13], [5, 4, 4.92], [0, 5, 5], [1, 5, 5.08], [2, 5, 5.37], [3, 5, 5.19], [4, 5, 6.23], [5, 5, 5.04], [0, 6, 5.17], [1, 6, 5.2], [2, 6, 5.58], [3, 6, 4.92], [4, 6, 6.44], [5, 6, 5.19], [0, 7, 5.21], [1, 7, 5.1], [2, 7, 5.35], [3, 7, 4.87], [4, 7, 6.34], [5, 7, 5.13], [0, 8, 5.16], [1, 8, 5.26], [2, 8, 5.7], [3, 8, 4.96], [4, 8, 6.48], [5, 8, 5.23], [0, 9, 5.07], [1, 9, 5.21], [2, 9, 5.56], [3, 9, 4.96], [4, 9, 6.41], [5, 9, 5.1], [0, 10, 5.02], [1, 10, 5.13], [2, 10, 5.42], [3, 10, 4.46], [4, 10, 6.24], [5, 10, 5.03], [0, 11, 4.98], [1, 11, 5.06], [2, 11, 5.29], [3, 11, 4.89], [4, 11, 6.3], [5, 11, 5.01]],
        dataLabels: {
            enabled: true,
            color: '#000000'
        }
    }]

});
}

    function drawCharts(){
        console.log("drawing charts");
        drawOverallChartWithSubgroups();
        drawGenderChart();
        drawHeatMap();
    }

$(document).ready(drawCharts)
$(document).on('turbolinks:load', drawCharts)
}())


