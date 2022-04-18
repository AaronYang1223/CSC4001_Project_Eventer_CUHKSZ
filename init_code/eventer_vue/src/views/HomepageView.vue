<template>
  <div class="home">
    <v-container>
      <v-row no-gutters>
        <v-col class="hidden-sm-and-up"
          cols="12" xs="12" sm="4" md="4"
          
        >
          <v-card
            class="pa-2 mx-1 mt-2"
            outlined
            tile
          >
            <WeatherCom />
          </v-card>
        </v-col>

        <v-col 
          cols="12" xs="12" sm="8" md="8" 
        >
          <v-card
            class="pa-2 mx-1 mt-2"
            outlined
            tile
          >
            <v-tabs
              v-model="tab"
            >
              <v-tab href="#tab-1">
                Calendar
              </v-tab>
              <v-tab href="#tab-2">
                Posts
              </v-tab>
              <v-tab href="#tab-3">
                Events
              </v-tab>
              <v-tabs-slider color="accent"></v-tabs-slider>
            </v-tabs>

            <v-tabs-items v-model="tab">
              {{updateNews(tab)}}
              <v-tab-item
                v-for="i in 3"
                :key="i"
                :value="'tab-' + i"
              >
                
                <v-card v-if="i == 1 && !isPublic" flat>
                  <CalendarCom v-bind:isPublic="isPublic" v-on:changeCalendar = "updateCalendar($event)"></CalendarCom>
                </v-card>
                <v-card v-if="i == 1 && isPublic" flat>
                  <PublicCalendarCom v-bind:isPublic="isPublic" v-on:changeCalendar = "updateCalendar($event)"></PublicCalendarCom>
                </v-card>
                <v-card v-if="i == 2" flat>
                  <PostsCom v-bind:isPersonal="isPersonal"></PostsCom>
                </v-card>
                <v-card v-if="i == 3" flat>
                  <EventsCom v-bind:isPersonal="isPersonal"> </EventsCom>
                </v-card>
              </v-tab-item>
            </v-tabs-items>

          </v-card>
        </v-col>

        <!-- 确定这个part的手机端适配方式：隐藏？ -->
        <v-col 
          cols="12" xs="12" sm="4" md="4"
          class="hidden-xs-only"
        >
          <v-card
            class="pa-2 mx-1 mt-2"
            outlined
            tile
          >
            <WeatherCom />
            <NewsCom v-bind:isPost="isPost"></NewsCom>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import CalendarCom from '@/components/CalendarCom'
import PostsCom from '@/components/PostsCom'
import EventsCom from '@/components/EventsCom'
import WeatherCom from '@/components/WeatherCom'
import NewsCom from '@/components/NewsCom'
import PublicCalendarCom from '@/components/PublicCalendarCom'

export default {
  name: 'HomepageView',
  components: { CalendarCom, PostsCom, EventsCom, WeatherCom, NewsCom, PublicCalendarCom},
  data () {
    return {
      tab: null,
      isPublic: false,
      isPost: true,
      isPersonal: false,
    }
  },
  methods:{
    // Work as Filter
    updateCalendar: function(updatedCalendar){
      this.isPublic = updatedCalendar
    },
    // Work as Filter
    updateNews: function(tab){
      if(tab == "tab-2"){
        this.isPost = true
      }else if(tab == "tab-3"|| tab == "tab-1"){
        this.isPost =false
      }
      console.log(this.isPost)
    }
  }
}
</script>