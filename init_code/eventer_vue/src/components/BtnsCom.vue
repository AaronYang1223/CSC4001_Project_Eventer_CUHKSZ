<template>
  <v-container>
    <v-card
      flat
      outlined
      tile
      min-height="95px"
    >

      <v-row class="mt-1 px-3" 
        align="center"
        justify="space-around"
      >
        <v-card
          flat
          tile
          max-height="80px"
          min-width="40px"
        >
          <v-list-item-content class="justify-center">

            <v-btn
              color="#DC004A"
              dark
              icon
              tile
              router :to="'/newpost'"
            >
              <v-icon>mdi-post</v-icon>
            </v-btn>        

            <div class="text-center mt-1">

              <span>New</span>

            </div>

          </v-list-item-content>
        </v-card>
        <v-card
          flat
          tile
          max-height="80px"
          min-width="40px"
        >
          <v-list-item-content class="justify-center">

            <v-btn
              color="#10A5D7"
              dark
              icon
              tile
              router :to="'/newevent'"
            >
              <v-icon>mdi-calendar-plus</v-icon>
            </v-btn>        

            <div class="text-center mt-1">

              <span>New</span>

            </div>

          </v-list-item-content>
        </v-card>
        <v-card
          flat
          tile
          max-height="80px"
          min-width="40px"
        >
          <v-list-item-content class="justify-center">

            <v-btn
              color="#FFD50A"
              dark
              icon
              tile
              @click="no"
            >
              <v-icon>mdi-lock</v-icon>
            </v-btn>        

            <div class="text-center mt-1">

              <span>Edit</span>

            </div>

          </v-list-item-content>
        </v-card>
      </v-row>

    </v-card>
  </v-container>
</template>

<script>
export default {
  data() {
    return {

    }
  },
  methods:{
    no: function(){
      this.$store.commit("logoutUpdate");
      this.$store.commit("userIDUpdate", "");
      console.log(this.$store.state.hasLogin);
      window.location.href = "/forget";
    },
  }

}
</script>