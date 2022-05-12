<template>
  <v-card
    tile
    outlined
  >
  <!-- 单个评论的展示 -->
  <!-- show single comment -->
    <v-card-actions>

      <v-row>
        <v-list-item class="grow">
          <v-list-item-avatar color="grey darken-3">
            <v-img
              alt="头像"
              :src="imgSrc"
            ></v-img>
            <!-- 头像地址 -->
          </v-list-item-avatar>

          <v-badge
            v-if="is_authenticated"
            color="accent"
            icon="mdi-hexagram"
            offset-x="30"
            offset-y="25"
          >
          </v-badge>  

          <v-list-item-content>
            <v-list-item-content>
                  <v-list-item-title>{{userNickname}}</v-list-item-title>
            </v-list-item-content>
          </v-list-item-content>
          <div >
            <!-- 点赞与点踩按钮，并且展示数字 -->
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
      userNickname:"",
      commentContent: "",
      likeNumber: 0,
      dislikeNumber: 0,
      likeColor: "grey",
      dislikeColor: "grey",
      userLike: false,
      userDislike: false,
      userCommented: false,
      likeIdList: "",
      dislikeIdList: "",
      hadCommentedId: "",
      likeArray: [],
      dislikeArray: [],
      hadCommentedArray: [],
      commentId: 1,
      type:"",
      is_authenticated: false,
    }
  },
  created: function () {
    this.userName  = this.CommentItem.commentUserID;//名字
    //console.log(this.userName);
    this.userNickname = this.CommentItem.commentUserNickname;
    this.commentContent = this.CommentItem.commentText;
    this.imgSrc = this.CommentItem.commentUserAvatarsPath;
    this.is_authenticated = this.CommentItem.is_authenticated;
    this.likeNumber = this.CommentItem.likeNum;
    this.dislikeNumber = this.CommentItem.dislikeNum;
    this.likeIdList = this.CommentItem.likeId;
    this.dislikeIdList = this.CommentItem.dislikeId;
    this.hadCommentedId = this.CommentItem.hadCommentedId
    this.likeArray = this.likeIdList.split(" ");
    //console.log(this.likeArray);
    this.dislikeArray = this.dislikeIdList.split(" ");
    //console.log(this.dislikeArray);
    this.hadCommentedArray = this.hadCommentedId.split(" ");
    console.log(this.CommentItem.hadCommentedId);
    this.commentId = this.CommentItem.commentId;
    this.type = this.CommentItem.type
    if(this.hadCommentedArray.includes(String(this.$store.state.userID))){
      this.userCommented = true;
      console.log("commented")
    }
    else{
      this.userCommented = false;
      console.log("not commented")
    }
    if (this.likeArray.includes(String(this.$store.state.userID))) {
      this.likeColor = "primary";
      this.userLike = true;
      this.userCommented = true;
    }
    else if (this.dislikeArray.includes(String(this.$store.state.userID))) {
      this.dislikeColor = "red";
      this.userDislike = true;
      this.userCommented = true;
    }
  },
  methods: {
    like: function() {
      if (!this.userDislike) {
        if (!this.userLike) {
          this.likeColor = "primary";
          this.likeNumber = this.likeNumber + 1;
          //用axios提交，在提交前最好先获取新的数量，避免别人在这时候已经点过了
          //注意提交user的id到服务器的likeId里
          //！提交的时候对象是this.commentId
          if(this.userCommented){
            this.$axios.put('http://127.0.0.1:8000/api/'+this.type+'/comment/like/add_change',{
              user_id:this.$store.state.userID,
              comment_id:this.commentId,
              is_like : '1'
            })
            .then((response)=>{
              console.log(response);
              this.userLike = true;
            });
          }else{
            this.$axios.post('http://127.0.0.1:8000/api/'+this.type+'/comment/like/add_change',{
                user_id:this.$store.state.userID,
                comment_id:this.commentId,
                is_like : '1'
            })
            .then((response)=>{
              console.log(response)
              this.userLike = true;
              this.userCommented = true;
            });
          }
          
        }
        else{
          this.likeColor = "grey";
          this.likeNumber = this.likeNumber - 1;
          //用axios提交，在提交前最好先获取新的数量，避免别人在这时候已经点过了
          //注意提交user的id到服务器的likeId里
          //！提交的时候对象是this.commentId
          this.$axios.put('http://127.0.0.1:8000/api/'+this.type+'/comment/like/add_change',{
              user_id:this.$store.state.userID,
              comment_id:this.commentId,
              is_like : '2'
          })
          .then((response)=>{
            console.log(response)
          });
          this.userLike = false;
        }
      }



    },
    dislike: function() {
      if (!this.userLike) {
        if (!this.userDislike) {
          this.dislikeColor = "red";
          this.dislikeNumber = this.dislikeNumber + 1;
          //用axios提交，在提交前最好先获取新的数量，避免别人在这时候已经点过了
          //注意提交user的id到服务器的likeId里
          //！提交的时候对象是this.commentId
          if(this.userCommented){
            this.$axios.put('http://127.0.0.1:8000/api/'+this.type+'/comment/like/add_change',{
              user_id:this.$store.state.userID,
              comment_id:this.commentId,
              is_like : '0'
            })
            .then((response)=>{
              console.log(response)
              this.userDislike = true;
            });
          }else{
            this.$axios.post('http://127.0.0.1:8000/api/'+this.type+'/comment/like/add_change',{
                user_id:this.$store.state.userID,
                comment_id:this.commentId,
                is_like : '0'
            })
            .then((response)=>{
              console.log(response)
              this.userDislike = true;
              this.userCommented = true;
            });
          }
          
        }
        else{
          this.dislikeColor = "grey";
          this.dislikeNumber = this.dislikeNumber - 1;
          //用axios提交，在提交前最好先获取新的数量，避免别人在这时候已经点过了
          //注意提交user的id到服务器的likeId里
          //！提交的时候对象是this.commentId
          this.$axios.put('http://127.0.0.1:8000/api/'+this.type+'/comment/like/add_change',{
              user_id:this.$store.state.userID,
              comment_id:this.commentId,
              is_like : '2'
          })
          .then((response)=>{
            console.log(response)
          });
          this.userDislike = false;
        }
      }
    },
  },
}
</script>

<style>

</style>
