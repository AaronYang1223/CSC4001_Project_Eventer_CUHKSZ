<template>
  <div class="main-text">

    <v-text-field
      rows = "1"
      type="text" 
      label="Topic"
      v-model="topic"
      id="inputTopic"
      :rules="[rules.required]"
    >
    </v-text-field>
    
    <v-row justify="center" align="center" class="mt-1">
      <v-col 
        cols="12" xs="12" sm="3" md="3"
      >
        <v-text-field
          rows = "1"
          type="text" 
          label="Tag"
          v-model="newTag"
          id="inputTopic"
        >
        </v-text-field>
      </v-col>
      <v-col 
        cols="12" xs="12" sm="1" md="1"
      >
      <!-- Add and Show the tags -->
        <v-btn
          block 
          tile 
          color="primary"
          depressed
          textarea
          outlined
          small
          @click="addTheTag"
        >
          Add Tag
        </v-btn>
      </v-col>
        <v-col 
        cols="12" xs="0" sm="1" md="1"
        class="hidden-xs-only"
      >
        </v-col>
      <v-col 
        cols="12" xs="12" sm="7" md="7"
      >
    <v-chip-group
      active-class="primary--text"
    >
      <v-chip
        class="font-weight-black"
        outlined
        v-for="tag in tags"
        :key="tag"
        color="primary"
        small
      >
      <v-icon left>
        mdi-label
      </v-icon>
        {{ tag | to-uppercase}}
      </v-chip>
    </v-chip-group>
    </v-col>
    </v-row>

    <v-divider></v-divider>
        <v-card
        flat
        >
        <!-- Upload the Banner picture to back end -->
          <v-list-item-content class="justify-center avatar">
            <div class="text-center mt-4">
              <v-btn
                color="primary"
                outlined
                @click="uploadClick"
                block
                tile
              >
                <v-icon small>mdi-pencil</v-icon>
                  Upload Banner
                <input
                  id="upload"
                  type="file" 
                  class="input-file" 
                  style="width:200px; height:20px;" 
                  @change="changeImage($event)" 
                  ref="avatarInput" 
                  accept="image/gif,image/jpeg,image/jpg,image/png"
                >
              </v-btn>
            </div>
            <v-img 
              :src="previewImg"
              :max-height="600"
              contain
            >
            </v-img>
          </v-list-item-content>
        </v-card>



    <rich-text-edit ref="textEditor">
    </rich-text-edit>

    <!-- text:{{text}}<br/>
    content:{{content}}<br/>
  <div>
    <span v-html="content"/>
  </div>
    <br/>
    dateStart:{{dateStart}}<br/>
    dateEnd:{{dateEnd}}<br/>
    start time:{{timeStart}}<br/>
    end time:{{timeEnd}}<br/>
    start date model:{{modalStartDate}}<br/>
    end date model:{{modalEndDate}}<br/>
    start time modal:{{modalStartTime}}<br/>
    end time modal:{{modalEndTime}}<br/>
    tags:{{tags}}<br/> -->

