//upload组件里的代码
<template>
  <div class="avatar">
    <v-container>
        <v-card
        flat
        outlined
        >
          <v-list-item-content class="justify-center">

          <v-avatar
            size="200"
          >
            <img :src="avatar">
          </v-avatar>

        <div class="text-center">
          <div class="mt-4">
          <v-btn
            :style="`width:${imgWidth};height:${imgHeight};`" 
            max-width="200"
            text
          >
            <input 
              type="file" 
              class="input-file" 
              :style="`width:${imgWidth};height:${imgHeight};`" 

              ref="avatarInput" 
              @change="changeImage($event)" 
              accept="image/gif,image/jpeg,image/jpg,image/png"
            >
            

          </v-btn>
          </div>
        </div>


          </v-list-item-content>
        </v-card>
    </v-container>
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

  props: ["uploadType", "imgWidth", "imgHeight"],

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
        this.upload() 
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
    position: relative;
    .input-file {
        position: relative;
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