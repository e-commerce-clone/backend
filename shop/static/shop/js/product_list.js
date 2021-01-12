window.addEventListener('DOMContentLoaded',function(){ 





    $(document).ready(function() {

        var noBody = $('.noBody');









        $('.btn').click(function(){

            $('#cartPut').css('display','block');
            $('.bg_loading').css('display','block');


           
            noBody.addClass('noBody_on');
            
            
        });



        $('.btn_type2').click(function(){
            $('#cartPut').css('display','none');
            $('.bg_loading').css('display','none');

            noBody.removeClass('noBody_on');
            ///// 닫기 눌렀으면 원래값으로 초기화 시켜줘야됨 ////
            number = 1;
            $('.inp').val(1); 
            $(".num").text(Math.floor(number*cost/1000) + ',' + number*cost%1000);
            $('.emph').text((number*cost)/20 + '원 적립');

            
        });

        var number = $('.inp').val();   //수량
        var cost = 1300;   // 상품의 가격을 설정해줘야됨.

        $('.down').click(function(){
            if(number > 0){
                number--;
                $(".inp").val(number);
                if(number == 0){               // 0원이면 0출력
                    $(".num").text(0);
                }
                else if((number % 10) == 0){
                    
                    $(".num").text(Math.floor(number*cost/1000) + ',' + '000');
                }
                else{
                
                $(".num").text(Math.floor(number*cost/1000) + ',' + number*cost%1000);
                }
            }

            if(number < 0){             //0 이하면 false 반환
                return false;
            }


            $('.emph').text((number*cost)/20 + '원 적립');
            
           
            
            
        });



        $('.up').click(function(){
            number++;
            $(".inp").val(number);
            if((number % 10) == 0){
                $(".num").text(Math.floor(number*cost/1000) + ',' + '000');
            }

            else{
                $(".num").text(Math.floor(number*cost/1000) + ',' + number*cost%1000);
                

            }



            
            $('.emph').text((number*cost)/20 + '원 적립');
            

            
        });

        

        $('.name_select').click(function(){
            $(".checked").toggle(function(){
                $('.name_select').css('color', '#5f0080');
            });
        });



        




        
        






       

























    });





});