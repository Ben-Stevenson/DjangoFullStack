$(document).ready(function()) {
	//JQuery code to be added in here.
	$('#suggestion').keyup(function(){
		var query;
		query = $(this).val();
		$.get('/topper/suggest/', {suggestion: query}, function(data){
			$('#albums').html(data);
		});
	});
}};