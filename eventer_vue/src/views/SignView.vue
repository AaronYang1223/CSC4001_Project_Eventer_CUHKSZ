<template>
  <div>
    <div class="input">
      <v-layout align-center justify-center>
        <v-card min-width=600px max-width=700px>
          <v-card-text>
            <div v-bind:class="{ 'text_email': isActive, 'text_tip': isTip }"><h1 align="center">Sign In</h1></div>
            <v-text-field
            type="text" 
            label="Email Address"
            v-model="email" 
            v-bind:class="{ 'input_email0' : hasError }" 
            v-bind:disabled = "inputLock"
            v-on:click="cancelError" 
            id="inputEmail"
            :rules="[rules.required, rules.emailMatch]"
            />
            <v-text-field
            type="password" 
            label="Password"
            v-model="newpassword"
            v-bind:disabled = "inputLock"
            id="inputNewPassword"
            :rules="[rules.required, rules.min]"
            />
            <v-text-field
            type="password" 
            label="Password Repeat"
            v-model="newpassword2"
            v-bind:disabled = "inputLock"
            id="inputNewPassword2"
            :rules="[rules.required, rules.min, rules.samepassword]"
            />
            <v-row
            align="center"
            justify="space-around"
            >
              <v-col>
                <v-text-field v-model="codeIn" type="text" placeholder="输入验证码" class="input_number" />
              </v-col>
              <v-col>
                <v-btn depressed class="btn_number" v-bind:class="{gray:wait_timer>0}" @click="getCode(), snackbar = true">
                  <span 
                  class="num_green" 
                  v-show="showNum" 
                  v-bind:class="{num:wait_timer>0}"
                  >{{this.wait_timer + "s "}}</span>
                  <span 
                  class="span_number" 
                  v-bind:class="{gray_span:wait_timer>0}"
                  >{{ getCodeText() }}</span>
                </v-btn>
              </v-col>
            </v-row>
            <v-row
            align="center"
            justify="space-around"
            >
              <v-btn v-if="submitShow" depressed @click="submitNewPassword()">
                提 交
              </v-btn>
            </v-row>
          </v-card-text>
        </v-card>
      </v-layout>
    </div>
    <v-snackbar v-model="snackbar">
      {{ tip }}
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
    <v-snackbar v-model="snackbar2">
      验证码错误
      <template v-slot:action="{ attrs }">
        <v-btn
          color="pink"
          text
          v-bind="attrs"
          @click="snackbar2 = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tip: "用Email找回密码",
      isTip: false,
      isActive: true,
      showNum: false,
      wait_timer: false,
      hasError: false,
      email: "",
      emailExist: false,
      newpassword: "",
      newpassword2: "",
      snackbar: false,
      snackbar2: false,
      submitShow: false,
      inputLock: false,
      rules: {
        required: value => !!value || 'Required.',
        min: v => v.length >= 8 || 'Min 8 characters',
        samepassword:  value => value == this.newpassword || "Password not same",
        emailMatch: v => /.+@+cuhk|link+.+cuhk+./.test(v) || "E-mail must be valid",
      },
      codeGet: "123456",
      codeCorrect: false,
      codeIn: "",
      codeTime: true,
    }
},
methods: {
    cancelError: function() {
      this.hasError = false;
      this.isActive = true;
      this.isTip = false;
      this.tip = "注册账号";
    },
    getCode: function() {
      if (this.wait_timer > 0) {
        return false;
      }
      if (!this.email) {
        this.hasError = true;
        this.isActive = false;
        this.isTip = true;
        this.tip = "Email不能为空";
        return false;
      }
      if (
        !/.+@+cuhk|link+.+cuhk+./.test(this.email)
      ) {
        this.hasError = true;
        this.isActive = false;
        this.isTip = true;
        this.tip = "Email地址无效";
        return false;
      }
      if (this.newpassword == "") {
        this.tip = "密码不能为空";
        return false;
      }
      if (this.newpassword.length < 8) {
        this.tip = "密码不能少于8位";
        return false;
      }
      if (this.newpassword != this.newpassword2) {
        this.tip = "密码不一致";
        return false;
      }
      console.log(this.email);
      // 等待服务器返回邮箱存在否
      this.emailExist = false;
      if (this.emailExist) {
        this.tip = "邮箱已存在";
        return false;
      }

      this.tip = "已发送，请稍候";
      this.inputLock = true;
      this.submitShow = true;
      this.showNum = true;
      this.wait_timer = 10;
      var that = this;
      var timer_interval = setInterval(function() {
        if (that.wait_timer > 0) {
          that.wait_timer--;
        } else {
          clearInterval(timer_interval);
        }
      }, 1000);
      if (this.codeTime) {
        console.log("请求验证码");
        this.codeTime = false;
      }
      //在这里调取你获取验证码的ajax
    },
    getCodeText: function() {
      if (this.wait_timer > 0) {
        return "已发送";
      }
      if (this.wait_timer === 0) {
        this.showNum = false;
        this.codeTime = true;
        return "重新发送验证码！";
      }
      if (this.wait_timer === false) {
        return "发送验证码！";
      }
    },
    submitNewPassword: function() {
      console.log(this.codeIn);
      //更改逻辑!!
      this.codeCorrect = true;
      //从服务器获得
      if (!this.codeCorrect) {
        this.snackbar2 = true;
        return false;
      }
      console.log(this.email, this.newpassword);
    }

},

}
</script>

<style>

</style>