<!-- 一些调试信息，打印出所有信息 -->
    <!-- {{startYear}}
    {{startMonth}}
    {{startDay}}
    {{startHour}}
    {{startMin}}
    {{endYear}}
    {{endMonth}}
    {{endDay}}
    {{endHour}}
    {{endMin}}

    {{timeFront}}
    {{timeLast}} -->

  <!-- choose the dialog and date -->
  <!-- 选择日期和时间 -->
    <v-row justify="center" align="center" class="mt-1">
      <v-col 
        cols="12" xs="12" sm="6" md="6"
      >
        <v-dialog
          ref="dialogStartDate"
          v-model="modalStartDate"
          :return-value.sync="dateStart"
          persistent
          width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="dateStart"
              label="Start Day"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="dateStart"
            scrollable
          >
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              @click="modalStartDate = false"
            >
              Cancel
            </v-btn>
            <v-btn
              text
              color="primary"
              @click="$refs.dialogStartDate.save(dateStart)"
            >
              OK
            </v-btn>
          </v-date-picker>
        </v-dialog>
      </v-col>
      <v-col 
        cols="12" xs="12" sm="6" md="6"
      >
        <v-dialog
          ref="dialogEndDate"
          v-model="modalEndDate"
          :return-value.sync="dateEnd"
          persistent
          width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="dateEnd"
              label="End Date"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="dateEnd"
            scrollable
          >
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              @click="modalEndDate = false"
            >
              Cancel
            </v-btn>
            <v-btn
              text
              color="primary"
              @click="$refs.dialogEndDate.save(dateEnd)"
            >
              OK
            </v-btn>
          </v-date-picker>
        </v-dialog>
      </v-col>
      <v-col 
        cols="12" xs="12" sm="6" md="6"
      >
        <v-dialog
          ref="dialogStartTime"
          v-model="modalStartTime"
          :return-value.sync="timeStart"
          persistent
          width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="timeStart"
              label="Start Time"
              prepend-icon="mdi-clock-time-four-outline"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-time-picker
            v-if="modalStartTime"
            v-model="timeStart"
            full-width
          >
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              @click="modalStartTime = false"
            >
              Cancel
            </v-btn>
            <v-btn
              text
              color="primary"
              @click="$refs.dialogStartTime.save(timeStart)"
            >
              OK
            </v-btn>
          </v-time-picker>
        </v-dialog>
      </v-col>
      <v-col 
        cols="12" xs="12" sm="6" md="6"
      >
        <v-dialog
          ref="dialogEndTime"
          v-model="modalEndTime"
          :return-value.sync="timeEnd"
          persistent
          width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="timeEnd"
              label="End Time"
              prepend-icon="mdi-clock-time-four-outline"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-time-picker
            v-if="modalEndTime"
            v-model="timeEnd"
            full-width
          >
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              @click="modalEndTime = false"
            >
              Cancel
            </v-btn>
            <v-btn
              text
              color="primary"
              @click="$refs.dialogEndTime.save(timeEnd)"
            >
              OK
            </v-btn>
          </v-time-picker>
        </v-dialog>
      </v-col>
      <v-col 
        cols="12" xs="12" sm="3" md="3"
      >
      <!-- input the Participant number -->
      <!-- 输入参与人数 -->
          <v-text-field
            label="Participant"
            prepend-icon="mdi-account"
            v-model="maxPartNum"
          ></v-text-field>
        </v-col>
      <!-- Set the event private or public -->
      <!-- 设置活动私人或者公共活动 -->
        <v-col 
          cols="12" xs="12" sm="3" md="3"
        >
          <v-checkbox
            v-model="eventIsPrivate"
            :label="`Set This Event Private`"
          ></v-checkbox>
        </v-col>

        <v-col 
          cols="12" xs="12" sm="3" md="3"
          v-if="userIsOrg == true"
        >
          <v-checkbox
            v-model="eventIsPublic"
            :label="`Set This Event Public`"
          ></v-checkbox>
        </v-col>
</v-row>
    
    <v-btn 
      tile 
      color="primary"
      depressed
      block 
      @click="Submit"
    >
      Submit
    </v-btn>
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
        
    {{file_info}}
  </div>
</template>

<script>
import RichTextEdit from '../components/RichTextEdit.vue'
import axios from 'axios'



