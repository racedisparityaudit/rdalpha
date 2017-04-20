var mapData = $.ajax('/assets/uk_map.json');
var ethnicityData = $.ajax('/assets/ethnicitydata.json');

$.when(mapData, ethnicityData).done(init);

function init(mapData, ethnicityData) {

	var mapData = mapData[0];
	var ethnicityData = ethnicityData[0];

	var options = {
		maxBounds: [[58.16745, -7.52916], [49.00275, -7.26308], [49.0525, 2.87146], [58.20681, 2.7386]],
		minZoom: 5,
		maxZoom: 5,
		zoomControl: false
	}

	var attr = { attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' };
	var tiles = 'http://{s}.tile.osm.org/{z}/{x}/{y}.png';

	var mapColor = '#005EA5';

	function ColorLuminance(hex, lum) {

	// validate hex string
	hex = String(hex).replace(/[^0-9a-f]/gi, '');
	if (hex.length < 6) {
		hex = hex[0]+hex[0]+hex[1]+hex[1]+hex[2]+hex[2];
	}
	lum = lum || 0;

	// convert to decimal and change luminosity
	var rgb = "#", c, i;
	for (i = 0; i < 3; i++) {
		c = parseInt(hex.substr(i*2,2), 16);
		c = Math.round(Math.min(Math.max(0, c + (c * lum)), 255)).toString(16);
		rgb += ("00"+c).substr(c.length);
	}

	return rgb;
	}

	function shadeColor(color, percent) {   
		var f=parseInt(color.slice(1),16),t=percent<0?0:255,p=percent<0?percent*-1:percent,R=f>>16,G=f>>8&0x00FF,B=f&0x0000FF;
		return "#"+(0x1000000+(Math.round((t-R)*p)+R)*0x10000+(Math.round((t-G)*p)+G)*0x100+(Math.round((t-B)*p)+B)).toString(16).slice(1);
	}

	function getPercent(min, max, value) {
		return (value - min) / (max - min);
	}

	function round10(value) {
		return Math.round(value * 100) / 100;
	}

	function Map(id, options, tiles, attr, regionData) {

		var _map = L.map(id, options)
		.setView([51.505, -0.09], 5);

		var topoLayer = new L.TopoJSON();

		var i = 1;

		L.tileLayer(tiles, attr).addTo(_map);

		topoLayer.addTo(_map);
		topoLayer.addData(mapData);

		topoLayer.eachLayer(function (layer) {

			if (regionData !== 'undefined') {
				var index = layer.feature.properties.EER13NM;
				var percent = round10(getPercent(5.1, 6.2, regionData[index]));
				var color = ColorLuminance(mapColor, percent);
			}
			else {
				var color = mapColor;
			}

			function mouseOverHandler() {
				this.setStyle({ fillOpacity: 1 })
			}

			function mouseOutHandler() {
				this.setStyle({ weight: 1, fillColor: color, fillOpacity: .95 })
			}

			function onClick() {
				if (regionData !== 'undefined') {
					var index = this.feature.properties.EER13NM;
					console.log(regionData[index]);
				}
			}

			layer.setStyle({
				color: color,
				fillOpacity: .95,
				weight: 1,
				stroke: true
			});

			layer.on({
				mouseover: mouseOverHandler,
				mouseout: mouseOutHandler,
				click: onClick
			});

		});

		topoLayer.resetStyle({
			stroke: false
		});

		return _map;
	}

	$(window).ready(function() {
		// validation
		if ($("#map_1").length) {
			console.log("load maps");
			new Map('map_1', options, tiles, attr, ethnicityData.white);
			new Map('map_2', options, tiles, attr, ethnicityData.black);
			new Map('map_3', options, tiles, attr, ethnicityData.asian);
			new Map('map_4', options, tiles, attr, ethnicityData.chinese);
			new Map('map_5', options, tiles, attr, ethnicityData.mixed);
		}
	});

}