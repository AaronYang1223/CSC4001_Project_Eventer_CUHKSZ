<template>
  <div class="home">
    <v-container>
      <v-row no-gutters>
        <v-col 
          cols="12" xs="12" sm="8" md="8" 
        >
          <v-card
            class="pa-2 mx-1 mt-2"
            outlined
            tile
          >
            <v-banner
              class= "text-h5 font-weight-bold"
              color="primary"
              elevation="2"
              outlined
              rounded
            >
              {{topic}}
            </v-banner>

            <div class="main-content">
              <v-card flat>
                <div>
                  <span v-html="content">
                  </span>
                </div>
              </v-card>

              <v-card flat>
                <div class="comment" v-for=" n in thisPageCommentNum" v-bind:key="n">
                  <single-comment :CommentItem = commentsList[n+(page-1)*10-1]>
                    <!-- 传数组 -->
                  </single-comment>
                </div>
              </v-card>

              <v-card flat>
                <div class="text-center">
                  <v-pagination
                    v-model="page"
                    :length="pageLength"
                    :total-visible="7"
                    @input="calculateNum"
                  ></v-pagination>
                </div>
              </v-card>

              <v-textarea
                name="input-7-1"
                filled
                label="New Comment"
                auto-grow
                v-model="newCommentText"
              ></v-textarea>
              <v-btn
                @click="SubmitNewComment"
              >
                Submit New Comment!
              </v-btn>
            </div>
              

          </v-card>
        </v-col>

        <!-- 确定这个part的手机端适配方式：隐藏？ -->
        <v-col 
          cols="12" xs="12" sm="4" md="4"
          
        >
          <v-card
            class="pa-2 mx-1 mt-2"
            outlined
            tile
          >
            <!-- <WeatherCom /> -->
            <div style="background:#000; color:#FFF">第五块</div>
            <!-- <NewsCom /> -->
            <div style="background:#000; color:#FFF">第六块</div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <!-- <v-btn @click="test">测试</v-btn> -->
    <!-- {{commentNumber}}<br/>
    {{pageLength}}<br/>
    {{lastPageComentNum}}<br/>
    {{thisPageCommentNum}}<br/>

    <br/>{{commentItem}}
    <br/>{{commentsList}} -->
    <v-snackbar v-model="snackbar">
      {{tip}}
      <template v-slot:action="{ attrs }">
        <v-btn
          color="pink"
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>

  </div>
</template>

<script>
import SingleComment from '../components/SingleComment.vue';
export default {
  components: { SingleComment },
  name: 'HomepageView',
  data () {
    return {
      tab: null,
      page: 1,
      commentNumber: 77,
      pageLength: 0,
      lastPageComentNum: 0,
      thisPageCommentNum: 0,
      topic: "这是标题好长啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊",
      content: "<p>123123123<strong>123213<em>12321312</em></strong></p> <p><strong><em>123213<s>123213123</s>123123</em></strong><em>123123</em></p> <p>123123<em>123213<strong>123213</strong></em></p> <p><s><em><strong>123123123</strong></em></s></p>",
      newCommentText: "",
      commentsList: [],
      commentItem: {
        commentUserID: "这是id",
        commentUserAvatarsPath: "",
        commentText: "这是评论",
        likeNum: 10,
        dislikeNum: 9,
      },
      tip: "",
      snackbar: false,
    }
  },
  created: function () {
    //axios获得目前post的评论数，然后再操作
    this.pageLength = Math.ceil(this.commentNumber/10);
    this.lastPageComentNum = this.commentNumber%10;
    if (this.commentNumber >= 10) {
      this.thisPageCommentNum = 10;
    }
    else {
      this.thisPageCommentNum = this.commentNumber;
    }
    //axios 把所有PostID对应的momment注入this.commentsList
    for (let index = 0; index < this.commentNumber; index++) {
      this.commentsList.push(this.commentItem);
    }
  },
  methods:{
    calculateNum: function(){
      if (this.page == this.pageLength) {
        this.thisPageCommentNum = this.lastPageComentNum;
      }
      else {
        this.thisPageCommentNum = 10;
      }
    },
    SubmitNewComment: function(){
      if (this.newCommentText == "") {
        this.tip = "No Comment";
        this.snackbar = true;
        return false;
      }
      //用axios上传
      console.log(this.newCommentText);
      console.log(this.$store.state.userID);
      console.log(this.$store.state.userNickName);
      console.log(this.$route.params.id);
      // axios 上传如果成功
      this.tip = "Comment Success";
      this.snackbar = true;
      // location.reload();
      // 如果失败
      // this.tip = "Comment Failed";
      // this.snackbar = true;
      // return false;
    }
  }
}
</script>

<style>
.main-content {
  margin: 10px;
}
.comment {
  margin: 5px;
  border:1px solid #00F
}

</style>