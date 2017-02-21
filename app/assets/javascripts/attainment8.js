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
            // layout: 'vertical',
            // align: 'right',
            // verticalAlign: 'top',
            // x: -40,
            // y: 80,
            // floating: true,
            // borderWidth: 1,
            // backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
            // shadow: true
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

    function drawCharts(){
        console.log("drawing charts");
        drawOverallChart();
        drawGenderChart();
    }

$(document).ready(drawCharts)
}())


