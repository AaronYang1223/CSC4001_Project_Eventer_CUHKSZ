<template>
  <div>
    <div>
      <v-layout align-center justify-center py-5>
        <v-card  class="px-2 pb-3" max-width=900px>
          <v-card-text>
            <h1 align="center">
              <span style="color:blue">S</span>ign <span style="color:blue">I</span>n
            </h1>
            <br/>
            <v-row>
              <v-col>
              <!-- 输入邮箱 -->
                <v-text-field
                  type="text" 
                  label="Email Address"
                  v-model="email"
                  v-bind:disabled = "inputLock"
                  id="inputEmail"
                  :rules="[rules.required, rules.emailMatch]"
                >
                </v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
              <!-- 输入密码 -->
                <v-text-field
                  type="text" 
                  label="Password"
                  v-model="newpassword"
                  v-bind:disabled = "inputLock"
                  id="inputNewPassword"
                  :rules="[rules.required, rules.min, rules.max]"
                >
                </v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
              <!-- 再次输入密码 -->
                <v-text-field
                  type="text" 
                  label="Password Repeat"
                  v-model="newpassword2"
                  v-bind:disabled = "inputLock"
                  id="inputNewPassword2"
                  :rules="[rules.required, rules.min, rules.samepassword]"
                >
                </v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <!-- 输入First/Last name  -->
              <v-col>
                <v-text-field
                  type="text" 
                  label="First Name"
                  v-model="firstname"
                  v-bind:disabled = "inputLock"
                  id="inputFirstname"
                  :rules="[rules.required, rules.max]"
                >
                </v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                  type="text" 
                  label="Last Name"
                  v-model="lastname"
                  v-bind:disabled = "inputLock"
                  id="inputLastname"
                  :rules="[rules.required, rules.max]"
                >
                </v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  type="text" 
                  label="Nick Name"
                  v-model="nickname"
                  v-bind:disabled = "inputLock"
                  id="inputNickname"
                  :rules="[rules.required, rules.max]"
                >
                </v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  type="text" 
                  label="Verification Code"
                  v-model="codeIn" 
                  id="inputVerifyCode"
                >
                </v-text-field>
              </v-col>
              <v-col>
                <v-btn
                  v-bind:class="{gray:wait_timer>0}" 
                  @click="getCode() 
                  snackbar = true"
                >
                  <span 
                    v-show="showNum" 
                    v-bind:class="{num:wait_timer>0}"
                  >
                  {{this.wait_timer + "s "}}
                  </span>
                  <span 
                    v-bind:class="{gray_span:wait_timer>0}"
                  >
                  {{ getCodeText() }}
                  </span>
                </v-btn>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-checkbox
                  v-model="applyForOrganization"
                  label= "Apply As Organization"
                ></v-checkbox>
              </v-col>
            </v-row>
            <v-row>
              <v-btn
                block
                v-if="submitShow" 
                @click="submitNewPassword()"
              >
                Submit!
              </v-btn>
            </v-row>
          </v-card-text>
        </v-card>
      </v-layout>
    </div>
    <div>
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
  </div>
</template>

<script>
import axios from 'axios'
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
      applyForOrganization: false,
      newpassword: "",
      newpassword2: "",
      firstname: "",
      lastname: "",
      nickname: "",
      snackbar: false,
      snackbar2: false,
      submitShow: false,
      inputLock: false,
      codeGet: "123456",
      codeCorrect: false,
      codeIn: "",
      codeTime: true,
      rules: {
        required: value => !!value || 'Required.',
        min: v => v.length >= 8 || 'Min 8 characters',
        max: v => v.length <= 18 || 'Max 18 characters',
        samepassword:  value => value == this.newpassword || "Password not same",
        emailMatch: v => /.+@+cuhk|link+.+cuhk+./.test(v) || "E-mail must be valid",
      },
      // All data needed.
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
      if (this.nickname == "" || this.firstname == "" || this.lastname == "") {
        this.tip = "名称等不能为空";
        return false;
      }
      if (this.newpassword.length < 8) {
        this.tip = "密码不能少于8位";
        return false;
      }
      if (this.nickname.length > 18 || this.firstname.length > 18 || this.lastname.length > 18) {
        this.tip = "名称等不能多于18位";
        return false;
      }
      if (this.newpassword.length > 18) {
        this.tip = "密码不能多于18位";
        return false;
      }
      if (this.newpassword != this.newpassword2) {
        this.tip = "密码不一致";
        return false;
      }
      //console.log(this.email);

      // 等待服务器返回邮箱存在否
      axios.post('api/profile/send_email',{
          email:this.email,
          email_type:'register'
      })
      .then((response)=>{
        if(response.data['code']=='001'){
          this.emailExist = false;
          console.log("false");
        }
        else if(response.data['code']=='101'){
          this.emailExist = true;
          console.log("true");}
      });

      //this.emailExist = false;
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
        console.log(this.email, "请求验证码");
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
      
      axios.post('api/profile/add',{
          email:this.email,
          code:this.codeIn,
          password:this.newpassword,
          first_name:this.firstname,
          last_name:this.lastname,
          nick_name:this.nickname,
          is_organization:this.applyForOrganization
      })
      .then((response)=>{
        if(response.data['code']=='002'){
          this.codeCorrect = true;
          //console.log("false");
        }
        else if(response.data['code']=='102'){
          this.codeCorrect = false;
          //console.log("true");
          }
      });
      console.log(this.newpassword)
      if (!this.codeCorrect) {
        this.snackbar2 = true;
        return false;
      }
      console.log(this.email, this.newpassword);

      
    },
  },
}
</script>

<style>


</style>