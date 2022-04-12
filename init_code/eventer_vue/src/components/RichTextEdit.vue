<template>
  <div>
    <div class="tinymce-editor">
      <div id="tinymceToolbar"></div>
      <vue-tinymce
        ref="editor"
        class="editor overflow-scroll"
        v-model="content"
        :setting="setting" 
        :setup="setup"
        @keyup.native="$emit('editorChange', content)"
        @change="HtmlToText"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'tinymceEditor',
  components: {
  },
  data() {
    return {
      // 编辑器内容
      text: "yyy",
      content: '',
      // 编辑器设置
      setting: {
        inline: true,  // 设置内敛模式
        menubar: false, // 隐藏菜单栏
        toolbar:
          'code undo redo restoredraft cut copy paste pastetext | forecolor backcolor bold italic underline strikethrough link | alignleft aligncenter alignright alignjustify outdent indent lineheight| \
    　　　　styleselect formatselect fontselect fontsizeselect | bullist numlist | blockquote subscript superscript removeformat | \
    　　　　table image emoticons hr pagebreak insertdatetime preview ',
           // 工具栏，根据需要写对应的工具名称，顺序及分割线等等，这里的最后的 ‘myUpload’ 是下面setup里的自定义插件
        toolbar_mode: 'sliding', // 工具栏模式，这里是滑行模式（当屏幕过小时，多余的工具会隐藏，点击更多按钮会出现其他工具，这里配置出现的特效）
        plugins: 'preview image link code table pagebreak insertdatetime emoticons',// 需要用到的功能插件，如链接，列表等等
        // language: 'zh_CN', // 语言，汉化
        branding: false, // 隐藏品牌，隐藏状态栏中显示的“ Powered by Tiny ”链接
        resize: false, // 是否可以缩放编辑器
        elementpath: false, // 在编辑器底部的状态栏中禁用元素路径。
        fixed_toolbar_container: '#tinymceToolbar', // 可以设置元素选择器指定工具栏嵌套在哪个元素里面
        custom_ui_selector: 'body', // 聚焦的元素
        noneditable_noneditable_class: 'mceNonEditable', // 使用此选项，您可以指定TinyMCE将使用的类名称，以确定使用noneditable插件时可编辑哪些内容区域。主要用入你想以代码的形式添加某些内容，并给这些内容设置类名，使他们不可编辑，只能整个删除
        init_instance_callback: editor => {
          editor.focus() // 初始化聚焦，让内联模式的编辑器工具显示
        },
      },
    }
  },
  methods: {
    /**
     * @description: 编辑器setup
     * @author: Depp_ck
     */
    HtmlToText: function() {
      this.text = this.content;
      this.text = this.text.replace(/<\/?.+?>/g, "");
      this.text = this.text.replace(/&nbsp;/g, "");
    },
    // setup(editor) {
    //     // 自定义插件实现自定义工具栏按钮功能
    //     // 把myUpload加进toolbar里
    //   editor.ui.registry.addButton('myUpload', {
    //     tooltip: '上传',
    //     icon: 'browse',
    //     onAction: () => {
    //       console.log('点击了上传')
    //     },
    //   })
    // },
  },
}
</script>

<style lang="scss" scoped>
.tinymce-editor {
  padding: 20px;
  position: relative;
  .editor {
    padding: 10px;
    border: 1px solid #ddd;
    height: 410px;
    font-size: 16px;
    line-height: 1.4;
    overflow-y: scroll;
  }
}
</style>
