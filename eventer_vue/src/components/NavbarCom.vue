<template>
  <nav>

    <v-toolbar app>
      <v-app-bar-nav-icon @click="drawer = !drawer" class="primary--text"></v-app-bar-nav-icon>
      <v-toolbar-title class="text-uppercase primary--text">
        <span class="font-weight-light">e</span>
        <span>venter</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon color="primary" @click="toggleTheme">
        <v-icon right>mdi-theme-light-dark</v-icon>
      </v-btn>
      <v-btn icon color="primary">
        <v-icon right>mdi-logout</v-icon>
      </v-btn>
    </v-toolbar>
    <!-- 之后会改成Avatar -->
    <v-navigation-drawer app v-model="drawer" class="primary">
      <p>test</p>
    </v-navigation-drawer>

  </nav>
</template>

<script>
export default {
  data() {
    return {
      // 控制侧边栏
      drawer: false
    }
  },
  methods:{
    toggleTheme(){
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark
    }
  }
}
</script>

<style>
</style>
