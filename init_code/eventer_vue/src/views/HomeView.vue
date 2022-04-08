<template>
  <div>
      <form @submit.prevent="onUpload">
          <div class="form-group">
              <input type="file" name="imagesArray" @change="onChange">
          </div>
          <div class="form-group">
              <button class="btn btn-success">Submit</button>
          </div>
      </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
      return {
         imagesArray: null
      };
    },
    methods: {
        onChange (event) {
          this.imagesArray = event.target.files[0]
        },
        onUpload() {
          const formData = new FormData()
          formData.append('imagesArray', this.imagesArray, this.imagesArray.name)
          axios.post('http://localhost:8888/api/activity/upload/1', formData, {
          }).then((response) => {
            console.log(response)
          })
        }  
    }

}
</script>

<style scoped lang="css">
.container {
  max-width: 500px;
}
</style>