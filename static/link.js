	window.onload = function() {
	var kij = "http://www.kijiji.ca"; 
	var wheels = "http://vehicles.wheels.ca";
	var carpages = "https://www.carpages.ca";  
	
	var kiarr = document.querySelectorAll('a.title');
	var wharr = document.querySelectorAll('a.ListingRowHeadTxt'); 
	var cparr = document.querySelectorAll('a'); 



	for(var i = 0; i < cparr.length; ++i) {
		cparr[i].href = carpages + cparr[i].href.substring(21); 
	}

	for (var i = 0; i < kiarr.length; i++) {
    	kiarr[i].href = kij + kiarr[i].href.substring(23);
	}

	for (var i = 0; i < wharr.length; ++i) {
		wharr[i].href = wheels + wharr[i].href.substring(23); 
	}
		$("img.lazy").each(function() {
		$(this).attr("src", $(this).attr("data-original"));
	
	
	}
		var val = document.getElementsByClassName('switch');
	val[0].href = "https://ca.linkedin.com/in/shayon-banerjee-b61233b9";

	);
	var cpages = "http://www.carpages.ca";
	var arr = document.getElementsByClassName('lazy');
	for (var i = 0; i < arr.length; ++ i) {
		arr[i].src = cpages + arr[i].src.substring(21);
	
}
