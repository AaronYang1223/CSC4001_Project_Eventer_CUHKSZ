<template>
  <v-app>
    <NavbarCom />

    <!-- load the actual code -->
    <v-content class="ma-2 pa-1">
      <router-view></router-view>
    </v-content>

  </v-app>
</template>

<script>
import NavbarCom from '@/components/NavbarCom'

export default {
  components: { NavbarCom },
  name: 'App',
  data() {
    return {

    }
  }
}
</script>
