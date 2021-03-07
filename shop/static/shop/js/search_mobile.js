

// 장바구니
const list_goods = document.querySelector('.search_list'),
      li = list_goods.querySelectorAll('.list_item'),
      rate = list_goods.querySelector('.dc'),
      cartPut_button = list_goods.querySelectorAll('.btn_cart'),
      cart_type3 = document.querySelector('.cart_type3'),
      bg_loading = document.querySelector('.bg_loading'),
      cartPut = document.querySelector('#cartPut'),
      cartPut_name = cartPut.querySelector('.name'),
      cartPut_dc_price = cartPut.querySelector('.dc_price'),
      cartPut_ori_price = cartPut.querySelector('.original_price'),
      cartPut_sum_price = cartPut.querySelector('.num'), //dc_price의 합계
      
      cartPut_point = cartPut.querySelector('.emph'),
      cancel = cartPut.querySelector(".txt_type"),
      button_up = cartPut.querySelector(".up"),
	    button_down = cartPut.querySelector(".down"),
      count = cartPut.querySelector(".inp");


let product_name = [];  //상품명 리스트
let product_price = []; //상품 (할인) 가격 리스트
let product_origin_price = []; //원가 리스트
let product_value = []; //상품 갯수 바뀔 때 필요한 value값 리스트

  for (i=0; i<li.length; i++){           // 리스트 값에 저장해주는 반복문
    product_name[i] = li[i].querySelector(".name"); //li 상품 이름
    product_price[i] = li[i].querySelector(".price"); // li 상품 (할인) 가격
    product_origin_price[i] = li[i].querySelector('.original'); // li 원가
    product_value[i] = li[i].querySelector(".value").value; // 상품 갯수 바뀔 때 필요한 value
  }
  
  
  for (let i = 0; i < li.length; i++) {    // 클릭했을 때 그 인덱스 맞는 값을 넣어주는 반복문
    
    (function(idx) {
        cartPut_button[idx].onclick = function() {
                if (li[idx].querySelector('.dc') === null) { //li에게 할인율이 없다면
                  cartPut_ori_price.style = 'display: none'; //cartPut에서 원가 삭제
                } else {
                  cartPut_ori_price.innerHTML = product_origin_price[idx].innerHTML; //carPut에 원가 체크 후 있으면 보이게, 없으면 안보이게.
                  cartPut_ori_price.style = 'display: inline';
                
                };

                cart_type3.classList.add('show');
                bg_loading.classList.add ('show');
                document.body.classList.add ('fixed_bg');
                cartPut_name.innerHTML = product_name[idx].innerHTML;
                cartPut_dc_price.innerHTML = product_price[idx].innerHTML;
                cartPut_sum_price.innerHTML = product_price[idx].innerHTML;
                cartPut_point.innerHTML = Math.round(Number(((product_value[idx] * 1)*0.005))).toLocaleString('ko')+'원 적립';
                //Math.round() :소수점 반올림, 정수형 변환
                // Number().toLocaleString('ko'): 숫자의 사용 언어에 따른 문자열 반환
            
                
  
                var k = 1
                button_up.addEventListener('click', function(){   // 수량 올리기 버튼 클릭 함수
                  k++;
                  count.value = k;
                  cartPut_sum_price.innerHTML = Math.round(Number((product_value[idx] * k))).toLocaleString('ko');
                  cartPut_point.innerHTML =  Math.round(Number((product_value[idx] * k)*0.005)).toLocaleString('ko')+'원 적립';
                
                });
              
                button_down.addEventListener('click', function(){  // 수량 내리기 버튼 클릭 함수
                  if (k > 0){
                    k--;
                    count.value = k;
                    cartPut_sum_price.innerHTML = Math.round(Number((product_value[idx] * k))).toLocaleString('ko');
                    cartPut_point.innerHTML =  Math.round(Number(((product_value[idx] * k)/20))).toLocaleString('ko')+'원 적립';
                  }
                });
              
                cancel.addEventListener('click', function(){   // 취소버튼 클릭시 사라지게 하는 반복문
                
                  cart_type3.classList.remove('show');
                  bg_loading.classList.remove('show');
                  document.body.classList.remove ('fixed_bg');
                  count.value = 1;
                  k = 1;

                
                });
        
        }
  
    })(i);
  }

  // 로딩 시 3초간 안내메세지
  const location_status = document.querySelector('.location_status');
  window.addEventListener('load', function() {
      location_status.classList.add('active');
      setTimeout(function() {
          location_status.classList.remove('active');
      }, 3000);
  });



