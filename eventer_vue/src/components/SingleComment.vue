<template>
  <v-card>
    <v-card-actions>
      <v-list-item class="grow">
        <v-list-item-avatar color="grey darken-3">
          <v-img
            alt="头像"
            src=""
          ></v-img>
          <!-- 头像地址 -->
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title>{{UeserName}}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-card-actions>
    <v-card-text class="font-weight-bold">
      {{commentText}}
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: ['CommentID', 'PostID'],
  
  data() {
    return {
      TruePostID: "",
      TrueCommentID: "",
      commentText: "",
      imgSrc: "",
      UeserName: "",
    }
  },
  created: function () {
    console.log(this.CommentID);
    console.log(this.PostID);
    this.TrueCommentID = this.CommentID;
    this.TruePostID = this.PostID;
    //根据两个id确定所有值
    this.commentText = "Turns out semicolon-less style is easier and safer in TS because most gotcha edge cases are type invalid as well.";
    this.UeserName = "Evan You";
  },
}
</script>

<style>

</style>
