(function(){

  function drawOverallChart(){
    Highcharts.chart('container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Unemployment rate by Race'
        },
        xAxis: {
            categories: ["White", "Black", "Mixed or multiple", "Indian",
            "Pakistani/Bangladeshi", "Chinese", "Other Asian", "Other",
            "Unknown", "ALL ETHNIC MINORITY", "ALL"],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Unemployment rate',
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
            data: [0.048, 0.14, 0.112, 0.064, 0.115, 0.049, 0.066, 0.09, "* *", 0.099, 0.054]
        }]
    });
}


function drawGenderChart(){
    Highcharts.chart('gender-container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Unemployment rate by Race'
        },
        xAxis: {
            categories: ["White", "Black", "Mixed or multiple", "Indian",
            "Pakistani/Bangladeshi", "Chinese", "Other Asian", "Other",
            "Unknown", "ALL ETHNIC MINORITY", "ALL"],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Unemployment rate',
                align: 'high'
            },
            labels: {
                overflow: 'justify',
                formatter: function () {
                    return (100 * this.value).toFixed(1) + "%";
                }
            }
        },
        legend: {
            align: 'center'
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
        credits: {
            enabled: false
        },
        series: [{
            name: 'Male',
            data: [0.049, 0.152, 0.13, 0.069, 0.098, "* *", 0.07, 0.073, "* *", 0.098, 0.055]
        },{
            name: 'Female',
            data: [0.046, 0.129, 0.096, 0.057, 0.15, "* *", 0.063, 0.114, "* *", 0.101, 0.052]
        }]
    });
}




function drawGenderChart2(){
    Highcharts.chart('gender-container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Attainment 8 Scores by Race and Gender'
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
                text: 'Average GCSE grade',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
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
                        return '<b>' + 100 * this.point.value + '</b> percent <br>';
                    }
                }
            }
        },
    legend: {
        align: 'center',
        verticalAlign: 'bottom'
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




function drawAgeBracketDrilldown() {
    Highcharts.chart('age-container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Unemployment rate by age and race'
        },
        subtitle: {
            text: 'Click the bars to view race.'
        },
        xAxis: {
            type: 'category'
        },
        yAxis: {
            title: {
                text: 'Unemployment rate'
            }
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                borderWidth: 0,
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

        tooltip: {
            formatter: function () {
                        if (isNaN(this.y)) {
                            return "We don't have enough data";
                        } else {
                            return '<b>' + this.key + ': ' + (100 * this.point.y).toFixed(1) + '</b>% <br>';
                        }
                    }
        },

        series: [{
            name: 'Age brackets',
            colorByPoint: true,
            data: [{
                name: '16-24',
                y: 0.147,
                drilldown: '16-24'
            }, {
                name: '25-49',
                y: 0.042,
                drilldown: '25-49'
            }, {
                name: '50-64',
                y: 0.034,
                drilldown: '50-64'
            }]
        }],
        drilldown: {
            series: [{
                name: '16-24',
                id: '16-24',
                data: [
                    ['White',0.133],
                    ['Black',0.303],
                    ['Mixed or multiple',0.216],
                    ['Indian',0.209],
                    ['Pakistani/Bangladeshi',0.271],
                    ['Chinese','*'],
                    ['Other Asian',0.223],
                    ['Other  ',0.262],
                    ['Unknown','*'],
                    ['ALL ETHNIC MINORITY',0.252],
                    ['ALL',0.147]
                ]
            }, {
                name: '25-49',
                id: '25-49',
                data: [
['White',0.036],
['Black',0.121],
['Mixed or multiple',0.077],
['Indian',0.047],
['Pakistani/Bangladeshi',0.082],
['Chinese','*'],
['Other Asian',0.054],
['Other  ',0.072],
['Unknown','*'],
['ALL ETHNIC MINORITY',0.077],
['ALL',0.042]
                ]
            }, {
                name: '50-64',
                id: '50-64',
                data: [
                ['White',0.032],
['Black',0.094],
['Mixed or multiple','*'],
['Indian',0.055],
['Pakistani/Bangladeshi',0.07],
['Chinese','*'],
['Other Asian','*'],
['Other  ',0.064],
['Unknown','*'],
['ALL ETHNIC MINORITY',0.067],
['ALL',0.034]
                ]
            }]
        }
    });
}

function drawTimeSeriesChart() {

    Highcharts.chart('time-container', {

    title: {
        text: 'Unemployment by ethnicity, 2002-2015'
    },

    yAxis: {
        title: {
            text: 'Unemployment rate'
        },
            labels: {
                overflow: 'justify',
                formatter: function () {
                    return (100 * this.value).toFixed(1) + "%";
                }
            }
    },
    legend: {
        align: 'center',
        verticalAlign: 'bottom'
    },

    plotOptions: {
        series: {
            pointStart: 2002
        }
    },

        tooltip: {
            formatter: function () {
                if (isNaN(this.y)) {
                    return "We don't have enough data";
                } else {
                    return '<b>' + this.point.series.name + ' (' + this.key + '): ' + (100 * this.point.y).toFixed(1) + '</b>% <br>';
                }
            }
        },

    series: [{
        name: 'White',
        data: [0.047,0.045,0.043,0.043,0.048,0.048,0.052,0.07,0.073,0.075,0.073,0.068,0.055,0.048]
    }, {
        name: 'Black',
        data: [0.134,0.129,0.124,0.128,0.139,0.132,0.134,0.179,0.164,0.196,0.166,0.17,0.154,0.14]
    }, {
        name: 'Mixed or multiple',
        data: [0.164,0.13,0.125,0.12,0.132,0.116,0.134,0.158,0.141,0.158,0.154,0.148,0.132,0.112]
    }, {
        name: 'Indian',
        data: [0.072,0.077,0.06,0.065,0.077,0.068,0.075,0.093,0.078,0.093,0.094,0.09,0.061,0.064]
    }, {
        name: 'Pakistani/Bangladeshi',
        data: [0.15,0.166,0.141,0.145,0.151,0.142,0.137,0.162,0.178,0.15,0.169,0.186,0.147,0.115]
    }, {
        name: 'Chinese',
        data: [0.053,0.066,0.079,0.078,0.082,0.082,0.07,0.058,0.075,0.089,0.11,0.091,0.072,0.049]
    }, {
        name: 'Other Asian',
        data: [0.095,0.11,0.092,0.084,0.095,0.097,0.092,0.09,0.112,null,0.102,0.093,0.066,0.066]
    }, {
        name: 'Other',
        data: [0.118,0.132,0.11,0.102,0.122,0.113,0.106,0.112,0.136,0.108,0.132,0.127,0.111,0.09]
    }]

});

}

function drawCharts(){
    if(!$("#unemployment").length) {
        return
    }
    console.log("drawing unemployment charts");
    drawOverallChart();
    drawGenderChart();
    drawAgeBracketDrilldown();
    drawTimeSeriesChart();
    $("#ethnicity-selector").trigger("click")
}

    $(document).ready(drawCharts)
    $(document).on('turbolinks:load', drawCharts)
}())



