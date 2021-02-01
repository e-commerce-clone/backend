$(document).ready(function(){
      //비밀번호 조건 만족 불만족 확인하기
      var text_pw = $('#newPassword');
      text_pw.focus(function(){               //포커스 되면
          $('.find_view .pw_chk').css('display', 'block');
      });
      text_pw.blur(function(){              //포커스에서 벗어나면
          
          pw_check();              //pw_check() 함수 실행    
      });


       //비밀번호확인 조건 만족 불만족 확인하기
       var text_pw2 = $('#confirmPassword');
       text_pw2.focus(function(){               //포커스 되면
           $('.find_view .pw2_chk').css('display', 'block');
       });
       text_pw2.blur(function(){              //포커스에서 벗어나면
           
           pw2_check();              //pw2_check() 함수 실행    
       });




});