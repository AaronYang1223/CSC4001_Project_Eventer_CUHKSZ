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
        commentUserNickname:"",
        commentUserAvatarsPath: "",
        commentText: "这是评论啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊",
        likeNum: 10,
        dislikeNum: 9,
        likeId: "1 2 3 4",
        dislikeId: "7 8 9",
        commentId: 1,
        type:"post"
      },
      tip: "",
      tags: [],
      tagList: "",
      snackbar: false,
    }
  },
  created: function () {
    //this.$route.params.id
    //这是用户打开的post的id
    //用axios发送到后端检验一下这个post是不是存在
    //不存在就:  window.location.href = "/";
    
    //axios获取topic 正文内容 tagList
    this.$axios.get('http://127.0.0.1:8000/api/post/'+ this.$route.params.id,{
          // params:{
          //   id:this.$route.params.id
          // }
      })
      .then((response)=>{
        this.topic = response.data.post_title;
        this.content = response.data.post_content;
        this.tagList = response.data.post_tag;
        this.tags = this.tagList.split(" ");
        this.commentNumber = response.data.comment_number;
        //console.log(response.data.comments.length);
        for (let i = 0; i < response.data.comments.length; i++) {
          console.log(response.data.comments[i]['user_id']);
          console.log('http://127.0.0.1:8000'+response.data.comments[i]['avatar']);
          console.log(response.data.comments[i]['content']);
          console.log(response.data.comments[i]['like_num']);
          console.log(response.data.comments[i]['dislike_num']);
          console.log(response.data.comments[i]['like_user']);
          console.log(response.data.comments[i]['dislike_user']);
          // this.commentItem['commentUserID'] = response.data.comments[i]['user_id'];
          // this.commentItem['commentUserAvatarsPath'] = response.data.comments[i]['avatar'];
          // this.commentItem['commentTexth'] = response.data.comments[i]['content'];
          // this.commentItem['likeNum'] = response.data.comments[i]['like_num'];
          // this.commentItem['dislikeNum'] = response.data.comments[i]['dislike_num'];
          // this.commentItem['likeId'] = response.data.comments[i]['like_user'];
          // this.commentItem['dislikeId'] = response.data.comments[i]['dislike_user'];
          this.commentsList.push(
              {commentUserID: String(response.data.comments[i]['user_id']),
              commentUserNickname: String(response.data.comments[i]['user_nickname']),
              commentUserAvatarsPath: 'http://127.0.0.1:8000'+response.data.comments[i]['avatar'],
              commentText: response.data.comments[i]['content'],
              likeNum: response.data.comments[i]['like_num'],
              dislikeNum: response.data.comments[i]['dislike_num'],
              likeId: response.data.comments[i]['like_user'],
              dislikeId: response.data.comments[i]['dislike_user'],
              commentId: response.data.comments[i]['id'],   //这里改成后端id的名称
              type:'post'
              })
          console.log(this.commentsList)
        }
        
        console.log(this.commentNumber)
        this.pageLength = Math.ceil(this.commentNumber/10);
        this.lastPageComentNum = this.commentNumber%10;
        if (this.commentNumber >= 10) {
          this.thisPageCommentNum = 10;
        }
        else {
        this.thisPageCommentNum = this.commentNumber;
        }
      });

    //this.topic = "Topic Test";
    //this.content = "<p>123123123<strong>123213<em>12321312</em></strong></p> <p><strong><em>123213<s>123213123</s>123123</em></strong><em>123123</em></p> <p>123123<em>123213<strong>123213</strong></em></p> <p><s><em><strong>123123123</strong></em></s></p>";
    //this.tagList = "tag1 tag2 tag3";
    
    console.log(this.tags)
    //axios获得一下目前post的评论数（写入this.commentNumber里），然后再操作
    

    //axios 把所有PostID对应的momment注入this.commentsList
    //下面这部分是测试显示的，如果注入comment之后注释掉
    // for (let index = 0; index < this.commentNumber; index++) {
    //   this.commentsList.push(this.commentItem);
    // 
    
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
      
      this.$axios.post('http://127.0.0.1:8000/api/post/comment/create',{
          user_id:this.$store.state.userID,
          post_id:this.$route.params.id,
          content:this.newCommentText,

      })
      .then((response)=>{
        
        console.log(response)
        //console.log(this.taglist)
        this.tip = "Comment Success";
        this.snackbar = true;
        location.reload();
      });
      //用axios上传
      // console.log(this.newCommentText);
      // console.log(this.$store.state.userID);
      // console.log(this.$store.state.userNickName);
      // console.log(this.$route.params.id);
      // axios 上传如果成功
      
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
}

</style>