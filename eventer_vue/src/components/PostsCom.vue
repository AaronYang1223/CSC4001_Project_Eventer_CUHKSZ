<template>

  <v-card
    class="mx-auto"
  >
    <!-- TODO:实现搜索功能-->

    <v-container>
  
      <v-row dense>
        <v-col>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search Posts"
            color="primary"
            clearable
            outlined
            dense
          ></v-text-field>
        </v-col>

        <!-- TODO:卡片颜色问题 -->
        <v-col
          v-for="(post, i) in filteredPosts"
          :key="i"
          cols="12"
        >
          <v-card
            :color="post.color"
            dark
          >

            <v-card-title
              class="text-h5 font-weight-light"
              v-text="post.title"
            ></v-card-title>

            <!-- TODO:限制显示字数上限,利用filter -->
            <v-card-text class="text-h6 font-weight-bold">
              "Turns out semicolon-less style is easier and safer in ."
            </v-card-text>

            <v-row class="mx-3">
                <v-chip-group>
                  <v-chip
                    class="ma-2 font-weight-thin"
                    color="white"
                    outlined
                    dark
                    v-for="tag in post.tags"
                    :key="tag"
                  >
                  <v-icon left>
                    mdi-label
                  </v-icon>
                    {{ tag }}
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
        {
          color: '#26c6da',
          title: 'Supermodel',
          text: "Turns out semicolon-less style is easier and safer in .",
          tags: ['Work', 'Home Improvement',] ,
          avatar: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
          is_authenticated: false,
          nickname: 'Foster the People',
          like_num: 111,
          comment_num: 11,
        },
        {
          color: '#26c6da',
          title: 'Halcyon Days',
          text: "Turns out semicolon-less style is easier and safer in .",
          tags: ['Art', 'Tech', 'Creative Writing',] ,
          avatar: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          is_authenticated: true,
          nickname: 'Ellie Goulding',
          like_num: 222,
          comment_num: 22,
        },
          {
          color: '#26c6da',
          title: 'Title',
          text: "Turns out semicolon-less style is easier and safer in .",
          tags: ['Art', 'Creative Writing',] ,
          avatar: 'https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light',
          is_authenticated: false,
          nickname: 'Evan You',
          like_num: 333,
          comment_num: 33,
        },
      ],
    search:'',
    isTag : false,
    }),
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
    }
  }
</script>