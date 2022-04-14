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
            <h1
              class="main-content"
            >
              {{topic}}
            </h1>
            <v-card-text>
              <span class="subheading">Post Tags:</span>
              <v-chip-group
                mandatory
                active-class="primary--text"
              >
                <v-chip
                  v-for="tag in tags"
                  :key="tag"
                  disabled
                  color="grey darken-3"
                  text-color="white"
                >
                  {{ tag }}
                </v-chip>
              </v-chip-group>
            </v-card-text>
            <v-divider></v-divider>

            <div class="main-content">
              <v-card flat>
                <div>
                  <span v-html="content">
                  </span>
                </div>
              </v-card>

              <v-card>
                <v-row class="main-content">
                  <v-col>
                    <v-text-field
                      label="Start Time"
                      prepend-icon="mdi-clock-time-four-outline"
                      :value="startTime"
                      readonly
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field
                      label="End Time"
                      prepend-icon="mdi-clock-time-four-outline"
                      :value="endTime"
                      readonly
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row class="main-content">
                  <v-col>
                    <v-text-field
                      label="Participant"
                      prepend-icon="mdi-account"
                      :value="partOverMax"
                      readonly
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <v-btn
                      color="yellow lighten-3"
                      block
                      @click="updateParticipant"
                      v-if="canJoin"
                    >
                      Join In
                    </v-btn>
                    <v-btn
                      color="grey lighten-3"
                      block
                      disabled
                      v-if="!canJoin"
                    >
                      Already End
                    </v-btn>
                  </v-col>
                </v-row>
              </v-card>

              <v-card
                v-if="canRating"
              >
                <v-row class="main-content">
                  <v-col>
                    Avarage: ({{ scoreAvg }})
                    <v-rating
                      v-model="scoreAvg"
                      background-color="grey"
                      color="yellow accent-4"
                      half-increments
                      hover
                      size="18"
                      readonly
                    ></v-rating>
                  </v-col>
                  <v-col>
                    Your: ({{ scoreNum }})
                    <div
                      @click="updateRating"
                    >
                      <v-rating
                        v-model="scoreNum"
                        background-color="grey"
                        color="yellow accent-4"
                        half-increments
                        hover
                        size="18"
                        :readonly="scoreReadOnly"
                      ></v-rating>
                    </div>
                  </v-col>
                </v-row>
              </v-card>

              <v-divider></v-divider>
              <v-banner
                class= "text-h5 font-weight-bold"
              >
                {{commentNumber}} Comment :
              </v-banner>

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
      topic: "Topic is Loading",
      content: "Content is Loading",
      newCommentText: "",
      commentsList: [],
      commentItem: {
        commentUserID: "这是id",
        commentUserAvatarsPath: "",
        commentText: "这是评论啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊",
        likeNum: 10,
        dislikeNum: 9,
        likeId: "1 2 3 4",
        dislikeId: "7 8 9",
        commentId: 1,
      },
      tip: "",
      tags: [],
      tagList: "",
      snackbar: false,

      //event 新数据
      startTime: "",
      endTime: "",
      participantNum: 0,
      maxParticipantNum: 0,
      partOverMax: "",
      coverPage: "",
      scoreNum: 0,
      scoreAvg: 0,
      //new
      isPrivate: false,
      privateID: "",

      //score new change
      canRating: true,
      scoreReadOnly: false,
      timeNow: "",
      //新数据已经评分的人的id存到scoreIds
      scoreIdList: [],
      scoreIds: "",
      //参加活动日期
      canJoin: true,
    }
  },
  created: function () {
    //this.$route.params.id
    //这是用户打开的post的id
    //用axios发送到后端检验一下这个post是不是存在
    //不存在就:  window.location.href = "/";

    //用axios获取isPrivate,把userid存到this.privateID
    if (this.isPrivate) {
      if (this.$store.state.userID != this.privateID) {
        window.location.href = "/";
      }
    }

    this.link = 'http://127.0.0.1:8000/api/activity/' + this.$route.params.id + '/comment'
    this.$axios.get(this.link).then(response => {
      this.topic = response.data.title
      this.content = response.data.content
      this.tagList = response.data.tag
      this.tags = this.tagList.split(" ")
      
      // "2022-04-12T14:00:00"
      this.startTime = response.data.start_time
      this.endTime = response.data.end_time
      this.participantNum = response.data.participant_num
      this.maxParticipantNum = response.data.max_participant_num
      this.partOverMax = response.data.part_max_num
      this.scoreNum = response.data.score_num
      this.scoreAvg = response.data.score_avg
      this.coverPage = 'http://127.0.0.1:8000' + response.data.cover_page
      this.commentNumber = response.data.comment_number
      this.pageLength = Math.ceil(this.commentNumber / 10)
      this.lastPageComentNum = this.commentNumber % 10
      if (this.commentNumber >= 10) {
        this.thisPageCommentNum = 10
      } else {
        this.thisPageCommentNum = this.commentNumber
      }

      for (let i = 0; i < response.data.comments.length; i++) {
        this.commentsList.push(
          {
            commentUserID: response.data.comments[i].user_id,
            commentUserAvatarsPath: 'http://127.0.0.1:8000' + response.data.comments[i].avatar,
            commentText: response.data.comments[i].content,
            likeNum: response.data.comments[i].like_num,
            dislikeNum: response.data.comments[i].dislike_num,
            likeId: response.data.comments[i].like_user,
            dislikeId: response.data.comments[i].dislike_user,
            commentId: response.data.comments[i].id,//这里改成后端id的名称
          }
        )
      }

      this.scoreIdList = response.data.score_list
      this.participant_list = response.data.participants_list

      this.canRating = response.data.is_outdate
      this.canJoin = !response.data.is_outdate
      if (this.canRating) {
      //用axios获得现在已经评价的人的id: this.scoreIds
        this.scoreIdList = this.scoreIds.split(" ");
        if (this.scoreIdList.includes(this.$store.state.userID)) {
          this.scoreReadOnly = true;
        }
      }
    })

    // //axios获取topic 正文内容 tagList
    // this.topic = "Topic Test";
    // this.content = "<p>123123123<strong>123213<em>12321312</em></strong></p> <p><strong><em>123213<s>123213123</s>123123</em></strong><em>123123</em></p> <p>123123<em>123213<strong>123213</strong></em></p> <p><s><em><strong>123123123</strong></em></s></p>";
    // this.tagList = "tag1 tag2 tag3";
    // this.tags = this.tagList.split(" ");

    // //event新元素
    // this.startTime = "XXXX.XX.XX XX:XX";
    // this.endTime = "XXXX.XX.XX XX:XX";
    // this.participantNum = 25;
    // this.maxParticipantNum = 100;
    // this.partOverMax = this.participantNum + " / " + this.maxParticipantNum;
    // this.scoreNum = 2;
    // this.scoreAvg = 2.2;
    // this.coverPage = "";

    // //axios获得一下目前post的评论数（写入this.commentNumber里），然后再操作
    // this.pageLength = Math.ceil(this.commentNumber/10);
    // this.lastPageComentNum = this.commentNumber%10;
    // if (this.commentNumber >= 10) {
    //   this.thisPageCommentNum = 10;
    // }
    // else {
    //   this.thisPageCommentNum = this.commentNumber;
    // }

    // //axios 把所有PostID对应的momment注入this.commentsList
    // //下面这部分是测试显示的，如果注入comment之后注释掉
    // for (let index = 0; index < this.commentNumber; index++) {
    //   this.commentsList.push(this.commentItem);
    // }
    // //控制rating能不能显示
    // //如果改了endTime记得把这部分判断移到修改endTime之前
    // this.timeNow = (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 23);
    // this.endTime = "2022-04-12T03:27:58.896683".substr(0, 23);
    // this.canRating = (this.endTime<this.timeNow);
    // //
    if (this.canRating) {
      //用axios获得现在已经评价的人的id: this.scoreIds
      this.scoreIdList = this.scoreIds.split(" ");
      if (this.scoreIdList.includes(this.$store.state.userID)) {
        this.scoreReadOnly = true;
      }
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
      location.reload();
      // 如果失败
      this.tip = "Comment Failed";
      this.snackbar = true;
      return false;
    },
    updateRating: function () {
      //axios提交this.scoreNum,计算后返回this.scoreAvg
      this.scoreReadOnly = true;
      this.scoreAvg = this.scoreNum - 1;
      //记得把this.$store.state.userID传到后端的已评价人id中this.scoreIds
    },
    updateParticipant: function () {
      //axios提交参加活动，根据返回值修改tip，同时在后端修改参与人数，前端获取新数据
      // this.participantNum
      // this.maxParticipantNum
      this.partOverMax = this.participantNum + " / " + this.maxParticipantNum;
      this.tip = "Event is Over";
      //活动已结束
      this.tip = "You already joined in";
      //已经参加了
      this.tip = "Event is Full";
      //人已经满了
      this.tip = "Succesee Join";
      //成功加入
      this.snackbar = true;
    },
  }
}
</script>

<style>
.main-content {
  margin: 10px;
}
.comment {
  margin: 5px;
}

</style>