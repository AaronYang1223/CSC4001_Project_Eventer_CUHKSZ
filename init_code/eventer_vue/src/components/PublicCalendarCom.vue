// 整体结构与CalendarCom相近，区别主要在于后台数据的读取和颜色design的不同，故不加赘述
<template>
  <v-row class="fill-height">
    <v-col>
      <v-sheet height="64">
        <v-toolbar
          flat
        >
          <v-btn
            outlined
            color="grey darken-2"
            @click="setToday"
            class="mr-4 hidden-xs-only"
          >
            Today
          </v-btn>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="prev"
          >
            <v-icon small>
              mdi-chevron-left
            </v-icon>
          </v-btn>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="next"
          >
            <v-icon small>
              mdi-chevron-right
            </v-icon>
          </v-btn>
          <v-toolbar-title v-if="$refs.calendar">
            {{ $refs.calendar.title }}
          </v-toolbar-title>

          <v-btn
            tile
            icon
            @click="changeCalendar"
          >
            <v-icon
            v-if="isPublic"  
            dark
            color=primary
            >
              mdi-account-multiple
            </v-icon>
            <v-icon 
            v-if="!isPublic" 
            dark
            color=primary
            >
              mdi-account
            </v-icon>
          </v-btn>

          <v-spacer></v-spacer>
          <v-menu
            bottom
            right
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                outlined
                color="grey darken-2"
                v-bind="attrs"
                v-on="on"
              >
                <span>{{ typeToLabel[type] }}</span>
                <v-icon right>
                  mdi-menu-down
                </v-icon>
              </v-btn>
            </template>
            <v-list>
              <!-- 适配时隐去一部分 -->
              <v-list-item @click="type = 'day'">
                <v-list-item-title>Day</v-list-item-title>
              </v-list-item>
              <v-list-item class="hidden-xs-only" @click="type = 'week'">
                <v-list-item-title>Week</v-list-item-title>
              </v-list-item>
              <v-list-item class="hidden-xs-only" @click="type = 'month'">
                <v-list-item-title>Month</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = '4day'">
                <v-list-item-title>4 days</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-toolbar>
      </v-sheet>

      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          v-model="focus"
          color="primary"
          :events="events"
          :event-color="getEventColor"
          :type="type"
          @click:event="showEvent"
          @click:more="viewDay"
          @click:date="viewDay"
        ></v-calendar>
        <v-menu
          v-model="selectedOpen"
          :close-on-content-click="false"
          :activator="selectedElement"
          offset-x
        >
        <!-- 更新显示，增加超链接 -->
          <v-card
            min-width="350px"
          >

            <v-card-title>
              <h2>{{selectedEvent.name}}</h2>
              <v-spacer></v-spacer>
              <v-chip
                class="ma-2"
                :color="getEventColor(selectedEvent)"
                outlined
              >
                {{ selectedEvent.DTime }}
                <v-icon
                  dark
                  right
                >
                  mdi-clock-time-two
                </v-icon>
              </v-chip>              
            </v-card-title>

            <v-divider></v-divider>
            <v-card-actions>
              <v-list-item class="grow">

                <v-list-item-avatar
                >
                  <v-img
                    class="elevation-6"
                    :src="selectedEvent.avatar"
                  ></v-img>
                </v-list-item-avatar>

                <v-badge
                  v-if="selectedEvent.is_authenticated"
                  color="accent"
                  icon="mdi-hexagram"
                  offset-x="30"
                  offset-y="25"
                >
                </v-badge>      

                <v-list-item-content>
                  <v-list-item-title>{{selectedEvent.nickname}}</v-list-item-title>
                </v-list-item-content>

                <v-row
                  align="center"
                  justify="end"
                >
                  <v-btn
                    text
                    color="secondary"
                    router :to="'/event/'+ selectedEvent.activity_id"
                  >
                    Detail
                  </v-btn>
                </v-row>

              </v-list-item>
            </v-card-actions>
          </v-card>
        </v-menu>
        
      </v-sheet>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    props:{
      isPublic:{
        type:Boolean
      }
    },
    data: () => ({
      focus: '',
      type: 'month',
      typeToLabel: {
        month: 'Month',
        week: 'Week',
        day: 'Day',
        '4day': '4 Days',
      },
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      events: [],
      colors: ['#FFA22F', '#0C4CCA', '#4551E6', '#34A1E1',],
      names: ['Meeting', 'Holiday', 'PTO', 'Travel', 'Event', 'Birthday', 'Conference', 'Party'],
      truth:[true, false],
      min_1: '',
      min_2: '',

    }),
    created(){
      if(this.$vuetify.breakpoint.mobile){
          this.type = "4day"
      }
      this.$axios.get('http://127.0.0.1:8000/api/public_calendar/all').then(response => {
        this.events = []
        console.log(response.data)
        for (let i = 0; i < response.data.length; i++) {
          this.events.push(
            {
              activity_id:response.data[i].activity_id,
              name: response.data[i].activity_title,
              start: new Date(response.data[i].activity_start_date),
              end: new Date(response.data[i].activity_end_date),
              DTime: this.showTime(new Date(response.data[i].activity_start_date), new Date(response.data[i].activity_end_date)), 
              avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
              is_authenticated: response.data[i].is_organization,
              nickname: response.data[i].nick_name,
              color: this.colors[this.rnd(0, this.colors.length - 1)],
              timed: new Date(response.data[i].activity_start_date),
            }
          )
        }
      })
    },
    // 渲染后调用
    mounted () {
      this.$refs.calendar.checkChange()
    },
    methods: {
      changeCalendar: function(){
        this.$emit('changeCalendar', !this.isPublic)
      }, 
      showTime (start, end) {
        this.min_1 = start.getMinutes()
        if (this.min_1 == 0){
          this.min_1 = "00"
        }else{
          this.min_1 = start.getMinutes().toString()
        }
        
        this.min_2 = end.getMinutes()
        if (this.min_2 == 0){
          this.min_2 = "00"
        }else{
          this.min_2 = end.getMinutes().toString()
        }
        return start.getHours().toString() + ":" + this.min_1 + "~" + end.getHours().toString() + ":" + this.min_2
      },
      viewDay ({ date }) {
        this.focus = date
        this.type = 'day'
      },
      getEventColor (event) {
        return event.color
      },
      setToday () {
        this.focus = ''
      },
      prev () {
        this.$refs.calendar.prev()
      },
      next () {
        this.$refs.calendar.next()
      },
      showEvent ({ nativeEvent, event }) {
        const open = () => {
          this.selectedEvent = event
          this.selectedElement = nativeEvent.target
          requestAnimationFrame(() => requestAnimationFrame(() => this.selectedOpen = true))
        }

        if (this.selectedOpen) {
          this.selectedOpen = false
          requestAnimationFrame(() => requestAnimationFrame(() => open()))
        } else {
          open()
        }

        nativeEvent.stopPropagation()
      },
    rnd (a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a
    },
    },

  }
</script>