<template>
  <div class="home">
    <h1>Homepage</h1>
    <v-btn @click="test">
    </v-btn>
    <v-btn @click="no">
      注销
    </v-btn>
    {{userid}}<br/>
    {{islogin}}
  </div>
</template>

<script>


export default {
  data() {
    return {
      userid: "",
      islogin: false,
    }
  },
  name: 'HomeView',
  methods: {
    test: function(){
      this.islogin = this.$store.state.hasLogin;
      this.userid = this.$store.state.msg;
    },
    no: function(){
      this.islogin = this.$store.state.hasLogin;
      this.userid = this.$store.state.msg;
      this.$store.commit("logoutUpdate");
      console.log("cnm")
      console.log(this.$store.state.hasLogin);
      window.location.href = "/";
    }
  },
}
</script>
