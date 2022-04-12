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
    <!-- <v-textarea
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
    </v-textarea> -->
    <rich-text-edit ref="textEditor">
    </rich-text-edit>
    t:{{text}}
    c:{{content}}
    
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

      //新元素
      snackbar: false,
      tip: "",
      userIsOrg: false,
      tagList: "",
      postId: "",
      newPath: "",

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
      //提交 id taglist content topic

      //提交之后,从服务器获得post id
      // this.newPath = "/post/"+this.postId,
      // window.location.href = this.newPath;

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