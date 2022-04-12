<template>
  <v-card
    class="mx-auto"
  >

    <v-container> 

      <v-row dense justify="center">
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
        <v-col
          v-for="event in filteredEvents"
          :key="event"
          cols="12"
          sm="12"
          md="6"
        >
          <v-card
            flat
            outlined
          >

            <v-img
              :src="event.banner"
              height="200px"
            >
            </v-img>

            <v-card-title>
              <v-btn
              text
              router :to="'/post/1'"
              >
              {{event.title | snippet_event}}
              </v-btn>
            </v-card-title>

            <v-card-subtitle>
              <!-- 存在显示不全的问题 -->
              <v-chip-group
              >
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
                  {{ tag | to-uppercase}}
                </v-chip>
              </v-chip-group>
            </v-card-subtitle>

            <v-card-actions>
              <v-btn
                color="orange lighten-2"
                text
              >
                Register
              </v-btn>

              <v-spacer></v-spacer>

              <v-btn
                icon
                @click="event.show = !event.show"
              >
                <v-icon>{{ event.show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
              </v-btn>
            </v-card-actions>

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
                    <!-- 外观考虑修改 -->
                    <v-icon class="mr-1">
                      mdi-account-group
                    </v-icon>
                    <span class="subheading mr-2">{{event.attend_num}}</span>
                    <span class="subheading mr-2">/</span>
                    <span class="subheading mr-2">{{event.upper_num}}</span>
                  </v-row>
                </v-list-item>

                <v-card-text>
                <v-chip-group
                  v-model="event.selection"
                  active-class="primary--text text--accent-4"
                  mandatory
                >
                <v-chip
                  v-for="time in event.available_time"
                  :key="time"
                >
                  {{ time }}
                </v-chip>
                </v-chip-group>
                </v-card-text>
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
    data: () => ({
      events: [
        // {
        //   banner:'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
        //   title: 'Supermodel',
        //   tags: ['Work', 'Home Improvement',] ,
        //   avatar: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
        //   is_authenticated: false,
        //   nickname: 'Foster the People',
        //   upper_num: 111,
        //   attend_num: 11,
        //   available_time:['5:30PM','7:30PM','8:00PM','9:00PM'],
        //   selection: 0,
        //   show: false,
        // },
        // {
        //   banner:'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
        //   title: 'Halcyon Days',
        //   tags: ['Art', 'Tech', 'Creative Writing',] ,
        //   avatar: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
        //   is_authenticated: true,
        //   nickname: 'Ellie Goulding',
        //   upper_num: 222,
        //   attend_num: 22,
        //   available_time:['5:30PM','9:00PM'],
        //   selection: 0,
        //   show: false,
        // },
        //   {
        //   banner:'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
        //   title: 'Title',
        //   tags: ['Art', 'Creative Writing',] ,
        //   avatar: 'https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light',
        //   is_authenticated: false,
        //   nickname: 'Evan You',
        //   upper_num: 333,
        //   attend_num: 33,
        //   available_time:['8:00PM','9:00PM'],
        //   selection: 0,
        //   show: false,
        // },
        // {
        //   banner:'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
        //   title: 'Supermodel',
        //   tags: ['Work', 'Home Improvement',] ,
        //   avatar: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
        //   is_authenticated: false,
        //   nickname: 'Foster the People',
        //   upper_num: 111,
        //   attend_num: 11,
        //   available_time:['5:30PM','7:30PM','8:00PM','9:00PM'],
        //   selection: 0,
        //   show: false,
        // },
        // {
        //   banner:'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
        //   title: 'Halcyon Days',
        //   tags: ['Art', 'Tech', 'Creative Writing',] ,
        //   avatar: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
        //   is_authenticated: true,
        //   nickname: 'Ellie Goulding',
        //   upper_num: 222,
        //   attend_num: 22,
        //   available_time:['5:30PM','9:00PM'],
        //   selection: 0,
        //   show: false,
        // },
        //   {
        //   banner:'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
        //   title: 'Title',
        //   tags: ['Art', 'Creative Writing',] ,
        //   avatar: 'https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light',
        //   is_authenticated: false,
        //   nickname: 'Evan You',
        //   upper_num: 333,
        //   attend_num: 33,
        //   available_time:['8:00PM','9:00PM'],
        //   selection: 0,
        //   show: false,
        // },
      ],

      search:'',
      isTag : false,

      sort:{
        link: '',
        icon: false,
      },

    }),
    created(){
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
              start_time: response.data[i].start_time,
              end_time: response.data[i].end_time,
              selection: 0,
              show: false,
            }
          )
        }
      })
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
      changeSort: function(){
        this.sort.icon = !this.sort.icon
        this.sort.link = this.sort.icon ? 'http://127.0.0.1:8000/api/activity/order/create_date/all' : 'http://127.0.0.1:8000/api/activity/order/comment_number/all'
        this.$axios.get(this.sort.link).then(response => {
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
                start_time: response.data[i].start_time,
                end_time: response.data[i].end_time,
                selection: 0,
                show: false,
              }
            )
            
          }
        })
      },
      register: function(user_id, activity_id){
        this.sort.link = 'http://127.0.0.1:8000/api/activity/participant/add'
        this.$axios.post(this.sort.link, {
          activity_id: activity_id,
          user_id: user_id,
        }).then(response => {
          console.log(response.data)
      
        })
      },
    },
  }
</script>