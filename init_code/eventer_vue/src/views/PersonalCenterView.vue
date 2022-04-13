<template>
  <div class="personal">
    <v-container>
      <v-row no-gutters>
        <v-col
          cols="12" xs="12" sm="4" md="4"
          
        >
          <v-card
            class="pa-2 mx-1 mt-2"
            outlined
            tile
          >
            <NewUpdateImageCom 
              :uploadType="`head`" 
              @upload="getImgUrl"
            >
            </NewUpdateImageCom>
            <BtnsCom />
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
                
                <v-card v-if="i == 1" flat>
                  <CalendarCom></CalendarCom>
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
      </v-row>
    </v-container>

  </div>
</template>

<script>
import NewUpdateImageCom from '@/components/NewUpdateImageCom'
import CalendarCom from '@/components/CalendarCom'
import PostsCom from '@/components/PostsCom'
import EventsCom from '@/components/EventsCom'
import BtnsCom from '@/components/BtnsCom'

export default {
  name: 'PersonalCenterView',
  components: {NewUpdateImageCom, CalendarCom, PostsCom, EventsCom, BtnsCom},
  data () {
    return {
      tab: null,
      isPersonal: true,
    }
  },
  methods:{
    //接收子组件emit的事件
    getImgUrl(data) {
        console.log("父组件")
        console.log(data)  
    },
    updateCalendar: function(updatedCalendar){
      this.isPublic = updatedCalendar
    },
    updateNews: function(tab){
      if(tab == "tab-2"){
        this.isPost = true
      }else if(tab == "tab-3"|| tab == "tab-1"){
        this.isPost =false
      }
      console.log(this.isPost)
    }
  },
}
</script>