export default {
  props: ["uploadType", "imgWidth", "imgHeight"],
  components: { RichTextEdit},
  data() {
    
    return {
      avatar: '',
      file: '',
      user_id: '',
      topic: "",
      main: "",
      content: "",
      text: "",
      newTag: "",
      tags: [
      ],
      tagList: "",
      file_info: null,
      timeStart: null,
      timeEnd: null,
      menu2: false,
      modalStartTime: false,
      modalEndTime: false,
      dateStart: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      dateEnd: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      modalStartDate: false,
      modalEndDate: false,
      rules: {
        required: value => !!value || 'Required.',
        min: v => v.length >= 8 || 'Min 8 characters',
        max: v => v.length <= 18 || 'Max 18 characters',
        samepassword:  value => value == this.newpassword || "Password not same",
        emailMatch: v => /.+@+cuhk|link+.+cuhk+./.test(v) || "E-mail must be valid",
      },

      //新元素
      snackbar: false,
      tip: "",
      userIsOrg: false,
      eventIsPublic: false,//是否公共
      eventIsPrivate: false,//是否私人
      maxPartNum: 0,
      eventId: "",
      newPath: "",

      //新判断元素
      startYear: "",
      startMonth: "",
      startDay: "",
      startHour: "",
      startMin: "",
      endYear: "",
      endMonth: "",
      endDay: "",
      endHour: "",
      endMin: "",

      //图片预览
      previewImg: undefined,

      //时间判断
      timeFront: "",
      timeLast: "",
    }
  },

  created: function () {
    //通过axios获得用户是不是组织用户
    this.userIsOrg = this.$store.state.userIsOrganization;//写完axios注释了
    console.log(this.userIsOrg);
    this.avatar = this.$store.state.avatar
  },

  methods: {
    uploadClick: function(){
      let uploadbtn = this.$refs.avatarInput
      uploadbtn.click()
    },
    changeImage: function(e){
      let file = e.target.files[0];
      if(file) {
        this.file = file
        this.previewImg = URL.createObjectURL(this.file)
      }
    },
    Submit: function() {
      this.content = this.$refs.textEditor.content;
      // content以html形式传输
      this.text = this.$refs.textEditor.text;
      // text以纯文本形式传输



      for (let index = 0; index < this.tags.length; index++) {
        this.tagList = this.tagList + " " + this.tags[index];
      }
      if (this.tagList == "") {
        this.tip = "tag can't be empty";
        this.snackbar = true;
        return false;
      }
      if (this.topic == "") {
        this.tip = "topic can't be empty";
        this.snackbar = true;
        return false;
      }
      if (this.content == "") {
        this.tip = "content can't be empty";
        this.snackbar = true;
        return false;
      }
      if (this.timeStart == null || this.timeEnd == null) {
        this.tip = "time can't be empty";
        this.snackbar = true;
        return false;
      }
      // if (this.maxPartNum <= 0 || this.maxPartNum%1 == 0) {
      if (this.maxPartNum <= 0) {
        this.tip = "Participant number invaild";
        this.snackbar = true;
        return false;
      }
      this.startYear = this.dateStart.split("-")[0];
      this.startMonth = this.dateStart.split("-")[1];
      this.startDay = this.dateStart.split("-")[2];
      this.startHour = this.timeStart.split(":")[0];
      this.startMin = this.timeStart.split(":")[1];
      this.endYear = this.dateEnd.split("-")[0];
      this.endMonth = this.dateEnd.split("-")[1];
      this.endDay = this.dateEnd.split("-")[2];
      this.endHour = this.timeEnd.split(":")[0];
      this.endMin = this.timeEnd.split(":")[1];
      this.timeFront = this.dateStart+this.timeStart;
      this.timeLast = this.dateEnd+this.timeEnd;
      if (this.timeFront>this.timeLast) {
        this.tip = "Your Date and Time is invalid";
        this.snackbar = true;
        return false;
      }

      let files = this.$refs.avatarInput.files
      let fileData = {}
      //make sure only update one file
      if(files instanceof Array) {
        fileData = files[0]
      } else {
        fileData = this.file
      }
      console.log('fileData', typeof fileData, fileData)
      let data = new FormData()
      data.append('cover_page', fileData)
      data.append('operaType', this.uploadType)
      console.log('data', typeof data, data)

      // data.append("organizer_id",this.$store.state.userID)
      // data.append("tag",this.tags.join(" "))
      // data.append("start_time",this.dateStart + " " + this.timeStart)
      // data.append("end_time",this.dateEnd + " " + this.timeEnd)
      // data.append("title",this.topic)
      // data.append("content",this.content)
      // data.append("max_participant_num",this.maxPartNum)
      // data.append("is_public",this.eventIsPublic)
      // data.append("is_private",this.eventIsPrivate)
      //axios 提交 tagList userid starttime(由date和time合并) endtime title comtent coverpage(还没做好) maxPartNum isPublic
      
      axios.post('api/activity/create',{
          organizer_id:this.$store.state.userID,
          tag:this.tags.join(" "),
          start_time:this.dateStart + " " + this.timeStart,
          end_time:this.dateEnd + " " + this.timeEnd,
          title:this.topic,
          content: this.content,
          //cover_page:this.file_info,
          max_participant_num: this.maxPartNum,
          is_public: this.eventIsPublic,
          is_private:this.eventIsPrivate,
      })
      .then((response)=>{
        if(response.data['code']=='101'){
          //this.codeCorrect = true;
          console.log("error");
          console.log(this.file_info)
        }
        else {
          console.log("ok");
          this.newPath = "/event/"+response.data.id;
          axios.post('api/activity/update_image/' + response.data.id, data)
          .then(response=>{
            console.log(response)
          });
          window.location.href = this.newPath;
          }
      });

      //提交之后,从服务器获得event id
      // this.newPath = "/event/"+this.eventId,
      

    },
    addTheTag: function() {
      if (this.newTag == "") {
        this.tip = "Tag can't be empty";
        this.snackbar = true;
        return false;
      }
      if (this.newTag.indexOf(" ") != -1) {
        this.tip = "Tag can't have space";
        this.snackbar = true;
        return false;
      }
      if (this.newTag.length >= 10) {
        this.tip = "Tag can't longer than 10 char";
        this.snackbar = true;
        return false;
      }
      if (this.tags.indexOf(this.newTag) != -1) {
        this.tip = "Tag can't repeat";
        this.snackbar = true;
        return false;
      }
      this.tags.push(this.newTag);
      this.newTag = "";
    },
  },
}
</script>

<style>
.main-text {
  margin: 20px;
}
#upload{
    height: 0;
    width: 0;
    visibility: hidden;
}
</style>

<style lang="less" scope>
.avatar {
    position: relative;
    .input-file {
        position: absolute;
        top: 0;
        left: 0;
        opacity: 0;
        cursor: pointer;
    }
    .v-btn__content {
      white-space: normal;
    }
}
</style>