console.log("Hellllll")

/*var inp=document.getElementById('profile_img')

inp.addEventListener('change', function() {
  	console.log("Files: ",this.value)
	  if (this.files && this.files[0]) {

	      var img_path = URL.createObjectURL(this.files[0]);

	      var img = document.getElementById('profile-pic');

	      img.onload = function() {
    		// no longer need to read the blob so it's revoked
   	 		URL.revokeObjectURL(img.src);
  		  };
	      img.src=img_path;


	      var canvas = document.createElement('canvas');
	      canvas.setAttribute('width',img.width);
	      canvas.setAttribute('height',img.height);
	      var context = canvas.getContext('2d');
	      context.drawImage(img,0,0);


	      /*var c=document.getElementById('myCanvas');
	      	      	      	      var ctx = c.getContext("2d");
	      	      	      		  ctx.drawImage(img, 0, 0);
	      	      	      		  console.log("Canvas: ",ctx);*/



function updateProfileImage(img_path,user)
{
	console.log('Function Called Successfully: ',img_path,user);

	var url='/updateProfileImage/'

	const csrftoken=getToken('csrftoken')

	fetch(url,{
		method: 'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({'img_path':img_path,'user':user})
	})

	.then((response) => {
		//console.log("Response: ",response.json())
		return response.json()
	})

	.then((data) => {
		console.log('Trigger: ',data)
		//location.reload()
	})
}


function getToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


var inp = document.getElementById('inputGroupFile01');

inp.addEventListener('change', function() {
	console.log("Files: ",this.files);
})


var cover = document.getElementById('inputGroupFile01');
cover.addEventListener('change', function() {
	console.log('Label1');
	var label=document.getElementById('label01');
	if(this.files && this.files[0])
	{
		label.innerHTML=this.files[0].name;
	}
	else
	{
		label.innerHTML="Choose Cover Image";
	}
})

var profile = document.getElementById('inputGroupFile02');
profile.addEventListener('change', function() {
	console.log('Label1');
	var label=document.getElementById('label02');
	if(this.files && this.files[0])
	{
		label.innerHTML=this.files[0].name;
	}
	else
	{
		label.innerHTML="Choose Profile Image";
	}
})