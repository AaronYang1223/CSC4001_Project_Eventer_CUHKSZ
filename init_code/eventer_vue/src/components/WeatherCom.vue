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
                <h1 class="font-weight-black">{{city}}</h1>       
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

          <h1 class="font-weight-thin text-center">{{temperature}}&deg;C</h1>

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
      date: "2022-04-12",
      time: "02:00:29",
      weather: "Mostly sunny",
      weather_img: "https://cdn.vuetifyjs.com/images/cards/sun.png",
      city: "Shenzhen",
    }),
    mounted() {
      this.weather_link = 'https://restapi.amap.com/v3/weather/weatherInfo?city=440307&key=4e5aad6906d160b50e6018ea4891b29c'
      this.$axios.get(this.weather_link).then(response => {
        this.temperature = response.data.lives[0].temperature
        this.date = response.data['lives'][0]['reporttime'].split(' ')[0]
        this.time = response.data['lives'][0]['reporttime'].split(' ')[1]
        this.weather = response.data['lives'][0]['weather'],
        this.city = response.data['lives'][0]['province'] + ' ' + response.data['lives'][0]['city']
        this.humidity = response.data['lives'][0]['humidity']
        this.winddirection = response.data['lives'][0]['winddirection']
        this.windpower = response.data['lives'][0]['windpower']
      })
    }
  }
</script>
