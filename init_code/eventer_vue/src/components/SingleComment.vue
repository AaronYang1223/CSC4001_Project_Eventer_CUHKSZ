<template>
  <v-card>
    <v-card-actions>
      <v-row>
        <v-list-item class="grow">
          <v-list-item-avatar color="grey darken-3">
            <v-img
              alt="头像"
              src:="imgSrc"
            ></v-img>
            <!-- 头像地址 -->
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title> </v-list-item-title>
          </v-list-item-content>
          <div >
            <v-btn
              class="ma-2"
              text
              icon
              :color="likeColor"
              @click="like"
            >
              <v-icon>mdi-thumb-up</v-icon>
              {{likeNumber}}
            </v-btn>

            <v-btn
              class="ma-2"
              text
              icon
              :color="dislikeColor"
              @click="dislike"
            >
              <v-icon>mdi-thumb-down</v-icon>
              {{dislikeNumber}}
            </v-btn>
          </div>
        </v-list-item>
      </v-row>
    </v-card-actions>
      <v-card-text class="font-weight-bold">
        <v-list-item-title>
          {{userName}}
        </v-list-item-title>
      </v-card-text>
    <v-card-text>
      {{commentContent}}
    </v-card-text>
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
      likeColor: "grey lighten-1",
      dislikeColor: "grey lighten-1",
      userLike: false,
      userDislike: false,
      likeIdList: "",
      dislikeIdList: "",
      likeArray: [],
      dislikeArray: [],
    }
  },
  created: function () {
    this.userName  = this.CommentItem.commentUserID;//名字
    this.commentContent = this.CommentItem.commentText;
    this.imgSrc = this.CommentItem.commentUserAvatarsPath;
    this.likeNumber = this.CommentItem.likeNum;
    this.dislikeNumber = this.CommentItem.dislikeNum;
    this.likeIdList = this.CommentItem.likeId;
    this.dislikeIdList = this.CommentItem.dislikeId;
    this.likeArray = this.likeIdList.split(" ");
    this.dislikeArray = this.dislikeIdList.split(" ");
    if (this.likeArray.includes(this.$store.state.userID)) {
      this.likeColor = "blue lighten-1";
      this.userLike = true;
    }
    else if (this.dislikeArray.includes(this.$store.state.userID)) {
      this.dislikeColor = "red lighten-1";
      this.userDislike = true;
    }
  },
  methods: {
    like: function() {
      if (!this.userDislike) {
        if (!this.userLike) {
          this.likeColor = "blue lighten-1";
          this.likeNumber = this.likeNumber + 1;
          //用axios提交，在提交前最好先获取新的数量，避免别人在这时候已经点过了
          //注意提交user的id到服务器的likeId里
          this.userLike = true;
        }
        else{
          this.likeColor = "grey lighten-1";
          this.likeNumber = this.likeNumber - 1;
          //用axios提交，在提交前最好先获取新的数量，避免别人在这时候已经点过了
          //注意提交user的id到服务器的likeId里
          this.userLike = false;
        }
      }
    },
    dislike: function() {
      if (!this.userLike) {
        if (!this.userDislike) {
          this.dislikeColor = "red lighten-1";
          this.dislikeNumber = this.dislikeNumber + 1;
          //用axios提交，在提交前最好先获取新的数量，避免别人在这时候已经点过了
          //注意提交user的id到服务器的likeId里
          this.userDislike = true;
        }
        else{
          this.dislikeColor = "grey lighten-1";
          this.dislikeNumber = this.dislikeNumber - 1;
          //用axios提交，在提交前最好先获取新的数量，避免别人在这时候已经点过了
          //注意提交user的id到服务器的likeId里
          this.userDislike = false;
        }
      }
    },
  },
}
</script>

<style>

</style>
