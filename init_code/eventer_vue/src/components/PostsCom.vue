// 整体结构与EventsCom相近，故不加赘述
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
            label="Search Posts"
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

      <v-row dense>
      
        <v-col
          v-for="(post, i) in filteredPosts"
          :key="i"
          cols="12"
        >
        
          <v-card
            flat
            outlined
          >

            <v-card-title>
              <v-btn
              class="text-h5 font-weight-black "
              v-rainbow
              text
              router :to="'/post/'+ post.id"
              >
                {{post.title | snippet_post}}
              </v-btn>
            </v-card-title>

          <!-- 强制提取富文本 -->
          <v-container mx-1>
            <p
            class="text-h6 font-weight-bold"
            >
              {{post.text | snippet}}
            </p>
          </v-container>

            <v-row class="mx-3">
              <v-chip-group>
                <v-chip
                  class="ma-2 font-weight-black"
                  outlined
                  v-for="tag in post.tags"
                  :key="tag"
                  color="accent"
                >
                <v-icon left>
                  mdi-label
                </v-icon>
                  {{ tag | to-uppercase}}
                </v-chip>
              </v-chip-group>
            </v-row>

            <v-card-actions>
              <v-list-item class="grow">

              <v-list-item-avatar
              >
                <v-img
                  class="elevation-6"
                  :src="post.avatar"
                ></v-img>
              </v-list-item-avatar>

                <v-badge
                v-if="post.is_authenticated"
                color="accent"
                icon="mdi-hexagram"
                offset-x="30"
                offset-y="25"
              >
              </v-badge>      

                <v-list-item-content>
                  <v-list-item-title>{{post.nickname}}</v-list-item-title>
                </v-list-item-content>

                <v-row
                  align="center"
                  justify="end"
                >
                  <v-icon class="mr-1">
                    mdi-comment-multiple
                  </v-icon>
                  <span class="subheading">{{post.comment_num}}</span>
                </v-row>
              </v-list-item>
            </v-card-actions>

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
      posts: [
      ],
    search:'',
    isTag : false,
    sort:{
      link: '',
      icon: false,
    },
    user_id: "",
    text: "text",
    }),
    // return private posts or all the posts
    created(){
      this.user_id=String(this.$store.state.userID)
      console.log(this.$store.state.userID)
      if(!this.isPersonal){
        this.$axios.get('http://127.0.0.1:8000/api/post/order/comment_number/all').then(response => {
          this.posts = []
          console.log("response.data !!!!")
          for (let i = 0; i < response.data.length; i++) {
            this.posts.push(
              {
                title: response.data[i].post_title,
                text: this.HtmlToText(response.data[i].post_content),
                tags: response.data[i].post_tag.split(' '),
                avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
                is_authenticated: response.data[i].is_organization,
                nickname: response.data[i].nick_name,
                comment_num: response.data[i].comment_number,
                id: response.data[i].id
              }
            )
          }
          console.log(this.posts)
        })
      }
      else{
        this.$axios.get('http://127.0.0.1:8000/api/post/user/' + this.user_id).then(response => {
          console.log("response.data")
          console.log(response.data)
          this.posts = []
          for (let i = 0; i < response.data.length; i++) {
            this.posts.push(
              {
                id: response.data[i].id,
                title: response.data[i].post_title,
                text: this.HtmlToText(response.data[i].post_content),
                tags: response.data[i].post_tag.split(' '),
                avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
                is_authenticated: response.data[i].is_organization,
                nickname: response.data[i].nick_name,
                comment_num: response.data[i].comment_number,
              }
            )
          }
          console.log(this.posts)
        })
      }
    },
    computed:{
      // Realize search 
      filteredPosts:function(){
        if (!this.search) return this.posts

        return this.posts.filter((post)=>{
          this.isTag = false;
          post.tags.forEach(element => {
            if (element.toLowerCase().match(this.search.toLowerCase())){
              this.isTag = true;
            }
          });
          return ( post.title.toLowerCase().match(this.search.toLowerCase()) || post.text.toLowerCase().match(this.search.toLowerCase()) || this.isTag )
        })
      }
    },
    methods:{
      // Change html to text
      HtmlToText: function(input) {
        console.log("TESTqqqq")
        console.log(input)
        this.text = input;
        this.text = this.text.replace(/<\/?.+?>/g, "");
        this.text = this.text.replace(/&nbsp;/g, "");
        console.log(this.text)
        return this.text
      },
      // Change the sort of the posts
      changeSort: function(){
        console.log(this.$store.state.userID)
        if(!this.isPersonal){
          this.sort.icon = !this.sort.icon
          this.sort.link = this.sort.icon ? 'http://127.0.0.1:8000/api/post/order/create_date/all' : 'http://127.0.0.1:8000/api/post/order/comment_number/all'
          this.$axios.get(this.sort.link).then(response => {
            this.posts = []
            for (let i = 0; i < response.data.length; i++) {
              this.posts.push(
                {
                  id: response.data[i].id,
                  title: response.data[i].post_title,
                  text: this.HtmlToText(response.data[i].post_content),
                  tags: response.data[i].post_tag.split(' '),
                  avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
                  is_authenticated: response.data[i].is_organization,
                  nickname: response.data[i].nick_name,
                  comment_num: response.data[i].comment_number,
                }
              )
            }
          })
        }else{
          this.sort.icon = !this.sort.icon
          this.sort.link = this.sort.icon ? ('http://127.0.0.1:8000/api/post/user/order/create_date/' + this.user_id) : ('http://127.0.0.1:8000/api/post/user/order/comment_number/' + this.user_id)
          this.$axios.get(this.sort.link).then(response => {
            this.posts = []
            for (let i = 0; i < response.data.length; i++) {
              this.posts.push(
                {
                  id: response.data[i].id,
                  title: response.data[i].post_title,
                  text: this.HtmlToText(response.data[i].post_content),
                  tags: response.data[i].post_tag.split(' '),
                  avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
                  is_authenticated: response.data[i].is_organization,
                  nickname: response.data[i].nick_name,
                  comment_num: response.data[i].comment_number,
                }
              )
            }
          })
        }
      },
    }

  }
</script>