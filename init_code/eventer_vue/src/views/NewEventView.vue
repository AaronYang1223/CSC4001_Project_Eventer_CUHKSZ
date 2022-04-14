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
    <v-row>
      <v-col>
        <v-text-field
          rows = "1"
          type="text" 
          label="Tag"
          v-model="newTag"
          id="inputTopic"
        >
        </v-text-field>
      </v-col>
      <v-col>
        <v-btn
          @click="addTheTag"
        >
          Add Tag
        </v-btn>
      </v-col>
    </v-row>
    <v-chip-group
      mandatory
      active-class="primary--text"
    >
      <v-chip
        v-for="tag in tags"
        :key="tag"
      >
        {{ tag }}
      </v-chip>
    </v-chip-group>
    <rich-text-edit ref="textEditor">
    </rich-text-edit>
    text:{{text}}<br/>
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
    tags:{{tags}}<br/>

    {{startYear}}
    {{startMonth}}
    {{startDay}}
    {{startHour}}
    {{startMin}}
    {{endYear}}
    {{endMonth}}
    {{endDay}}
    {{endHour}}
    {{endMin}}

    <v-row>
      <v-col
        cols="11"
        sm="5"
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
    <v-spacer></v-spacer>
      <v-col
        cols="11"
        sm="5"
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
    </v-row>

    <v-row>
      <v-col
        cols="11"
        sm="5"
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
    <v-spacer></v-spacer>
      <v-col
        cols="11"
        sm="5"
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
    </v-row>


    <v-file-input
      v-model="file_info"
      label="Event Picture"
      filled
      dense
      show-size
      accept="image/*"
      prepend-icon="mdi-camera"
    ></v-file-input>
    <div>
      <v-row>
        <v-col>
          <v-text-field
            label="Participant"
            prepend-icon="mdi-account"
            v-model="maxPartNum"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-checkbox
            v-model="eventIsPrivate"
            :label="`Set This Event Private`"
          ></v-checkbox>
        </v-col>
        <v-col>
          <div v-if="userIsOrg == true">
            <v-checkbox
              v-model="eventIsPublic"
              :label="`Set This Event Public`"
            ></v-checkbox>
          </div>
        </v-col>
      </v-row>
    </div>
    
    <v-btn 
      block
      @click="Submit"
    >
      提交
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
  components: { RichTextEdit },
  data() {
    return {
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
    }
  },

  created: function () {
    //通过axios获得用户是不是组织用户
    this.userIsOrg = this.$store.state.userIsOrganization;//写完axios注释了
    console.log(this.userIsOrg);
  },

  methods: {
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
      if (this.startYear > this.endYear) {
        this.tip = "Your Date and Time is invalid";
        this.snackbar = true;
        return false;
      }
      else if (this.startMonth > this.endMonth) {
        this.tip = "Your Date and Time is invalid";
        this.snackbar = true;
        return false;
      }
      else if (this.startDay > this.endDay) {
        this.tip = "Your Date and Time is invalid";
        this.snackbar = true;
        return false;
      }
      else if (this.startHour > this.endHour) {
        this.tip = "Your Date and Time is invalid";
        this.snackbar = true;
        return false;
      }
      else if (this.startMin > this.endMin) {
        this.tip = "Your Date and Time is invalid";
        this.snackbar = true;
        return false;
      }
      let data = new FormData();
      let cover_page = {};
      cover_page = this.file_info;
      data.append("cover_page",cover_page)
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
          axios.put('api/activity/update_image/' + response.data.id, data)
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
</style>