  function drawChart(data) {
	var dataSet = [];
	dataSet[0] = ['Date', 'TMAX', 'TMIN'];
	for(var key in data){
		dataSet[key + 1] = [data[key].DATE, data[key].TMAX, data[key].TMIN];
	}
	var data = google.visualization.arrayToDataTable(dataSet);
	var options = {
	  title: 'Weather Forecast',
	  curveType: 'function',
	  legend: { position: 'bottom' }
	};

	var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
	
	chart.draw(data, options);
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
		respString = JSON.stringify(resp);
		document.getElementById("view").innerHTML = respString;
		drawChart(resp);
       },  
       error: function(e){  
		document.getElementById("view").innerHTML = "Error Occur!";
       }  
    });
}
