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
          cols="8"
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
        cols="4"
        align="center"
      >
        <v-card
          class="mx-auto mt-1"
          flat
          tile
          height="83"
        >
          <v-card-title>
            <h2 class="font-weight-thin">23&deg;C</h2>
          </v-card-title>
            <v-card-subtitle>
              <v-img
                :src="weather_img"
                width="30"
              ></v-img>
            </v-card-subtitle>
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
