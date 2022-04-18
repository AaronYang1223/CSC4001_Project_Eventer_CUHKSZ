// TODO:读懂代码并修改，承担发帖子和发event的作用
<template>
  <v-card
    class="mx-auto"
    flat
    tile
    outlined
  >

    <v-card
      class="mt-3"
      tile
      flat
      height="40"
    >
      <h3 v-if="!isPost" class="font-weight-black text-center">
        Hot Events
      </h3>
      <h3 v-if="isPost" class="font-weight-black text-center">
        Hot Posts
      </h3>
    </v-card>

    <v-divider></v-divider>

    <v-list 
      v-if="!isPost"
      three-line
    >

        <v-list-item
          v-for="(event, i) in events"
          :key="i"
        >
          
          <v-list-item-avatar>
            <v-img :src="event.avatar"></v-img>
          </v-list-item-avatar>

          <v-badge
              v-if="event.is_authenticated"
              color="accent"
              icon="mdi-hexagram"
              offset-x="30"
              offset-y="20"
            >
          </v-badge>  

          <v-list-item-content>
            <v-list-item-title v-if="i==0" >
              <v-btn
                text
                router :to="'/event/'+ event.activity_id"
                color="red"
              >
              <h3>{{event.title | snippet_event}}</h3>
              </v-btn>
            </v-list-item-title>
            <v-list-item-title v-else-if="i==1" >
              <v-btn
                text
                router :to="'/event/'+ event.activity_id"
                color="orange"
              >
              <h3>{{event.title | snippet_event}}</h3>
              </v-btn>
            </v-list-item-title>
            <v-list-item-title v-else-if="i==2">
              <v-btn
                text
                router :to="'/event/'+ event.activity_id"
                color="amber"
                >
                <h3>{{event.title | snippet_event}}</h3>
              </v-btn>
            </v-list-item-title>
            <v-list-item-title v-else v-html="event.title">
              <v-btn
                text
                router :to="'/event/'+ event.activity_id"
                >
                <h3>{{event.title | snippet_event}}</h3>
              </v-btn>
            </v-list-item-title>
            <v-list-item-subtitle v-html="event.content">
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
    </v-list>

    <v-list 
      v-if="isPost"
      three-line
    >

        <v-list-item
          v-for="(post, i) in posts"
          :key="i"
        >
          
          <v-list-item-avatar>
            <v-img :src="post.avatar"></v-img>
          </v-list-item-avatar>

          <v-badge
              v-if="post.is_authenticated"
              color="accent"
              icon="mdi-hexagram"
              offset-x="30"
              offset-y="20"
            >
          </v-badge>  

          <v-list-item-content>
            <v-list-item-title v-if="i==0" >
              <v-btn
                text
                router :to="'/post/'+ post.post_id"
                color="red"
              >
              <h3>{{post.title | snippet_event}}</h3>
              </v-btn>
            </v-list-item-title>
            <v-list-item-title v-else-if="i==1">
              <v-btn
                text
                router :to="'/post/'+ post.post_id"
                color="orange"
              >
              <h3>{{post.title | snippet_event}}</h3>
              </v-btn>
            </v-list-item-title>
            <v-list-item-title v-else-if="i==2">
              <v-btn
                text
                router :to="'/post/'+ post.post_id"
                color="amber"
              >
              <h3>{{post.title | snippet_event}}</h3>
              </v-btn>
            </v-list-item-title>
            <v-list-item-title v-else >
              <v-btn
                text
                router :to="'/post/'+ post.post_id"
              >
              <h3>{{post.title | snippet_event}}</h3>
              </v-btn>
            </v-list-item-title>
            
            <v-list-item-subtitle v-html="post.content"></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
    </v-list>
  </v-card>
</template>

<script>
  export default { 
    props:{
      isPost:{
        type:Boolean
      }
    },
    created(){

      this.posts_link = 'http://127.0.0.1:8000/api/post/order/comment_number/5'
      this.$axios.get(this.posts_link).then(response => {
        this.posts = []
        for (let i = 0; i < response.data.length; i++) {
          this.posts.push(
            {
              post_id: response.data[i].id,
              title: response.data[i].post_title,
              content: response.data[i].post_content,
              tags: response.data[i].post_tag.split(' '),
              avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
              is_authenticated: response.data[i].is_organization,
              nickname: response.data[i].nick_name,
              comment_num: response.data[i].comment_number,
            }
          )
        }
      })

      this.activity_link = 'http://127.0.0.1:8000/api/activity/order/comment_number/5'
      this.$axios.get(this.activity_link).then(response => {
        this.events = []
        console.log("hot events")
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
              start_time: response.data[i].start_time,
              end_time: response.data[i].end_time,
              selection: 0,
              show: false,
            }
          )
        }
      })

      // get_post_user(user_id) {
      //   this.posts_link = 'http://127.0.0.1:8000/api/post/user/' + user_id
      //   this.$axios.get(this.posts_link).then(response => {
      //     this.posts = []
      //     for (let i = 0; i < response.data.length; i++) {
      //       this.posts.push(
      //         {
      //           post_id: response.data[i].id,
      //           title: response.data[i].post_title,
      //           content: response.data[i].post_content,
      //           tags: response.data[i].post_tag.split(' '),
      //           avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
      //           is_authenticated: response.data[i].is_organization,
      //           nickname: response.data[i].nick_name,
      //           comment_num: response.data[i].comment_number,
      //         }
      //       )
      //     }
      //   })
      // }

      // get_activity_user(user_id) {
      //   this.activity_link = 'http://127.0.0.1:8000/api/activity/user/' + user_id
      //   this.$axios.get(this.activity_link).then(response => {
      //     this.events = []
      //     console.log(response.data)
      //     for (let i = 0; i < response.data.length; i++) {
      //       this.events.push(
      //         {
      //           activity_id: response.data[i].id,
      //           banner: 'http://127.0.0.1:8000' + response.data[i].cover_page,
      //           title: response.data[i].title,
      //           content: response.data[i].content,
      //           tags: response.data[i].tag.split(' '),
      //           avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
      //           is_authenticated: response.data[i].is_organization,
      //           nickname: response.data[i].nick_name,
      //           upper_num: response.data[i].max_participant_num,
      //           attend_num: response.data[i].participant_num,
      //           start_time: response.data[i].start_time,
      //           end_time: response.data[i].end_time,
      //           selection: 0,
      //           show: false,
      //         }
      //       )
      //     }
      //   })
      // }
      
    },
    data: () => ({
      posts: [
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
          is_authenticated: true,
          title: 'Brunch this weekend?',
          content: `<span class="text--primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
        },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
          is_authenticated: false,
          title: 'Summer BBQ ',
          content: `<span class="text--primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
        },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
          is_authenticated: true,
          title: 'Oui oui',
          content: '<span class="text--primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
        },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
          is_authenticated: false,
          title: 'Birthday gift',
          content: '<span class="text--primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
        },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
          is_authenticated: false,
          title: 'Recipe to try',
          content: '<span class="text--primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
        },
      ],
      events: [
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
          is_authenticated: true,
          title: 'Brunch this weekend?',
          content: `<span class="text--primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
        },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
          is_authenticated: false,
          title: 'Summer BBQ ',
          content: `<span class="text--primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
        },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
          is_authenticated: true,
          title: 'Oui oui',
          content: '<span class="text--primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
        },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
          is_authenticated: false,
          title: 'Birthday gift',
          content: '<span class="text--primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
        },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
          is_authenticated: false,
          title: 'Recipe to try',
          content: '<span class="text--primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
        },
      ],
    }),
  }
</script>