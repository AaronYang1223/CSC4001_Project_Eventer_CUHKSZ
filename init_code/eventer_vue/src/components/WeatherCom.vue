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
          cols="12" xs="6" sm="12" md="6"
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
              <v-list-item-subtitle>{{date}}, {{weather}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>

      <v-col
        cols="12" xs="6" sm="12" md="6"
        align="center"
      >
        <v-card
          class="mt-6"
          flat
          tile
          height="83"
        >

          <h1 class="font-weight-thin text-center display-2">{{temperature}}&deg;C</h1>

          <!-- <v-img
            :src="weather_img"
            width="30"
          ></v-img> -->
        </v-card>
      </v-col>
    </v-row>
  </v-card>
</template>

// <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
// <script src="https://cdn.bootcdn.net/ajax/libs/crypto-js/4.0.0/crypto-js.js"></script>

<script>
  export default {
    data: () => ({
      date: "2022-04-12",
      time: "02:00:29",
      weather: "Mostly sunny",
      weather_img: "https://cdn.vuetifyjs.com/images/cards/sun.png",
      city: "Shenzhen",
    }),
    //Update weather info
    mounted() {
      this.weather_link = 'https://restapi.amap.com/v3/weather/weatherInfo?city=440307&key=4e5aad6906d160b50e6018ea4891b29c'
      this.$axios.get(this.weather_link).then(response => {
        this.temperature = response.data.lives[0].temperature
        this.date = response.data['lives'][0]['reporttime'].split(' ')[0]
        this.time = response.data['lives'][0]['reporttime'].split(' ')[1]
        this.weather = response.data['lives'][0]['weather'],
        this.city = response.data['lives'][0]['city']
        this.humidity = response.data['lives'][0]['humidity']
        this.winddirection = response.data['lives'][0]['winddirection']
        this.windpower = response.data['lives'][0]['windpower']
      })
      // var appKey = '07c0e4651c277a50'
      // var key = 'AaQCL0vFyaXKGVINyE0o9XjQf6s4qxrI'
      // var salt = (new Date).getTime()
      // var curtime = Math.round(new Date().getTime()/1000)
      // var query = this.weather
      // var from = 'zh-CHS'
      // var to = 'en'
      // var str1 = appKey + query + salt + curtime + key
      // var sign = this.CryptoJS.SHA256(str1).toString(this.CryptoJS.enc.Hex)
      // this.$axios.post('https://openapi.youdao.com/api', {
      //   q: query,
      //   appKey: appKey,
      //   salt: salt,
      //   from: from,
      //   to: to,
      //   sign: sign,
      //   signType: 'v3',
      //   curtime: curtime
      // }).then(response => {
      //   this.tras = response.data.translation[0]
      //   console.log(response.data)
      // })
    }
}
</script>
