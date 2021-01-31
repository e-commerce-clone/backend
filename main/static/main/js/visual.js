'use strict';

const ul = document.querySelector('.promotions'); //html에서 ul을 가져옴
const firstIndexClone = ul.firstElementChild.cloneNode(true); //index1의 복사본
ul.appendChild(firstIndexClone); //ul의 가장 뒤에 복사본을 붙임

// visual.css의 ul의 총 너비를 4200에서 5250으로 변경

function move() {

	let curIndex = 0; //current Index

	setInterval(function(){ //setInterval  = 일정 간격으로 코드를 반복 실행하는 함수, {코드}, 시간간격(ms)
		ul.style.transition = '0.6s'; //0.2초에 걸쳐 객체 변화
		ul.style.transform = "translate3d(-"+1900*(curIndex+1)+"px, 0px, 0px)"; //translate3d = 현재위치에서 x, y, z축의 거리만큼 이동

		curIndex++; //index	1씩 증가

		//언제까지?
		if(curIndex === 4) { // 현재 index가 4인 경우,
			setTimeout(function(){ //시간지연함수 실행(일정 시간 후 특정 함수/코드를 지연한 뒤 실행)
				ul.style.transition = '0s'; //transition 삭제
				ul.style.transform = "translate3d(0px, 0px, 0px)"; //현재 위치에서 이동 없음
			}, 601) //복사본이 자리잡은 0.601초 뒤 transition, transform 끔
			curIndex = 0; //index 1로 되돌림
		} // 

	}, 3000); // 3초 간격 {코드} 실행
}

document.addEventListener("DOMContentLoaded", function(){ //문서의 로드시점을 DOMContentLoaded로 함. = onload 이벤트보다 먼저 발생하며, 빠른 실행속도가 필요할 때 적합
	move();
});
// 참고: https://takeknowledge.tistory.com/34