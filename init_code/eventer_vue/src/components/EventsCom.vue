<template>
  <v-card
    class="mx-auto"
  >

    <v-container> 

      <v-row dense justify="center">
        <!-- 搜索框 -->
        <v-col
        cols="10"
        >
          <v-text-field
            v-model="search"
            label="Search Events"
            color="primary"
            clearable
            dense
          ></v-text-field>
        </v-col>

        <!-- 排序按钮 -->
        <v-col
        cols="1"
        align-end>
          <v-btn
            tile
            icon
            @click="changeSort"
          >
            <v-icon
            v-if="sort.icon" 
            dark
            color=blue
            >
              mdi-new-box
            </v-icon>
            <v-icon 
            v-if="!sort.icon" 
            dark
            color=red
            >
              mdi-fire
            </v-icon>
          </v-btn>
        </v-col>
        
      </v-row>

      <v-row>
        <!-- 显示所有event -->
        <v-col
          v-for="event in filteredEvents"
          :key="event"
          cols="12"
          sm="12"
          md="6"
        >
          <!-- 显示单个card -->
          <v-card
            flat
            outlined
          >

            <!-- 显示banner -->
            <v-img
              :src="event.banner"
              height="200px"
            >
            </v-img>

            <!-- 显示event信息简介 -->
            <v-card-title>
              <v-btn
              text
              router :to="'/event/'+ event.activity_id"
              >
              {{event.title | snippet_event}}
              </v-btn>
            </v-card-title>

            <v-card-subtitle>
              <v-chip-group>
                <v-chip
                  class="font-weight-light"
                  outlined
                  v-for="tag in event.tags"
                  :key="tag"
                  color="blue-grey lighten-2"
                  small
                >
                <v-icon left>
                  mdi-label
                </v-icon>
                  {{ tag | to-uppercase }}
                </v-chip>
              </v-chip-group>
            </v-card-subtitle>

            <v-card-actions>
              <!-- 详情跳转按钮 -->
              <v-btn
                color="orange lighten-2"
                text
                router :to="'/event/'+ event.activity_id"
              >
                Detail
              </v-btn>

              <v-chip
              color="accent"
              small
              >
              <v-icon left>
                mdi-clock
              </v-icon>
                {{ event.start_time }}
              </v-chip>

              <v-spacer></v-spacer>

              <v-btn
                icon
                @click="event.show = !event.show"
              >
                <v-icon>{{ event.show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
              </v-btn>
            </v-card-actions>

            <!-- 显示报名人数，活动发起方头像 -->
            <v-expand-transition>
              <div v-show="event.show">
                <v-divider></v-divider>

                <v-list-item class="grow">

                <v-list-item-avatar>
                  <v-img
                    class="elevation-6"
                    :src="event.avatar"
                  ></v-img>
                </v-list-item-avatar>

                  <v-badge
                  v-if="true"
                  color="accent"
                  icon="mdi-hexagram"
                  offset-x="30"
                  offset-y="25"
                >
                </v-badge>      

                  <v-list-item-content>
                    <v-list-item-title>{{event.nickname}}</v-list-item-title>
                  </v-list-item-content>

                  <v-row
                    align="center"
                    justify="end"
                  >
                    <v-icon class="mr-1">
                      mdi-account-group
                    </v-icon>
                    <span class="subheading mr-2">{{event.attend_num}}</span>
                    <span class="subheading mr-2">/</span>
                    <span class="subheading mr-2">{{event.upper_num}}</span>
                  </v-row>
                </v-list-item>
              </div>
            </v-expand-transition>

          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
  export default {
    props:{
      isPersonal:{
        type:Boolean
      }
    },

    data: () => ({
      events: [
      ],

      search:'',
      isTag : false,

      sort:{
        link: '',
        icon: false,
      },

      min: '',

      user_id: "",

    }),
    created(){
      this.user_id = this.$store.state.userID.toString()
      if(!this.isPersonal){
        this.$axios.get('http://127.0.0.1:8000/api/activity/order/comment_number/all').then(response => {
          this.events = []
          console.log(response.data)
          for (let i = 0; i < response.data.length; i++) {
            this.events.push(
              {
                activity_id: response.data[i].id,
                banner: 'http://127.0.0.1:8000' + response.data[i].cover_page,
                title: response.data[i].title,
                text: response.data[i].content,
                tags: response.data[i].tag.split(' '),
                avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
                is_authenticated: response.data[i].is_organization,
                nickname: response.data[i].nick_name,
                upper_num: response.data[i].max_participant_num,
                attend_num: response.data[i].participant_num,
                start_time: this.showStartTime(new Date(response.data[i].start_time)),
                end_time: response.data[i].end_time,
                selection: 0,
                show: false,
              }
            )
          }
        })
      }
      else{
        this.$axios.get('http://127.0.0.1:8000/api/activity/user/' + this.user_id).then(response => {
          this.events = []
          console.log(response.data)
          for (let i = 0; i < response.data.length; i++) {
            this.events.push(
              {
                activity_id: response.data[i].id,
                banner: 'http://127.0.0.1:8000' + response.data[i].cover_page,
                title: response.data[i].title,
                content: response.data[i].content,
                tags: response.data[i].tag.split(' '),
                avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
                is_authenticated: response.data[i].is_organization,
                nickname: response.data[i].nick_name,
                upper_num: response.data[i].max_participant_num,
                attend_num: response.data[i].participant_num,
                start_time:  this.showStartTime(new Date(response.data[i].start_time)),
                end_time: response.data[i].end_time,
                selection: 0,
                show: false,
              }
            )
          }
        })
      }
    },
    computed:{
      filteredEvents:function(){
        if (!this.search) return this.events

        return this.events.filter((event)=>{
          this.isTag = false;
          event.tags.forEach(element => {
            if (element.toLowerCase().match(this.search.toLowerCase())){
              this.isTag = true;
            }
          });
          return ( event.title.toLowerCase().match(this.search.toLowerCase()) || event.nickname.toLowerCase().match(this.search.toLowerCase()) || this.isTag )
        })
      }
    },
    // run when anything change
    methods: {
      showStartTime (start) {
        console.log(1)
        this.min = start.getMinutes()
        if (this.min < 10){
          this.min = "0" + this.min.toString()
        }else{
          this.min = start.getMinutes().toString()
        }

        return (start.getMonth() + 1).toString() + "/" + start.getDate().toString() + " " + start.getHours().toString() + ":" + this.min 
      },
      changeSort: function(){
        this.user_id = this.$store.state.userID.toString()
        if(!this.isPersonal){
          this.sort.icon = !this.sort.icon
          this.sort.link = this.sort.icon ? 'http://127.0.0.1:8000/api/activity/order/create_date/all' : 'http://127.0.0.1:8000/api/activity/order/comment_number/all'
          this.$axios.get(this.sort.link).then(response => {
            this.events = []
            console.log("FIX")
            console.log(response.data)
            for (let i = 0; i < response.data.length; i++) {
              this.events.push(
                {
                  activity_id: response.data[i].id,
                  banner: 'http://127.0.0.1:8000' + response.data[i].cover_page,
                  title: response.data[i].title,
                  text: response.data[i].content,
                  tags: response.data[i].tag.split(' '),
                  avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
                  is_authenticated: response.data[i].is_organization,
                  nickname: response.data[i].nick_name,
                  upper_num: response.data[i].max_participant_num,
                  attend_num: response.data[i].participant_num,
                  start_time: this.showStartTime(new Date(response.data[i].start_time)),
                  end_time: response.data[i].end_time,
                  selection: 0,
                  show: false,
                }
              )
            }
          })
        }
        else{
          this.sort.icon = !this.sort.icon 
          this.sort.link = this.sort.icon ? ('http://127.0.0.1:8000/api/activity/user/order/create_date/' + this.user_id) : ('http://127.0.0.1:8000/api/activity/user/order/comment_number/' + this.user_id)
          this.$axios.get(this.sort.link).then(response => {
            this.events = []
            console.log("FIX")
            console.log(response.data)
            for (let i = 0; i < response.data.length; i++) {
              this.events.push(
                {
                  activity_id: response.data[i].id,
                  banner: 'http://127.0.0.1:8000' + response.data[i].cover_page,
                  title: response.data[i].title,
                  text: response.data[i].content,
                  tags: response.data[i].tag.split(' '),
                  avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
                  is_authenticated: response.data[i].is_organization,
                  nickname: response.data[i].nick_name,
                  upper_num: response.data[i].max_participant_num,
                  attend_num: response.data[i].participant_num,
                  start_time: this.showStartTime(new Date(response.data[i].start_time)),
                  end_time: response.data[i].end_time,
                  selection: 0,
                  show: false,
                }
              )
              
            }
          })
        }
      },
    },
  }
</script>