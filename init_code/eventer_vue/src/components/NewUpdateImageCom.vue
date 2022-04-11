//upload组件里的代码
<template>
  <div class="avatar">
    <input 
      type="file" 
      class="input-file" 
      :style="`width:${imgWidth};height:${imgHeight};`" 
      name="avatar" 
      ref="avatarInput" 
      @change="changeImage($event)" 
      accept="image/gif,image/jpeg,image/jpg,image/png"
    >
    <img 
      :src="avatar?avatar:require('../assets/logo.png')" 
      alt="" 
      :style="`width:${imgWidth};height: ${imgHeight};`" 
      name="avatar"
    >
    <div class="text" @click="upload" v-if="file">确定上传</div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      avatar: '',
      file: '',
      user_id: 1,
    }
  },

  props: ["uploadType", "imgUrl", "imgWidth", "imgHeight"],

    created(){
      this.$axios.get('http://127.0.0.1:8000/api/activity/order/comment_number/all').then(response => {
        console.log(response.data)
        this.avatar = 'http://127.0.0.1:8000' + response.data[this.user_id-1].picture
      })
    },

  methods: {
  //changeImage
    changeImage: function(e){
      let file = e.target.files[0];
      if(file) {
        this.file = file
        console.log(this.file)
        let reader = new FileReader()
        let that = this
        reader.readAsDataURL(file)
        reader.onload= function(){
          // 这里的this 指向reader
          that.avatar = this.result
        }
      }
    },

    upload: function(){
      let files = this.$refs.avatarInput.files
      let fileData = {}
      //make sure only update one file
      if(files instanceof Array) {
        fileData = files[0]
      } else {
        fileData = this.file
      }
      console.log('fileData', typeof fileData, fileData)
      let data = new FormData()
      data.append('picture', fileData)
      data.append('operaType', this.uploadType)
      console.log('data', typeof data, data)
      this.$axios.post('http://127.0.0.1:8000/api/profile/upload/1', data
      ).then(response => {
        console.log(response.data)
        this.$axios.get('http://127.0.0.1:8000/api/activity/order/comment_number/all').then(response => {
        console.log(response.data)
        this.avatar = 'http://127.0.0.1:8000' + response.data[this.user_id-1].picture
      })
      })

    }
  }
}
</script>

<style lang="less" scope>
.avatar {
    cursor: pointer;
    position: relative;
    .input-file {
        position: absolute;
        top: 0;
        left: 0;
        opacity: 0;
        cursor: pointer;
    }
    .bg {
        width: 100%;
        height: 100%;
        color: #fff;
        background-color: rgba(0,0,0,0.3);
        text-align: center;
        cursor: pointer;
        position: absolute;
        top: 0;
        left: 0;

    }
    .text {
        padding-top: 10px;
        color: lightblue;
    }
}
</style>