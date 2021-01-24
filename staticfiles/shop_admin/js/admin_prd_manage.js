$(document).ready(function() {


    $(".product_delete").click(function(event) {
        event.preventDefault();
        var confirm_test = confirm("정말 삭제 하시겠습니까?????");
        if ( confirm_test == true ) {
            $(this).closest('tr').remove();
            if($('#tblParent tbody tr').length == 0){    //만약에 tbody 의 tr(상품개수)이 0개가 되면
                $('.no_data').css('display', 'block');   //상품이 없습니다의 디스플레이를 block 으로 변경!
            }
        } else if ( confirm_test == false ) {
            return false;
        }


      });















});