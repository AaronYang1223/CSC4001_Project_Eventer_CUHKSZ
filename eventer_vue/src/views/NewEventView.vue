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
    
    <v-btn 
      block
      @click="Submit"
    >
      提交
    </v-btn>
        
    {{file_info}}
  </div>
</template>

<script>
import RichTextEdit from '../components/RichTextEdit.vue'
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
    }
  },
  methods: {
    Submit: function() {
      this.content = this.$refs.textEditor.content;
      // content以html形式传输
      this.text = this.$refs.textEditor.text;
      // text以纯文本形式传输
    },
    addTheTag: function() {
      if (this.newTag != "" && (this.tags.indexOf(this.newTag) == -1)) {
        this.tags.push(this.newTag);
        this.newTag = "";
      }
    },
  },
}
</script>

<style>
.main-text {
  margin: 20px;
}
</style>