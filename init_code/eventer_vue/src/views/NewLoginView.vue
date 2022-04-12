<template>
  <div>
    <div>
      <v-layout align-center justify-center py-5>
        <v-card class="px-2 pb-3" max-width=900px>
          <v-card-text>
            <h1 align="center">
              <span style="color:blue">L</span>ogin
            </h1>
            <br/>
            <v-row>
              <v-text-field
                id="login"
                label="Email Address"
                type="text"
                v-model="email"
                :rules="[rules.required]"
              ></v-text-field>
            </v-row>
            <v-row>
              <v-text-field
                id="password"
                label="Password"
                type="password"
                v-model="password"
                :rules="[rules.required]"
              ></v-text-field>
            </v-row>
            <v-row justify="center" align="center">
              <v-btn block @click="submit" color="green">
                Login/登陆
              </v-btn>
            </v-row>
            <!-- 以下:注册和忘记密码 -->
            <v-row>
              <v-col>
                <v-btn block @click="toSignin">
                    Sign In/注册
                </v-btn>
              </v-col>
              <v-col>
                <v-btn block @click="toForget">
                  Forget the Password/忘记密码
                </v-btn>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-layout>
    </div>
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
import axios from 'axios'
export default {
  data() {
    return {
      email: "",
      ID:"",
      nickname:"",
      avatar:"",
      loginSuccess: false,
      snackbar: false,
      password: "",
      rules: {
        required: value => !!value || 'Required.',
        min: v => v.length >= 8 || 'Min 8 characters',
        samepassword:  value => value == this.newpassword || "Password not same",
        emailMatch: v => /.+@+cuhk|link+.+cuhk+./.test(v) || "E-mail must be valid",
      },
    }
  },
  methods: {
    submit: function(){
      if (this.email == "") {
        this.tip = "Input your Email !";
        this.snackbar = true;
        return false;
      }
      if (this.password == "") {
        this.tip = "Input your Password !";
        this.snackbar = true;
        return false;
      }
      console.log(this.email, this.password);
      // 需要服务器返回登陆信息
      axios.get('api/profile/verify',{
          params:{
            email:this.email,
            password:this.password
          }
      })
      .then((response)=>{
          if(response.data.status == "error"){
            this.loginSuccess = false;
            return;
          }
          this.loginSuccess = true;
          this.ID = response.data.id;
          this.email = response.data.email;
          this.nickname = response.data.nick_name;
          this.avatar = 'http://127.0.0.1:8000' + response.data.picture;
          
          
          this.$store.commit("loginUpdate");
          this.$store.commit("userEmailUpdate", this.email);
          this.$store.commit("userIDUpdate", this.ID);
          this.$store.commit("userNicknameUpdate", this.nickname);
          this.$store.commit("userAvatarUpdate", this.avatar);
          this.$store.commit("userIsOrganizationUpdate", response.data.is_organization);
          console.log("success");
          window.location.href = "/";
          
      });
      //this.loginSuccess = true;
      // console.log(this.loginSuccess);
      // if (this.loginSuccess) {
      //   this.$store.commit("loginUpdate");
      //   this.$store.commit("userIDUpdate", this.email);
      //   console.log(this.$store.state.userID);
      //   window.location.href = "/";
      // }
    },
    toSignin: function(){
      window.location.href = "/signin";
    },
    toForget: function(){
      window.location.href = "/forget";
    }
  },
}
</script>

<style>

</style>