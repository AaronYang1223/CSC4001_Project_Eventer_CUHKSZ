// TODO:增加跳转按钮
<template>
  <div id="building">
    <!-- <NavbarComNotLogin :Page=pageNow>
    </NavbarComNotLogin> -->
    <v-container mt-16 py-16>
      <v-row justify="center" align="center" class="mt-1">
        <v-card 
          class="px-2 pb-3" 
          max-width=400px
          flat
          outlined
          tile
        >

          <div class="text-center mt-2">
            <h1 class="primary--text">
              <span>Forget Passward</span>
            </h1>
          </div>

          <v-card-text>
            <v-row justify="center" align="center" dense>
              <v-col 
                cols="12" xs="12" sm="12" md="12"
              >
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
              <v-col 
                cols="12" xs="12" sm="12" md="12"
              >
              <!-- 输入密码 -->
              <v-text-field
                type="password" 
                label="Password"
                v-model="newpassword"
                v-bind:disabled = "inputLock"
                id="inputNewPassword"
                :rules="[rules.required, rules.min, rules.max,]"
              >
              </v-text-field>
              </v-col>
              <v-col 
                cols="12" xs="12" sm="12" md="12"
              >
              <!-- 再次输入密码 -->
              <v-text-field
                type="password" 
                label="Password Repeat"
                v-model="newpassword2"
                v-bind:disabled = "inputLock"
                id="inputNewPassword2"
                :rules="[rules.required, rules.min, rules.max, rules.samepassword]"
              >
              </v-text-field>
              </v-col>
              <v-col 
                cols="12" xs="12" sm="6" md="6"
              >
                <v-text-field
                  type="text" 
                  label="Verification Code"
                  v-model="codeIn" 
                  id="inputVerifyCode"
                >
                </v-text-field>
              </v-col>
              <v-col
                cols="12" xs="12" sm="6" md="6"
              >
              <!-- Verification Code Get -->
              <!-- 获取验证码，并且提示再获取时间 -->
                <v-btn
                  block 
                  tile 
                  color="primary"
                  depressed
                  textarea
                  outlined
                  small
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
              <v-col
                cols="12" xs="12" sm="12" md="12"
              >
              <v-btn
                tile 
                color="primary"
                depressed
                block
                v-if="submitShow" 
                @click="submitNewPassword()"
              >
                Submit!
              </v-btn>
              </v-col>
              <v-col 
                cols="12" xs="12" sm="12" md="12"
              >
                <v-btn
                  tile 
                  color="primary"
                  depressed
                  textarea
                  outlined
                  small
                  block
                  router :to="'/login'"
                >
                  <v-icon
                    small
                  >
                    mdi-login-variant
                  </v-icon>
                  <span>back to login</span> 
                </v-btn>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-row>
</v-container>
    <div>
      <!-- 提示错误信息 -->
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
        Verify Code Error
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
// import NavbarComNotLogin from '../components/NavbarComNotLogin.vue'
export default {
  // components: { NavbarComNotLogin },
  data() {
    return {
      tip: "用Email找回密码",
      showNum: false,
      wait_timer: false,
      email: "",
      emailExist: false,
      newpassword: "",
      newpassword2: "",
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
      pageNow: {
        isPage: "forget",
      },
    }
  },
  methods: {
    // 验证输入，并发送验证码
    // Send Verification Code
    getCode: function() {
      if (this.wait_timer > 0) {
        return false;
      }
      if (!this.email) {
        this.hasError = true;
        this.isActive = false;
        this.isTip = true;
        this.tip = "Email can't be empty";
        return false;
      }
      if (
        !/.+@+cuhk|link+.+cuhk+./.test(this.email)
      ) {
        this.hasError = true;
        this.isActive = false;
        this.isTip = true;
        this.tip = "Email is invalid";
        return false;
      }
      if (this.newpassword == "") {
        this.tip = "Password can't be empty";
        return false;
      }
      if (this.newpassword.length < 8) {
        this.tip = "Password can't less than 8 char";
        return false;
      }
      if (this.newpassword.length > 18) {
        this.tip = "Password can't more than 18 char";
        return false;
      }
      if (this.newpassword != this.newpassword2) {
        this.tip = "Two Password is not same";
        return false;
      }
      console.log(this.email);
      axios.post('api/profile/send_email',{
          email:this.email,
          email_type:'retrieve'
      })
      .then((response)=>{
        if(response.data['code']=='003'){
          this.emailExist = true;
          console.log("false");
        }
        else if(response.data['code']=='103'){
          this.emailExist = false;
          console.log("true");}
      });
      //this.emailExist = true;
      if (!this.emailExist) {
        this.tip = "Email not exist";
        return false;
      }

      this.tip = "Already send, please wait";
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
    },

    getCodeText: function() {
      if (this.wait_timer > 0) {
        return "Already send";
      }
      if (this.wait_timer === 0) {
        this.showNum = false;
        this.codeTime = true;
        return "Send Again !";
      }
      if (this.wait_timer === false) {
        return "Send Verify Code";
      }
    },
    // Submit the password
    // 提交新的密码
    submitNewPassword: function() {
      console.log(this.codeIn);
      axios.put('api/profile/retrieve',{
          email:this.email,
          code:this.codeIn,
          newpassword:this.newpassword,
      })
      .then((response)=>{
        if(response.data['code']=='004'){
          this.codeCorrect = true;
          //console.log("false");
        }
        else if(response.data['code']=='104'){
          this.codeCorrect = false;
          //console.log("true");
          if (!this.codeCorrect) {
          this.snackbar2 = true;
          return false;
      }
        }
      });
      //this.codeCorrect = true;
      //从服务器获得
      
      console.log(this.email, this.newpassword);
      window.location.href = "/login";
    },
  },
}
</script>

// TODO:应该是只要保留一个
<style>
#building{
background:url("../assets/bg.png");
width:100%;			
height:100%;			
background-size: cover; 
position: absolute; 
background-repeat: no-repeat;
}
</style>