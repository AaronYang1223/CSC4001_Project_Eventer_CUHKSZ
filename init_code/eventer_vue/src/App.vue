<template>
  <v-app>
    <NavbarCom v-if="this.$store.state.hasLogin"></NavbarCom>
    <!-- load the actual code -->
    <!-- Only show the bar when login -->
    <v-content>
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

}
</script>
