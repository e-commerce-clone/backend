window.addEventListener('DOMContentLoaded',function(){

    const top_event_close= document.querySelector('.top_event_close');


    
    top_event_close.addEventListener('click', close);

    
    function close(){
       
        $("#top_event").slideUp(200)
    }

    



});