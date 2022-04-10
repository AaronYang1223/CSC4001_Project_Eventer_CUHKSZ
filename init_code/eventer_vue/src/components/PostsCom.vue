<!-- TODO:增加超链接 -->
<template>

  <v-card
    class="mx-auto"
  >
    <!-- TODO:热点tag推送功能，见chip的例子 -->

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
            v-icon 
            dark
            color=blue
            >
              mdi-new-box
            </v-icon>
            <v-icon 
            v-if="!sort.icon" 
            v-icon 
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

            <v-card-title
              class="text-h5 font-weight-black "
              v-text="post.title"
              v-rainbow
            ></v-card-title>

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
                    mdi-heart
                  </v-icon>
                  <span class="subheading mr-2">{{post.like_num}}</span>
                  <span class="mr-1">·</span>
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
    data: () => ({
      posts: [
        // {
        //   title: 'Supermodel',
        //   text: "Turns out semicolon-less style is easier and safer in. 11111 11111 111111 11 111 111111 111 111111 111111 11111 1111111 11111111111111 111111111111",
        //   tags: ['Work', 'Home Improvement',] ,
        //   avatar: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
        //   is_authenticated: false,
        //   nickname: 'Foster the People',
        //   like_num: 111,
        //   comment_num: 11,
        // },
        // {
        //   title: 'Halcyon Days',
        //   text: "Turns out semicolon-less style is easier and safer in.22 222222222 22222 222222 2222 222 2222 2222 22222 222 2222222222 2222 22 222222 2222222 2222222 2222222 222222 2222 2222222 22222 22222222 222222 222222 2222",
        //   tags: ['Art', 'Tech', 'Creative Writing',] ,
        //   avatar: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
        //   is_authenticated: true,
        //   nickname: 'Ellie Goulding',
        //   like_num: 222,
        //   comment_num: 22,
        // },
        //   {
        //   title: 'Title',
        //   text: "Turns out semicolon-less style is easier and safer in .333 3333333 3333 3333333 33 33",
        //   tags: ['Art', 'Creative Writing',] ,
        //   avatar: 'https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light',
        //   is_authenticated: false,
        //   nickname: 'Evan You',
        //   like_num: 333,
        //   comment_num: 33,
        // },
      ],
    search:'',
    isTag : false,
    sort:{
      link: '',
      icon: false,
    }
    }),
    created(){
      this.$axios.get('http://127.0.0.1:8000/api/post/order/comment_number/all').then(response => {
        this.posts = []
        for (let i = 0; i < response.data.length; i++) {
          this.posts.push(
            {
              title: response.data[i].post_title,
              text: response.data[i].post_content,
              tags: response.data[i].post_tag.split(' '),
              avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
              is_authenticated: response.data[i].is_organization,
              nickname: response.data[i].nick_name,
              comment_num: response.data[i].comment_number,
            }
          )
        }
      })
    },
    computed:{
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
      changeSort: function(){
        this.sort.icon = !this.sort.icon
        this.sort.link = this.sort.icon ? 'http://127.0.0.1:8000/api/post/order/create_date/all' : 'http://127.0.0.1:8000/api/post/order/comment_number/all'
        this.$axios.get(this.sort.link).then(response => {
          this.posts = []
          for (let i = 0; i < response.data.length; i++) {
            this.posts.push(
              {
                title: response.data[i].post_title,
                text: response.data[i].post_content,
                tags: response.data[i].post_tag.split(' '),
                avatar: 'http://127.0.0.1:8000' + response.data[i].picture,
                is_authenticated: response.data[i].is_organization,
                nickname: response.data[i].nick_name,
                comment_num: response.data[i].comment_number,
              }
            )
          }
        })
      },
    }

  }
</script>