<template>
  <v-card>
    <v-card-actions>
      <v-list-item class="grow">
        <v-list-item-avatar color="grey darken-3">
          <v-img
            alt="头像"
            src:="imgSrc"
          ></v-img>
          <!-- 头像地址 -->
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title>{{userName}}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-card-actions>
    <v-card-text class="font-weight-bold">
      {{commentContent}}
    </v-card-text>
    like:{{likeNumber}}
    dislike:{{dislikeNumber}}
  </v-card>
</template>

<script>
export default {
  props: ['CommentItem'],
  
  data() {
    return {
      imgSrc: "",
      userName: "",
      commentContent: "",
      likeNumber: 0,
      dislikeNumber: 0,
    }
  },
  created: function () {
    this.userName  = this.CommentItem.commentUserID;//名字
    this.commentContent = this.CommentItem.commentText;
    this.imgSrc = this.CommentItem.commentUserAvatarsPath;
    this.likeNumber = this.CommentItem.likeNum;
    this.dislikeNumber = this.CommentItem.dislikeNum;
  },
}
</script>

<style>

</style>
