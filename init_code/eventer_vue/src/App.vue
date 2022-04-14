<template>
  <v-app>
    <NavbarCom v-if="this.$store.state.hasLogin"></NavbarCom>
    <!-- load the actual code -->
    <v-content class="ma-2 pa-1">
      <router-view></router-view>
    </v-content>

  </v-app>
</template>

<script>
import NavbarCom from '@/components/NavbarCom'

export default {
  components: { NavbarCom},
  name: 'App',
  data() {
    return {

    }
  },

  // created () {
  //   console.log("nihao");


  //   console.log('页面执行刷新时,保存Vuex的状态到LocalStorage')
  //   //在页面加载时读取localStorage里的状态信息
  //   localStorage.getItem("userMsg") && this.$store.replaceState(Object.assign(this.$store.state.hasLogin,JSON.parse(localStorage.getItem("userMsg"))));
  //   console.log(this.$store.state)
  //   //在页面刷新时将vuex里的信息保存到localStorage里
  //   window.addEventListener("beforeunload",()=>{
  //       console.log(this.$store.state.hasLogin)
  //       localStorage.setItem("userMsg",JSON.stringify(this.$store.state.hasLogin))
  //   })

  //   console.log(this.$store.state.hasLogin)

  // }


}
</script>
