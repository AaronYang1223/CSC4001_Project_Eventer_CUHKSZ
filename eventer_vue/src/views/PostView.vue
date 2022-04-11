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
                <!-- <CalendarCom v-bind:isPublic="isPublic" v-on:changeCalendar = "updateCalendar($event)"></CalendarCom> -->
              </v-card>

              <v-card flat>
                <div class="comment" v-for=" n in thisPageCommentNum" v-bind:key="n">
                  {{n+(page-1)*10}}
                  <single-comment :CommentID="123" :PostID="13">
                  </single-comment>
                </div>
                <!-- <PostsCom /> -->
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
    {{commentNumber}}<br/>
    {{pageLength}}<br/>
    {{lastPageComentNum}}<br/>
    {{thisPageCommentNum}}<br/>
    被提交的：{{submittest}}
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
      isPublic: false,
      page: 1,
      commentNumber: 22,
      pageLength: 0,
      lastPageComentNum: 0,
      topic: "这是标题好长啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊",
      content: "<p>123123123<strong>123213<em>12321312</em></strong></p> <p><strong><em>123213<s>123213123</s>123123</em></strong><em>123123</em></p> <p>123123<em>123213<strong>123213</strong></em></p> <p><s><em><strong>123123123</strong></em></s></p>",
      thisPageCommentNum: 0,
      newCommentText: "",

      submittest: "",
    }
  },
  created: function () {
    console.log("nihao");
    //获得目前post的帖子数
    this.pageLength = Math.ceil(this.commentNumber/10);
    this.lastPageComentNum = this.commentNumber%10;
    if (this.commentNumber >= 10) {
      this.thisPageCommentNum = 10;
    }
    else {
      this.thisPageCommentNum = this.commentNumber;
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
      console.log(this.newCommentText);
      this.submittest = this.newCommentText;
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