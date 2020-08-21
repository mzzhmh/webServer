
google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.load('current', {packages: ['corechart', 'line']});
function drawNSWDailyChart() {
	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Date');
	data.addColumn('number', 'Daily Increased Cases');
	//
	var Data = $.ajax({
		url: "/getNSWDailyData",
	    dataType: "json",
	    type: "GET",
	    contentType: 'application/json',
	    async: false
	}).responseText;
	data.addRows(JSON.parse(Data));

	var options = {
		chart: {
			title: 'NSW Daily Increased Cases'
		}
	};

	var materialChart = new google.charts.Bar(document.getElementById('piechart'));
	materialChart.draw(data, options);
}

function drawNSWTotalChart() {


	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Date');
	data.addColumn('number', 'NSW Total Confirmed Cases');

	var Data = $.ajax({
		url: "/getNSWTotalData",
	    dataType: "json",
	    type: "GET",
	    contentType: 'application/json',
	    async: false
	}).responseText;
	data.addRows(JSON.parse(Data));

	var options = {
		chart: {
			title: 'NSW Total Confirmed Cases'
		},
		hAxis: {
			title: 'Date'
		},
		vAxis: {
			title: 'NSW Total Confirmed Cases'
		}
	};

	var chart = new google.visualization.LineChart(document.getElementById('piechart'));
	chart.draw(data, options);
}

function drawNSWRecoveryChart() {


	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Date');
	data.addColumn('number', 'NSW Total Recovered Cases');

	var Data = $.ajax({
		url: "/getNSWRecoveryData",
	    dataType: "json",
	    type: "GET",
	    contentType: 'application/json',
	    async: false
	}).responseText;
	data.addRows(JSON.parse(Data));

	var options = {
		chart: {
			title: 'NSW Total Recovered Cases'
		},
		hAxis: {
			title: 'Date'
		},
		vAxis: {
			title: 'NSW Total Recovered Cases'
		}
	};

	var chart = new google.visualization.LineChart(document.getElementById('piechart'));
	chart.draw(data, options);
}

function drawNSWActiveChart() {


	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Date');
	data.addColumn('number', 'NSW Remained Active Cases');

	var Data = $.ajax({
		url: "/getNSWactiveData",
	    dataType: "json",
	    type: "GET",
	    contentType: 'application/json',
	    async: false
	}).responseText;
	data.addRows(JSON.parse(Data));

	var options = {
		chart: {
			title: 'NSW Remained Active Cases'
		},
		hAxis: {
			title: 'Date'
		},
		vAxis: {
			title: 'NSW Remained Active Cases'
		}
	};

	var chart = new google.visualization.LineChart(document.getElementById('piechart'));
	chart.draw(data, options);
}

function drawNSWTestChart() {

	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Date');
	data.addColumn('number', 'NSW Daily Tested Cases');

	var Data = $.ajax({
		url: "/getNSWTestData",
	    dataType: "json",
	    type: "GET",
	    contentType: 'application/json',
	    async: false
	}).responseText;
	data.addRows(JSON.parse(Data));

	var options = {
		chart: {
			title: 'NSW Daily Tested Cases'
		},
		hAxis: {
			title: 'Date'
		},
		vAxis: {
			title: 'NSW Daily Tested Cases'
		}
	};

	var chart = new google.visualization.LineChart(document.getElementById('piechart'));
	chart.draw(data, options);
}

function drawNSWDeathChart() {

	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Date');
	data.addColumn('number', 'NSW Total Death');

	var Data = $.ajax({
		url: "/getNSWDeathData",
	    dataType: "json",
	    type: "GET",
	    contentType: 'application/json',
	    async: false
	}).responseText;
	data.addRows(JSON.parse(Data));

	var options = {
		chart: {
			title: 'NSW Total Death'
		},
		hAxis: {
			title: 'Date'
		},
		vAxis: {
			title: 'NSW Total Death'
		}
	};

	var chart = new google.visualization.LineChart(document.getElementById('piechart'));
	chart.draw(data, options);
}

function drawAUDailyChart() {
	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Date');
	data.addColumn('number', 'National Increased Daily');

	var Data = $.ajax({
		url: "/getAUDailyData",
	    dataType: "json",
	    type: "GET",
	    contentType: 'application/json',
	    async: false
	}).responseText;
	data.addRows(JSON.parse(Data));

	var options = {
		chart: {
			title: 'National Increased Daily'
		}
	};

	var materialChart = new google.charts.Bar(document.getElementById('piechart'));
	materialChart.draw(data, options);
}

