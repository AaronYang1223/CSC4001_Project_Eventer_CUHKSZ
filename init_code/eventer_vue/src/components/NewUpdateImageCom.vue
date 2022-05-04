//upload组件里的代码
<template>
  <div class="avatar">
    <v-container>
        <v-card
        flat
        outlined
        class="hidden-sm-and-down"
        tile
        >

          <v-list-item-content class="justify-center">

            <v-avatar
              size="200"
            >
              <img :src="avatar">
            </v-avatar>          

            <div class="text-center mt-4">

              <v-btn
                style="width:150px; height:25px;" 
                color="primary"
                tile
              >
                <v-icon small>mdi-pencil</v-icon>
                <span>avatar</span>

                <input
                  type="file" 
                  class="input-file" 
                  style="width:200px; height:20px;" 

                  ref="avatarInput" 
                  @change="changeImage($event)" 
                  accept="image/gif,image/jpeg,image/jpg,image/png"
                >

              </v-btn>

            </div>

          </v-list-item-content>
        </v-card>
                
                
        <v-card
        flat
        outlined
        class="hidden-md-and-up"
        tile
        >

          <v-list-item-content class="justify-center">

            <v-avatar
              size="150"
            >
              <img :src="avatar">
            </v-avatar>          

            <div class="text-center mt-4">

              <v-btn
                style="width:120px; height:25px;" 
                color="primary"
                depressed
                tile
              >

                <v-icon small>mdi-pencil</v-icon>
                <span>Edit avatar</span>

                <input
                  type="file" 
                  class="input-file" 
                  style="width:200px; height:20px;" 

                  ref="avatarInput" 
                  @change="changeImage($event)" 
                  accept="image/jpg,image/png"
                >

              </v-btn>

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
      user_id: '',
    }
  },

  props: ["uploadType", "imgWidth", "imgHeight"],

    created(){
      this.$axios.get('http://127.0.0.1:8000/api/activity/order/comment_number/all').then(response => {
        console.log(response.data)
        this.avatar = this.$store.state.avatar
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
      this.$axios.post('http://127.0.0.1:8000/api/profile/upload/'+ this.$store.state.userID, data
      ).then(response => {
        console.log(response.data)
        this.avatar = 'http://127.0.0.1:8000'+response.data['picture']
        this.$axios.get('http://127.0.0.1:8000/api/activity/order/comment_number/all').then(response => {
        console.log(response.data)
        this.$store.commit("userAvatarUpdate", this.avatar);
        //this.avatar = this.$store.state.avatar;
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
        position: absolute;
        top: 0;
        left: 0;
        opacity: 0;
        cursor: pointer;
    }
    .v-btn__content {
      white-space: normal;
    }
}
</style>
