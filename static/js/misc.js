//Handle registration form

$(function(){
	$("body").height($(window).height());
console.log($('body').height());

	$('#registerForm').submit(function(e){
	e.preventDefault();
	$('#error_username').text("");
	$("#error_password").text("");
	$('#error_email').text("");
	var token = $("input[name='csrfmiddlewaretoken']").val();
	var username = $("#id_username").val().trim();
	var password = $("#id_password").val().trim();
	var email = $("#id_email").val().trim();
	$.ajax({
		url:"/registerUser/",
		method:"POST",
		data:{"csrfmiddlewaretoken":token,"email":email,"username":username,"password":password},
		success:function(response){
			if(response.status == "ok")
				$('.alert-message').show();
			else{
				$('.alert-message').hide();
				if(response.username != undefined)
					$('#error_username').text(response.username)

				if(response.email != undefined)
					$('#error_email').text(response.email)

				if(response.password != undefined)
					$('#error_password').text(response.password)
			}
		},
		error:function(response){
			console.log(response)
		}

	})
});

});


//Handle registration form

$(function(){
	$('#loginForm').submit(function(e){
	e.preventDefault();
	$('#error_username').text("");
	$("#error_password").text("");
	var token = $("input[name='csrfmiddlewaretoken']").val();
	var username = $("#id_username").val().trim();
	var password = $("#id_password").val().trim();
	$.ajax({
		url:"/authUser/",
		method:"POST",
		data:{"csrfmiddlewaretoken":token,"username":username,"password":password},
		success:function(response){
			console.log(response)
			if(response.status != undefined)
			{
				if(response.status == "ok")
					window.location.replace("/")
				else
					$('.alert-message').show();
			}
			else{
				$('.alert-message').hide();
				if(response.username != undefined)
					$('#error_username').text(response.username)

				if(response.password != undefined)
					$('#error_password').text(response.password)
			}
		},
		error:function(response){
			console.log(response)
		}

	})
});

});