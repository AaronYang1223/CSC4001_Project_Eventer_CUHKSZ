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
            <v-list-item-title class="accent-4 red--text" v-if="i==0" >{{post.title}}</v-list-item-title>
            <v-list-item-title class="accent-4 orange--text" v-else-if="i==1">{{post.title}}</v-list-item-title>
            <v-list-item-title class="accent-4 amber--text" v-else-if="i==2">{{post.title}}</v-list-item-title>
            <v-list-item-title v-else v-html="post.title"></v-list-item-title>
            <v-list-item-subtitle v-html="post.content"></v-list-item-subtitle>
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
            <v-list-item-title class="accent-4 red--text" v-if="i==0" >{{post.title}}</v-list-item-title>
            <v-list-item-title class="accent-4 orange--text" v-else-if="i==1">{{post.title}}</v-list-item-title>
            <v-list-item-title class="accent-4 amber--text" v-else-if="i==2">{{post.title}}</v-list-item-title>
            <v-list-item-title v-else v-html="post.title"></v-list-item-title>
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