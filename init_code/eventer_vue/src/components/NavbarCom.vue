<template>
  <nav>

    <v-toolbar app>
      {{fresh()}}
      <v-menu
        bottom
        min-width="200px"
        rounded
        offset-y
      >
        <template v-slot:activator="{ on }">
          <v-btn
            icon
            x-large
            v-on="on"
          >
            <v-avatar
              size="48"
            >
              <img :src= "user.avatar">
            </v-avatar>
          </v-btn>
        </template>

        <v-card>
          <v-list-item-content class="justify-center">
            <div class="mx-auto text-center">
              <h3 color="grey darken-1">{{ user.fullName }}</h3>
              <p class="text-caption mt-1" color="grey darken-1">
                {{ user.email }}
              </p>

              <v-divider class="my-3"></v-divider>

              <v-btn
                text
                color="grey darken-1"
                plain
                router :to="'/'"
              >
                HomePage
              </v-btn>

              <v-divider class="my-3"></v-divider>

              <v-btn
                text
                color="grey darken-1"
                plain
                router :to="'/personal'"
              >
                Personal center
              </v-btn>

              <v-divider class="my-3"></v-divider>

              <v-btn
                text
                color="grey darken-1"
                plain
                router :to="'/newpost'"
              >
                New Post
              </v-btn>

              <v-divider class="my-3"></v-divider>

              <v-btn
                text
                color="grey darken-1"
                plain
                router :to="'/newevent'"
              >
                New event
              </v-btn>

              <v-divider class="my-3"></v-divider>

              <v-btn
                text
                color="grey darken-1"
                plain
                @click="no"
              >
                Logout
              </v-btn>

            </div>
          </v-list-item-content>
        </v-card>
      </v-menu>

      <v-spacer></v-spacer>

      <!-- 设置为按钮是为了留一个刷新键 -->
      <v-btn class="text-uppercase primary--text" x-large text>
        <h1 class="font-weight-light">e</h1>
        <h1>venter</h1>
      </v-btn>

      <v-btn icon @click="toggleTheme">
        <v-icon right>mdi-theme-light-dark</v-icon>
      </v-btn>
    </v-toolbar>

  </nav>
</template>

<script>
export default {
  data() {
    return {
      user: {
        avatar: this.$store.state.avatar,
        fullName: this.$store.state.userNickName,
        email: this.$store.state.userEmail,
      },
    }
  },
  methods:{
    toggleTheme(){
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark
    },
    no: function(){
      this.$store.commit("logoutUpdate");
      this.$store.commit("userIDUpdate", "");
      console.log(this.$store.state.hasLogin);
      window.location.href = "/";
    },
    fresh: function(){
      this.user.avatar = this.$store.state.avatar
    }
  }

}
</script>

<style>
</style>
