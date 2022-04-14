<template>
  <nav>

    <v-toolbar app>
      <!-- <v-menu
        bottom
        min-width="200px"
        rounded
        offset-y
      > -->

      <!-- 设置为按钮是为了留一个刷新键 -->
      <v-btn class="text-uppercase primary--text" x-large text>
        <h1 class="font-weight-light">e</h1>
        <h1>venter</h1>
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn 
        tile 
        @click="goLogin" color="primary"
        depressed
      >
        Login
      </v-btn>
      <v-divider
        class="mx-4"
        vertical
      ></v-divider>
      <v-btn 
        tile 
        @click="goOther"
        depressed
      >
        {{toPage}}
      </v-btn>
      <!-- </v-menu> -->
    </v-toolbar>

  </nav>
</template>

<script>
export default {
  props: ['Page'],
  data() {
    return {
      toPage: "",
      toPath: "",
    }
  },
  created() {
    if (this.Page.isPage == "signin") {
      this.toPage = "Forget Password"
      this.toPath = "/forget"
    }
    if (this.Page.isPage == "forget") {
      this.toPage = "Sign In"
      this.toPath = "/signin"
    }
  },
  methods:{
    goLogin(){
      window.location.href = "/login";
    },
    goOther(){
      window.location.href = this.toPath;
    },
  }

}
</script>

<style>
</style>
