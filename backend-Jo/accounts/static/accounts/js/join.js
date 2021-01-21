window.addEventListener('DOMContentLoaded',function(){     //시작


    // 변수 생성 
    const id_bell_f = document.querySelector('.id_bell_f');
    const id_bell_s = document.querySelector('.id_bell_s');
    const id_bell_t = document.querySelector('.id_bell_t');
    

    const pw_bell_f = document.querySelector('.pw_bell_f');
    const pw_bell_s = document.querySelector('.pw_bell_s');
    const pw_bell_t = document.querySelector('.pw_bell_t');
    // const pw_bell_u = document.querySelector('.pw_bell_u');  사용하려다가 그냥 안하는게 낫겠음 나중에 필요하면 주석해제 ( 동일한 숫자 3개 이상 연속 사용 불가 )
    

    const pw2_bell_f = document.querySelector('.pw2_bell_f');
    const pw2_bell_s = document.querySelector('.pw2_bell_s');


    const juso = document.querySelector('#juso');
    const user_address = document.querySelector('#user_address');
    const user_detail_address = document.querySelector('#user_detail_address');
    const juso_search = document.querySelector('.juso_search');

  


    juso.addEventListener('click', jusosearch);  // 주소 검색 클릭 하면 jusosearch() 함수 실행
    
    function jusosearch(){   //주소 검색 카카오 api 
        new daum.Postcode({
            oncomplete: function(data) {
                // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

                // 각 주소의 노출 규칙에 따라 주소를 조합한다.
                // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
                var addr = ''; // 주소 변수
                var extraAddr = ''; // 참고항목 변수

                //사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
                if (data.userSelectedType === 'R') { // 사용자가 도로명 주소를 선택했을 경우
                    addr = data.roadAddress;
                } else { // 사용자가 지번 주소를 선택했을 경우(J)
                    addr = data.jibunAddress;
                }

                // 사용자가 선택한 주소가 도로명 타입일때 참고항목을 조합한다.
                if(data.userSelectedType === 'R'){
                    // 법정동명이 있을 경우 추가한다. (법정리는 제외)
                    // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
                    if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                        extraAddr += data.bname;
                    }
                    // 건물명이 있고, 공동주택일 경우 추가한다.
                    if(data.buildingName !== '' && data.apartment === 'Y'){
                        extraAddr += (extraAddr !== '' ? ', ' + data.buildingName : data.buildingName);
                    }
                    // 표시할 참고항목이 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
                    if(extraAddr !== ''){
                        extraAddr = ' (' + extraAddr + ')';
                    }
                    // 조합된 참고항목을 해당 필드에 넣는다.
                    
                
                } else {
                    document.getElementById("sample6_extraAddress").value = '';
                }

                // 우편번호와 주소 정보를 해당 필드에 넣는다.
               
                document.getElementById("user_address").value = addr;
                // 커서를 상세주소 필드로 이동한다.
                document.getElementById("user_detail_address").focus();

                //주소 검색이 완료된 후 변하는 css 목록
                user_address.classList.add('on'); //선택한 주소 나오는 창 생성 
                juso_search.classList.add('on'); //주소 검색 쪽 height 키움
                user_detail_address.classList.add('on');  // 상세 주소 입력하게 나오는 창 생성
                juso.classList.add('on');    //주소검색 버튼 작게 만들기 on






                







                // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분입니다.
                // 예제를 참고하여 다양한 활용법을 확인해 보세요.
                // http://postcode.map.daum.net/guide  api주소 
            }
        }).open();
    }





    // 비밀번호 일치 불일치 확인하기

    $('.check_pw').focusout(function () {          //비밀번호 확인 칸에서 벗어났을 때 실행.
        var pwd1 = $(".inpt_pw").val();            //변수 생성후 값 대입
        var pwd2 = $(".inpt_pw2").val();           //변수 생성후 값 대입
 
        if ( pwd1 != '' && pwd2 == '' ) {          //둘다 빈칸일 경우 아무것도 하지 않음
            null;
        } else if (pwd1 != "" || pwd2 != "") {     // 빈칸이 아닐 경우
            if (pwd1 == pwd2) {                    // 비교해서 같으면
                $(".pw2_bell_s").css('color', '#0f851a');                 
                $(".pw2_bell_s").text("비밀번호가 동일합니다.");
            
                
            } else {        // 비교해서 같지 않으면
                $(".pw2_bell_s").css('color', '#b3130b');
                $(".pw2_bell_s").text("비밀번호가 일치하지 않습니다.");
                
                
            }
        }

        
    });


    




    //아이디 조건 만족 불만족 함수 생성
    function id_check(){
        var id = $(".inpt_id").val();             // 변수 id에  id값 대입

        // var num = /[0-9]/;
        // var eng = /[a-zA-Z]/;
        var spe = /[~!@#$%^&*()_+|<>?:{}]/;         
    


        if(id.length < 6){                     //만약에 id의 길이가 6보다 작으면
            $(".id_bell_s").css('color', '#b3130b');   //글자색 변경
            // $(".id_bell_s").text("6자 이상의 영문 혹은 영문과 숫자를 조합");
            return false;
        }else if(spe.test(id) == 1){    //spe.test(id) --> id안에 특수문자가 있으면 true반환 없으면 false반환
            $(".id_bell_s").css('color', '#b3130b');   //글자색 변경
            // $(".id_bell_s").text("6자 이상의 영문 혹은 영문과 숫자를 조합");
            return false;

        }else{          // 모든 조건이 일치하지 않다면  

            $(".id_bell_s").css('color', '#0f851a');  //글자색 초록색으로 변경
            return true;  //true값 반환
        }
       
    }


    //비밀번호 조건 만족 불만족 함수 생성
    function pw_check(){
        var pw = $(".inpt_pw").val();                   // 변수 pw에 pw값 대입

        var num = /[0-9]/;
        var eng = /[a-zA-Z]/;
        var spe = /[~!@#$%^&*()_+|<>?:{}]/;
    


        if(pw.length < 10){                                  //pw의 길이가 10 이하일 때
            $(".pw_bell_s").css('color', '#b3130b');
            // $(".pw_bell_s").text("10자 이상 입력해주세요.");
            return false;
        }

        if(pw.length >= 10){                                  //pw의 길이가 10 이상일 때
            $(".pw_bell_s").css('color', '#0f851a');
            // $(".pw_bell_s").text("성공!");
            
        }

        if(num.test(pw) == 0 || eng.test(pw) == 0 || spe.test(pw) == 0){    // pw의 숫자가 없거나 , 영어가 없거나, 특수문자가 없을경우 실패
            $(".pw_bell_t").css('color', '#b3130b');
            // $(".pw_bell_t").text("영문,숫자, 특수문자를 혼합하여 입력해주세요.");
            return false;
        }

        if(num.test(pw) == 1 && eng.test(pw) == 1 && spe.test(pw) == 1){ // pw의 숫자,영어,특수문자가 1개이상씩 있을경우 성공
            $(".pw_bell_t").css('color', '#0f851a');
            // $(".pw_bell_t").text("성공!");
            
        }
        // if(/(\w)\1\1/.test(pw)){
        //     $(".pw_bell_u").css('color', '#b3130b'); 
        //     $(".pw_bell_u").text("동일한 숫자 3개 이상 연속 사용 불가");
        //     return false;
        // }
        // if(!/(\w)\1\1/.test(pw)){
        //     $(".pw_bell_u").css('color', '#0f851a');
        //     $(".pw_bell_u").text("성공!");
            
        // }

        return true;
        }



    //아이디 조건 만족 불만족 확인하기
    var text1 = $('.inpt_id');
    text1.focus(function(){               //포커스 되면
        id_bell_f.classList.add('on');
        id_bell_s.classList.add('on');
        id_bell_t.classList.add('on');
      });
      text1.blur(function(){              //포커스에서 벗어나면
        
        id_check();              //id_check() 함수 실행
        
      });




    //비밀번호 조건 만족 불만족 확인하기
    var text2 = $('.inpt_pw');
    text2.focus(function(){                   //포커스 되면
        pw_bell_f.classList.add('on');
        pw_bell_s.classList.add('on');
        pw_bell_t.classList.add('on');
        // pw_bell_u.classList.add('on');  동일한 숫자 3개 이상 연속 사용불가 제외시켜버렸음
      });
      text2.blur(function(){              //포커스에서 벗어나면
        
        pw_check();                      //pw_check() 함수 실행
       
        
      });

    //비밀번호 확인 조건 만족 불만족
    var text3 = $('.inpt_pw2');
    text3.focus(function(){
        pw2_bell_f.classList.add('on');
        pw2_bell_s.classList.add('on');
      });
      text3.blur(function(){           // 여기 작성 할껄 위에 focusout 함수에 작성했음 
        
      });

    



    //아이디 중복체크
    const idjungbok = document.querySelector('#idjungbok');
    idjungbok.addEventListener('click', id_overlap_check); 

    function id_overlap_check() {

        $('.inpt_id').change(function () {
            $(".id_bell_t").css('color', '#b3130b');
            
            // $('.inpt_id').attr("check_result", "fail");
        })
    
    
        if ($('.inpt_id').val() == '') {
          alert('아이디를 입력해주세요');
          return;
        }
    
        id_overlap_input = document.querySelector('input[name="id"]');
    
        $.ajax({
          type: "GET",
          url: "./id_check?id="+id_overlap_input,    //해당 url로 데이터를 넘김
          data: {
            'username': $('.inpt_id').val()
          },
          datatype: 'json',
          success: function (data) {
            console.log(data['overlap']);
            if (data['overlap'] == "fail") {
              alert("이미 존재하는 아이디 입니다.");
              id_overlap_input.focus();
              return;
            } else {
              alert("사용가능한 아이디 입니다.");
              $(".id_bell_t").css('color', '#0f851a');
              return;
            }
          }
        });
    }




    //이메일 중복체크
    const emailjungbok = document.querySelector('#emailjungbok');
    emailjungbok.addEventListener('click', email_overlap_check);

    function email_overlap_check() {

        // $('.inpt_email').change(function () {
            
        // })
    
    
        if ($('.inpt_email').val() == '') {
          alert('이메일을 입력해주세요');
          return;
        }
    
        email_overlap_input = document.querySelector('input[name="email"]');
    
        $.ajax({
          type: "GET",
          url: "./email_check?id="+email_overlap_input,    //해당 url로 데이터를 넘김
          data: {
            'email': $('.inpt_email').val()
          },
          datatype: 'json',
          success: function (data) {
            console.log(data['overlap']);
            if (data['overlap'] == "fail") {
              alert("이미 존재하는 이메일 입니다.");
              email_overlap_input.focus();
              return;
            } else {
              alert("사용가능한 이메일 입니다.");
              return;
            }
          }
        });
    }
    






      
    


});

