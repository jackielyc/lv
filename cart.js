// alert("cart")

// var sleep = function(time) {
//     var startTime = new Date().getTime() + time*1000;
//     while(new Date().getTime() < startTime) {}
// };


var find_and_click = function(item_id) {
    console.log("start")
    i = 0;
    while(i<10) {
        i++
        if(document.getElementById(item_id)) 
        { 
            document.getElementById(item_id).click()
            break;
        }    
        console.log("loop")
        sleep(1);
    }
    console.log("stop")

}

find_and_click("proceedToCheckoutButton")

// window.onload = doIt; 
// function doIt() { 
//     $(document).ready(function () { 
//         console.log("onload")
//         if (document.getElementById("addToCartSubmit"))
//         { 
//             console.log("buy")
        
//             //1.放入购物袋
//             find_and_click("addToCartSubmit")

//             window.location.href="https://secure.louisvuitton.cn/zhs-cn/cart"

//             // //2.打开购物袋
//             // find_and_click("header-shoppingBag")


//             // //3.立即结账
//             // find_and_click("viewTaxesAndDetails")


//             // //4.提交
//             // find_and_click("proceedToCheckoutButton")

//             // //5.提交
//             // find_and_click("globalSubmit")

//             // //6.打钩
//             // find_and_click("acceptTerms")


//             // //7.提交订单
//             // find_and_click("globalSubmit")


        
//         }else{

//             // window.onload = function(){console.log("ready")};
//             console.log("reload")
//             // sleep(30);
//             location.reload(true);

//         } 
//     }
//     );
// }