function drawAUTotalChart() {

	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Date');
	data.addColumn('number', 'National Total Confirmed Cases');

	var Data = $.ajax({
		url: "/getAUTotalData",
	    dataType: "json",
	    type: "GET",
	    contentType: 'application/json',
	    async: false
	}).responseText;
	data.addRows(JSON.parse(Data));

	var options = {
		chart: {
			title: 'National Total Confirmed Cases'
		},
		hAxis: {
			title: 'Date'
		},
		vAxis: {
			title: 'National Total Confirmed Cases'
		}
	};

	var chart = new google.visualization.LineChart(document.getElementById('piechart'));
	chart.draw(data, options);
}
function openCity(evt, cityName) {
	var i, tabcontent, tablinks;
	tabcontent = document.getElementsByClassName("tabcontent");
	for (i = 0; i < tabcontent.length; i++) {
		tabcontent[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName("tablinks");
	for (i = 0; i < tablinks.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" active", "");
	}
	document.getElementById(cityName).style.display = "block";
	evt.currentTarget.className += " active";
}
function NSWDaily(){
	//console.log("loading figures");
	//        //drawNSWDailyChart();
	//
	//                //var options = {'title':'My Average Day', 'width':450, 'height':400};
	//
	modal.style.display = "block";
	modal.style.visibility = "hidden";
	drawNSWDailyChart();
	modal.style.visibility = "visible";
	 //get parent container size
	 //        //const EleChart = document.querySelector('#piechart');
	 //                //console.log(EleChart.getBoundingClientRect());
	 //                        //height = EleChart.getBoundingClientRect().height
	 //                                //width = EleChart.getBoundingClientRect().width
	 //
}

function replaceAt(index, replacement) {
	    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}

function AUCross(){
	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Date');
	//get what columns are checked
	var code = "0000000000";
	var NSWckBox = document.getElementsByClassName("custom-control-input");
	for (var i = 6; i<16; i++) {
		if(NSWckBox[i].checked == true){
			code = code.substr(0,i-6)+"1"+code.substr(i-6+1) //replace 0 with 1 if the column is checked

				//add google draw col
				if(NSWckBox[i].id == "swAUDaily"){
					data.addColumn('number', 'National Increased Daily');
				} else if (NSWckBox[i].id == "swAUTotal") {
					data.addColumn('number', 'National Total Confirmed');
				} else if (NSWckBox[i].id == "swNSWDaily2") {
					data.addColumn('number', 'NSW Increased Daily');
				} else if (NSWckBox[i].id == "swQLDDaily") {
					data.addColumn('number', 'QLD Increased Daily');
				}
				else if (NSWckBox[i].id == "swSADaily") {
					data.addColumn('number', 'SA Increased Daily');
				}
				else if (NSWckBox[i].id == "swVICDaily") {
					data.addColumn('number', 'VIC Increased Daily');
				}
				else if (NSWckBox[i].id == "swWADaily") {
					data.addColumn('number', 'WA Increased Daily');
				}
				else if (NSWckBox[i].id == "swTASDaily") {
					data.addColumn('number', 'TAS Increased Daily');
				}
				else if (NSWckBox[i].id == "swNTDaily") {
					data.addColumn('number', 'NT Increased Daily');
				}
				else if (NSWckBox[i].id == "swACTDaily") {
					data.addColumn('number', 'ACT Increased Daily');
				} else {
					var foo = 0;
				}
		}
	}
	//alert(code);
	
	var Data = $.ajax({
            url: "/AUcrossRF",
	    dataType: "json",
	    type: "GET",
	    data: {'data':code},
	    contentType: 'application/json',
	    async: false
	}).responseText;

	//draw figure	
	modal.style.display = "block";
	modal.style.visibility = "hidden";

	//var data = new google.visualization.DataTable();
	//data.addColumn('string', 'Date');

	

	data.addRows(JSON.parse(Data));

	var options = {
	};
	var chart = new google.charts.Line(document.getElementById('piechart'));
	chart.draw(data, options);

	modal.style.visibility = "visible";
}

function NSWCross(){
	var nswDailyCB = document.getElementById("swNSWDaily");
	var nswTotalCB = document.getElementById("swNSWTotal");
	var nswRecCB = document.getElementById("swNSWRecovery");
	var nswActCB = document.getElementById("swNSWActive");
	var nswTestCB = document.getElementById("swNSWTest");
	var nswDeathCB = document.getElementById("swNSWDeath");
	
	var jsonData = {NSWdaily:0, NSWtotal:0,NSWRec:0,NSWact:0,NSWtest:0,NSWdeath:0};
        if(nswDailyCB.checked == true){
		jsonData.NSWdaily = 1;
	} else {
		jsonData.NSWdaily = 0;
	}
	if(nswTotalCB.checked == true){
		jsonData.NSWtotal = 1;
	} else {
		jsonData.NSWtotal = 0;
	}
	if(nswRecCB.checked == true){
		jsonData.NSWRec = 1;
	} else {
		jsonData.NSWRec = 0;
	}
	if(nswActCB.checked == true){
		jsonData.NSWact = 1;
	} else {
		jsonData.NSWact = 0;
	}
	if(nswTestCB.checked == true){
		jsonData.NSWtest = 1;
	} else {
		jsonData.NSWtest = 0;
	}
	if(nswDeathCB.checked == true){
		jsonData.NSWdeath = 1;
	} else {
		jsonData.NSWdeath = 0;
	}

	modal.style.display = "block";
	modal.style.visibility = "hidden";

	//alert(JSON.stringify(jsonData));	
	//pass to server side prog
	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Date');
	for (var key in jsonData){
		if ((key == 'NSWdaily') && (jsonData[key] == 1)){
	//		alert('add NSWdaily');
			data.addColumn('number', 'NSW Daily Increased');
		}
		if ((key == 'NSWtotal') && (jsonData[key] == 1)){
	//		alert('add NSWtotal');
			data.addColumn('number', 'NSW Total Confirmed');
		}
		if ((key == 'NSWRec') && (jsonData[key] == 1)){
	//		alert('add NSWRec');
			data.addColumn('number', 'NSW Recovered');
		}
		if ((key == 'NSWact') && (jsonData[key] == 1)){
	//		alert('add NSWact');
			data.addColumn('number', 'NSW Active Cases');
		}
		if ((key == 'NSWtest') && (jsonData[key] == 1)){
	//		alert('add NSWtest');
			data.addColumn('number', 'NSW Daily Tested');
		}
		if ((key == 'NSWdeath') && (jsonData[key] == 1)){
	//		alert('add NSWdeath');
			data.addColumn('number', 'NSW Death');
		}
	}

	var Data = $.ajax({
		url: "/NSWcrossRF",
	    dataType: "json",
	    type: "GET",
	    data: {'data':JSON.stringify(jsonData)},
	    contentType: 'application/json',
	    async: false
	}).responseText;
	data.addRows(JSON.parse(Data));

	var options = {
	};
	var chart = new google.charts.Line(document.getElementById('piechart'));
	chart.draw(data, options);
	modal.style.visibility = "visible";
}

//check first 6 for NSW page tab
function sanitCK(){
	var cnt = 0;
	var NSWckBox = document.getElementsByClassName("custom-control-input");
	//for (var i = 0; i<NSWckBox.length; i++) {
	for (var i = 0; i<6; i++) {
		if(NSWckBox[i].checked == true){
			cnt = cnt + 1;
		}
	}
	if(cnt > 3){
		alert("Maximum checked number is 3.");
		for (var i = 0; i<NSWckBox.length; i++) {
			NSWckBox[i].checked = false;
		}
	}
}

//check 7 to 16 switch in AU page 2nd tab
function sanitCK2(){
	var cnt = 0;
	var NSWckBox = document.getElementsByClassName("custom-control-input");
	//for (var i = 0; i<NSWckBox.length; i++) {
	for (var i = 6; i<16; i++) {
		if(NSWckBox[i].checked == true){
			cnt = cnt + 1;
		}
	}
	if(cnt > 4){
		alert("Maximum checked number is 4.");
		for (var i = 0; i<NSWckBox.length; i++) {
			NSWckBox[i].checked = false;
		}
	}
}

function NSWTotal(){
	modal.style.display = "block";
	modal.style.visibility = "hidden";

	drawNSWTotalChart();
	modal.style.visibility = "visible";
}
function NSWRecovery(){
	modal.style.display = "block";
	modal.style.visibility = "hidden";

	drawNSWRecoveryChart();
	modal.style.visibility = "visible";
}
function NSWActive(){
	modal.style.display = "block";
	modal.style.visibility = "hidden";

	drawNSWActiveChart();
	modal.style.visibility = "visible";
}
function NSWTest(){
	modal.style.display = "block";
	modal.style.visibility = "hidden";

	drawNSWTestChart();
	modal.style.visibility = "visible";
}
function NSWDeath(){
	modal.style.display = "block";
	modal.style.visibility = "hidden";

	drawNSWDeathChart();
	modal.style.visibility = "visible";
}
function AUDaily(){
	modal.style.display = "block";
	modal.style.visibility = "hidden";

	drawAUDailyChart();
	modal.style.visibility = "visible";
}
function AUTotal(){
	modal.style.display = "block";
	modal.style.visibility = "hidden";

	drawAUTotalChart();
	modal.style.visibility = "visible";
}
function drawDaily(stateName){
	modal.style.display = "block";
	modal.style.visibility = "hidden";

	drawDailyChart(stateName);
	modal.style.visibility = "visible";
}

