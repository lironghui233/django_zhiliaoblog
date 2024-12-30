// 页面加载完毕执行下面函数
$(function () {
    function bindCaptchaBtnClick() {
        //根据id查找对象，绑定点击事件
        $("#captcha-btn").click(function (event) {

            //将js对象（DOM元素）转换为jquery对象
            let $this = $(this);

            //根据input标签的name查找对象
            let email = $("input[name='email']").val();
            if (!email) {
                alert("请先输入邮箱！");
                return;
            }

            // 取消按钮的点击事件
            $this.off('click')

            // 发送ajax请求，url只需填写path部分
            $.ajax('/auth/captcha?email='+email, {
                method:'GET',
                success: function (result){
                    if(result['code'] == 200){
                        alert("验证码发送成功！");
                    }else{
                        alert(result['message']);
                    }
                },
                fail: function (error){
                    console.log(error);
                }
            })

            // 倒计时
            let countdown = 60;
            let timer = setInterval(function () {
                if (countdown <= 0) {
                    $this.text('获取验证码');
                    //清理定时器
                    clearInterval(timer);
                    //重新绑定点击事件
                    bindCaptchaBtnClick();
                } else {
                    countdown--;
                    $this.text(countdown + "s")
                }
            }, 1000)
        })
    }

    bindCaptchaBtnClick();
})