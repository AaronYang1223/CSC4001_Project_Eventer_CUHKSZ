// TODO:在功能上考虑和event的结合程度，更改适配

<template>
  <v-row class="fill-height">
    <v-col>
      <v-sheet height="64">
        <v-toolbar
          flat
        >
          <v-btn
            outlined
            class="mr-4"
            color="grey darken-2"
            @click="setToday"
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
            v-icon 
            dark
            color=primary
            >
              mdi-account-multiple
            </v-icon>
            <v-icon 
            v-if="!isPublic" 
            v-icon 
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
              <v-list-item @click="type = 'week'">
                <v-list-item-title>Week</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = 'month'">
                <v-list-item-title>Month</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = '4day'">
                <v-list-item-title>4 days</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-toolbar>
      </v-sheet>

<!-- //TODO:更GAI CHANGE!!! -->
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
          @change="updateRange"
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
                :color="selectedEvent.color"
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
      //TODO:更改主题色!!!
      colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'orange', 'grey'],
      names: ['Meeting', 'Holiday', 'PTO', 'Travel', 'Event', 'Birthday', 'Conference', 'Party'],
      truth:[true, false],
      min_1: '',
      min_2: '',

    }),
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
        return start.getUTCHours().toString() + ":" + this.min_1 + "~" + end.getUTCHours().toString() + ":" + this.min_2
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
      updateRange ({ start, end }) {
        const events = []

        const min = new Date(`${start.date}T00:00:00`)
        const max = new Date(`${end.date}T23:59:59`)
        const days = (max.getTime() - min.getTime()) / 86400000
        const eventCount = this.rnd(days, days + 20)

        for (let i = 0; i < eventCount; i++) {
          const allDay = this.rnd(0, 3) === 0
          const firstTimestamp = this.rnd(min.getTime(), max.getTime())
          const first = new Date(firstTimestamp - (firstTimestamp % 900000))
          const secondTimestamp = this.rnd(2, allDay ? 288 : 8) * 900000
          const second = new Date(first.getTime() + secondTimestamp)

          events.push({
            name: this.names[this.rnd(0, this.names.length - 1)],
            start: first,
            end: second,
            DTime: this.showTime(first, second), 
            color: this.colors[this.rnd(0, this.colors.length - 1)],
            timed: !allDay,

            avatar: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
            is_authenticated: this.truth[this.rnd(0, this.truth.length - 1)],
            nickname: 'Foster the People',

            is_personal: this.truth[this.rnd(0, this.truth.length - 1)],
          })
        }

        this.events = events
      },
      rnd (a, b) {
        return Math.floor((b - a + 1) * Math.random()) + a
      },
      changeSort: function(){
        this.sort.link = 'http://127.0.0.1:8000/api/public_calendar/all'
        this.$axios.get(this.sort.link).then(response => {
          this.public_calendar = []
          console.log(response.data)
          for (let i = 0; i < response.data.length; i++) {
            this.public_calendar.push(
              {
                name: response.data[i].activity_title,
                start: response.data[i].start_date,
                end: response.data[i].end_date,
                tags: response.data[i].tag.split(' '),
                avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
                is_authenticated: response.data[i].is_organization,
                nickname: response.data[i].nick_name,
                // public 没有这个选项，因为和个人是没有关系的
                // is_personal: response.data[i].is_personal,
              }
            )
            
          }
        })
      },
    },
  }
</script>