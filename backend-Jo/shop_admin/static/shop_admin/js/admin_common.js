$(document).ready(function() {



    var floatPosition = parseInt($(".snb_my").css('top')); //관리자 메뉴의 css top위치를 가져와서 변수에다가 넣어줌
    var bottomscoll = $(document).height() - $(window).height();  //최 하단의 scrollTop 구하는 공식임  문서의 높이 - 브라우저창 높이  (문서의높이 : 페이지전체의 높이   브라우저창 높이: 모니터에보이는 브라우저 높이)

    $(window).scroll(function(){
        
        

        var scrollTop = $(window).scrollTop();  // 변수 scrollTop에다가  브라우저 상단좌표를 넣어줌
        var newPosition = scrollTop + floatPosition + "px"; //새로운위치를 지정할변수에다가 브라우저 상단좌표 + 관리자메뉴의위치를 더해줌


        

        if(scrollTop > bottomscoll-200){ //푸터 쪽으로 못내려오게 return false를 줬음 
            return false;
        }
    
            
    
        $(".snb_my").stop().animate({
             "top" : newPosition      //관리자메뉴의 탑 위치를 새로운위치변수로 바꿔줌
        }, 500);  //여기서 500은 속도
    




       





    });



    





});