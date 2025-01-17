 let profile = document.getElementById('profile');
 let profile_btn = document.getElementById('pro');

 let pro_value = '0'

 profile_btn.addEventListener('click', function(e){
    if(pro_value== '0'){
        profile.style.top='70px';
        pro_value = '1';
        console.log('working', pro_value)
    }else{
        profile.style.top='-400px';
        pro_value = '0';
        console.log('not working', pro_value)
    }
 })