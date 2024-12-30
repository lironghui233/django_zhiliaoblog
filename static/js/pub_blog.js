// 整个页面加载完毕才执行
window.onload = function () {
    const {createEditor, createToolbar} = window.wangEditor

    const editorConfig = {
        placeholder: 'Type here...',
        onChange(editor) {
            const html = editor.getHtml()
            console.log('editor content', html)
            // 也可以同步到 <textarea>
        },
    }

    const editor = createEditor({
        selector: '#editor-container',
        html: '<p><br></p>',
        config: editorConfig,
        mode: 'default', // or 'simple'
    })

    const toolbarConfig = {}

    const toolbar = createToolbar({
        editor,
        selector: '#toolbar-container',
        config: toolbarConfig,
        mode: 'default', // or 'simple'
    })

    // 根据id获取对象
    $("#submit-btn").click(function (event) {
        // 阻止按钮的默认行为
        event.preventDefault();

        // 根据input标签和name属性获取对象
        let title = $("input[name='title']").val();
        // 根据id获取对象
        let category = $("#category-select").val();
        // 根据wangEditor提供的对象获取 富文本内容
        let content = editor.getHtml();
        // 根据input标签和name属性获取对象
        let csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();

        // 发送ajax请求，url只需填写path部分
        $.ajax('/blog/pub', {
            method: 'POST',
            data: {
                title,
                category,
                content,
                csrfmiddlewaretoken
            },
            success: function (result) {
                if(result['code']==200){
                    // 获取博客id
                    let blog_id = result['data']['blog_id']
                    // 跳转到博客详情页面
                    window.location = '/blog/detail/' + blog_id
                }else{
                    alert(result['message']);
                }
            },
            error: function () {

            }
        })
    })
}