  function drawChart(dataSet, chartView, name) {
	var plotData = google.visualization.arrayToDataTable(dataSet);
	var options = {
	  title: name,
	  curveType: 'function',
	  legend: { position: 'bottom'},
	  vAxis: {title: 'Temperature'}
	};

	var chart = new google.visualization.LineChart(document.getElementById(chartView));
	
	chart.draw(plotData, options);
  }
  
  function loadDoc() {
	var date = $('#dateid').val()
	var myUrl = "http://ec2-52-37-173-114.us-west-2.compute.amazonaws.com/forecast/"
	myUrl += date
	var dates, tmax, tmin; 
	$.ajax({  
       type: "GET",  
       url: myUrl, 	         
       success: function(resp){ 
		var dataSet = [];
		dataSet[0] = ['Date', 'TMAX', 'TMIN'];
		for(var key = 0; key < resp.length; key++){
			dataSet[key+1] = [resp[key].DATE, resp[key].TMAX, resp[key].TMIN];
		}
		drawChart(dataSet, 'mychart','My Weather Forecast');
       },  
       error: function(e){  
		alert("Error: Input field is empty or dataType is incorrect!");
       }  
    });
}

function yahooWeather() {
	var weatherUrl = "https://query.yahooapis.com/v1/public/yql?q=select%20item%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22cincinnati%2C%20oh%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys";
	$.ajax({  
       type: "GET",  
       url: weatherUrl, 	         
       success: function(data){ 
		var forecast = data.query.results.channel.item.forecast;
	   	var dataSet = [];
		dataSet[0] = ['Date', 'TMAX', 'TMIN'];
		for(var key = 0; key < forecast.length; key++){
			dataSet[key+1] = [forecast[key].date, parseInt(forecast[key].high), parseInt(forecast[key].low)];
		}
		drawChart(dataSet, 'yahoochart', 'Yahoo Weather Forecast for Cincinnati, OH');
       },  
       error: function(e){  
		alert("Error Occur!");
       }  
    });
  };
