<template>
  <div class="personal">
     <v-container>
      <v-row no-gutters>
        <v-col 
          cols="12" xs="12" sm="12" md="12" 
        >
          <v-card
            class="pa-2 mx-1 mt-2"
            outlined
            tile
          >
          <!-- 适配时直接右侧砍掉 做成超链接形式-->
            <v-tabs
              vertical 
              slider-size="3"
              height="600px"
              grow
              right
            >
              <v-tab>
                <v-icon left>
                  mdi-account
                </v-icon>
                Personal Information
              </v-tab>
              <v-tab>
                <v-icon left>
                  mdi-calendar
                </v-icon>
                Personal Calendar
              </v-tab>
              <v-tab>
                <v-icon left>
                  mdi-post
                </v-icon>
                New Post
              </v-tab>
              <v-tab>
                <v-icon left>
                  mdi-calendar-plus
                </v-icon>
                New Event
              </v-tab>
              <v-tab>
                <v-icon left>
                  mdi-access-point
                </v-icon>
                Option 5
              </v-tab>

              <v-tab-item>
                <v-card flat >
                <NewUpdateImageCom :uploadType="`head`" :imgWidth="`85px`" :imgHeight="`104px`" :imgUrl="'https://cdn.vuetifyjs.com/images/cards/foster.jpg'"
    @upload="getImgUrl"></NewUpdateImageCom>
                <ChangeInfoCom />
                </v-card>
              </v-tab-item>
              <v-tab-item>
                <v-card flat>
                  <CalendarCom />
                </v-card>
              </v-tab-item>
              <v-tab-item>
                <v-card flat>
                  <v-card-text>
                    <p>
                      Fusce a quam. Phasellus nec sem in justo pellentesque facilisis. Nam eget dui. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In dui magna, posuere eget, vestibulum et, tempor auctor, justo.
                    </p>

                    <p class="mb-0">
                      Cras sagittis. Phasellus nec sem in justo pellentesque facilisis. Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nam at tortor in tellus interdum sagittis.
                    </p>
                  </v-card-text>
                </v-card>
              </v-tab-item>
            </v-tabs>

          </v-card>
        </v-col>

      </v-row>
    </v-container>
    

  </div>
</template>

<script>
import NewUpdateImageCom from '@/components/NewUpdateImageCom'
import CalendarCom from '@/components/CalendarCom'
import ChangeInfoCom from '@/components/ChangeInfoCom'

export default {
  name: 'PersonalCenterView',
  components: {NewUpdateImageCom, CalendarCom, ChangeInfoCom},
  data () {
    return {

    }
  },
  methods:{
//接收子组件emit的事件
getImgUrl(data) {
    console.log("父组件")
    console.log(data)  
}
  },
}
</script>