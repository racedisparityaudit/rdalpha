(function(){

  function drawOverallChart(){
    Highcharts.chart('container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Smoking prevalence at age 15'
        },
        xAxis: {
            categories: ["White", "Mixed", "Asian", "Black",
            "Chinese", "Other",
            "Unknown"],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Smoking prevalence',
                align: 'high'
            },
            labels: {
                overflow: 'justify',
                formatter: function () {
                    return (100 * this.value).toFixed(1) + "%";
                }
            }
        },
        tooltip: {
            formatter: function () {
                        if (isNaN(this.y)) {
                            return "We don't have enough data";
                        } else {
                            return '<b>' + this.key + ': ' + (100 * this.point.y).toFixed(1) + '</b>% <br>';
                        }
                    }
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true,
                    formatter: function () {
                        if (isNaN(this.y)) {
                            return "";
                        } else {
                            return '<b>' + (100 * this.y).toFixed(1) + '</b>% <br>';
                        }
                    }
                }
            }
        },
        legend: {
            enabled:false
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'All',
            data: [0.092, 0.090, 0.026, 0.0024, null, 0.029, null ]
        }]
    });
  }

  function drawRegularChart(){
    Highcharts.chart('regular', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Smoking prevalence at age 15'
        },
        xAxis: {
            categories: ["White", "Mixed", "Asian", "Black",
            "Chinese", "Other",
            "Unknown"],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Smoking prevalence',
                align: 'high'
            },
            labels: {
                overflow: 'justify',
                formatter: function () {
                    return (100 * this.value).toFixed(1) + "%";
                }
            }
        },
        tooltip: {
            formatter: function () {
                        if (isNaN(this.y)) {
                            return "We don't have enough data";
                        } else {
                            return '<b>' + this.key + ': ' + (100 * this.point.y).toFixed(1) + '</b>% <br>';
                        }
                    }
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true,
                    formatter: function () {
                        if (isNaN(this.y)) {
                            return "";
                        } else {
                            return '<b>' + (100 * this.y).toFixed(1) + '</b>% <br>';
                        }
                    }
                }
            }
        },
        legend: {
            enabled:false
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'All',
            data: [0.062, 0.054, 0.015, 0.009, null, 0.022, null ]
        }]
    });
  }

  function drawOccasionalChart(){
    Highcharts.chart('occasional', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Smoking prevalence at age 15'
        },
        xAxis: {
            categories: ["White", "Mixed", "Asian", "Black",
            "Chinese", "Other",
            "Unknown"],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Smoking prevalence',
                align: 'high'
            },
            labels: {
                overflow: 'justify',
                formatter: function () {
                    return (100 * this.value).toFixed(1) + "%";
                }
            }
        },
        tooltip: {
            formatter: function () {
                        if (isNaN(this.y)) {
                            return "We don't have enough data";
                        } else {
                            return '<b>' + this.key + ': ' + (100 * this.point.y).toFixed(1) + '</b>% <br>';
                        }
                    }
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true,
                    formatter: function () {
                        if (isNaN(this.y)) {
                            return "";
                        } else {
                            return '<b>' + (100 * this.y).toFixed(1) + '</b>% <br>';
                        }
                    }
                }
            }
        },
        legend: {
            enabled:false
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'All',
            data: [0.030, 0.037, 0.010, 0.015, null, 0.007, null ]
        }]
    });
  }



function drawCharts(){
    if(!$("#smoking").length) {
        return
    }
    console.log("drawing smoking charts");
    drawOverallChart();
    drawRegularChart();
    drawOccasionalChart();
    $("#current-selector").trigger("click");
}
    $(document).ready(drawCharts)
    $(document).on('turbolinks:load', drawCharts)
}())
