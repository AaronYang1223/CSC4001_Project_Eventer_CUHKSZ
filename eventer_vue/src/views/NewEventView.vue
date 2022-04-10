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
    <v-textarea
      rows = "6"
      counter
      outlined
      full-width
      shaped
      auto-grow
      type="text"
      label="Main"
      v-model="content"
      id="inputMain"
      :rules="[rules.required]"
    >
    </v-textarea>
    <rich-text-edit ref="textEditor">
    </rich-text-edit>
    text:{{text}}<br/>
    content:{{content}}<br/>
  <div>
    <span v-html="content"/>
  </div>
    date:{{date}}<br/>
    time:{{time}}<br/>
    date model:{{modal}}<br/>
    time modal:{{modal2}}<br/>

    <v-row>
      <v-col
        cols="12"
        sm="6"
        md="4"
      >
        <v-dialog
          ref="dialogDate"
          v-model="modal"
          :return-value.sync="date"
          persistent
          width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="date"
              label="Picker in dialog"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="date"
            scrollable
          >
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              @click="modal = false"
            >
              Cancel
            </v-btn>
            <v-btn
              text
              color="primary"
              @click="$refs.dialogDate.save(date)"
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
          ref="dialogTime"
          v-model="modal2"
          :return-value.sync="time"
          persistent
          width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="time"
              label="Picker in dialog"
              prepend-icon="mdi-clock-time-four-outline"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-time-picker
            v-if="modal2"
            v-model="time"
            full-width
          >
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              @click="modal2 = false"
            >
              Cancel
            </v-btn>
            <v-btn
              text
              color="primary"
              @click="$refs.dialogTime.save(time)"
            >
              OK
            </v-btn>
          </v-time-picker>
        </v-dialog>
      </v-col>
    </v-row>
    
    <v-btn 
      block
      @click="Submit"
    >
      提交
    </v-btn>
        
    
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
      time: null,
      menu2: false,
      modal2: false,
      date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      modal: false,
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