<template>

  <v-card
    class="mx-auto"
  >
    <!-- TODO:实现搜索功能 考虑v-app-bar组件-->
    <v-toolbar
      color="primary"
      dark
    >

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
    </v-toolbar>

    <v-container>
      <v-row dense>

        <!-- TODO:卡片颜色问题 -->
        <v-col
          v-for="(item, i) in items"
          :key="i"
          cols="12"
        >
          <v-card
            :color="item.color"
            dark
          >

            <v-card-title
              class="text-h5 font-weight-light"
              v-text="item.title"
            ></v-card-title>

            <!-- TODO:限制显示字数上限 -->
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
                    v-for="tag in item.tags"
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
                  :src="item.avatar"
                ></v-img>
              </v-list-item-avatar>

                <v-badge
                v-if="item.is_authenticated"
                color="accent"
                icon="mdi-hexagram"
                offset-x="30"
                offset-y="25"
              >
              </v-badge>      

                <v-list-item-content>
                  <v-list-item-title>{{item.nickname}}</v-list-item-title>
                </v-list-item-content>

                <v-row
                  align="center"
                  justify="end"
                >
                  <v-icon class="mr-1">
                    mdi-heart
                  </v-icon>
                  <span class="subheading mr-2">{{item.like_num}}</span>
                  <span class="mr-1">·</span>
                  <v-icon class="mr-1">
                    mdi-comment-multiple
                  </v-icon>
                  <span class="subheading">{{item.comment_num}}</span>
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
      items: [
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
    }),
  }
</script>