// TODO:连接api？ 整理
<template>
  <v-card
    class="mx-auto mb-2"
    outlined
    tile
  >
    <v-row dense>
      <v-col
          class="text-h2"
          cols="12" xs="8" sm="12" md="8"
          align="center"
      >
        <v-card
        class="mx-auto mt-2"
        flat
        tile
        height="83"
        >
          <v-list-item two-line>
            <v-list-item-content>
              <v-list-item-title >
                <h1 class="font-weight-black">CUHKSZ</h1>       
              </v-list-item-title>
              <v-list-item-subtitle>{{date}}, {{time}}, {{weather}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>

      <v-col
        cols="12" xs="4" sm="12" md="4"
        align="center"
      >
        <v-card
          class="mx-auto mt-2"
          flat
          tile
          height="83"
        >

          <h1 class="font-weight-thin text-center">23&deg;C</h1>

          <v-img
            :src="weather_img"
            width="30"
          ></v-img>
        </v-card>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      date: "Mon",
      time: "12:30 PM",
      weather: "Mostly sunny",
      weather_img: "https://cdn.vuetifyjs.com/images/cards/sun.png",
    }),
  }
</script>
