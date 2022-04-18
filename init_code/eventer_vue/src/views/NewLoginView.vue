// TODO: 处理右侧滚轮
<template>
  <div id="building">
    <v-container mt-16 py-16>

      <v-row justify="center" align="center" class="mt-16">
        <v-card 
          class="px-2 pb-3" 
          max-width=400px 
          flat
          outlined
          tile
        >

          <div class="text-center mt-4">
            <h1 class="primary--text text-uppercase">
              <span class="font-weight-light">E</span>
              <span>venter</span>
            </h1>
          </div>

          <v-card-text>
            <v-row justify="center" align="center" dense>
              <v-col 
                cols="12" xs="12" sm="12" md="12"
              >
                <v-text-field
                  id="login"
                  label="Email Address"
                  type="text"
                  v-model="email"
                  :rules="[rules.required]"
                  max-width=""
                ></v-text-field>
              </v-col>

              <v-col 
                cols="12" xs="12" sm="12" md="12"
              >
                <v-text-field
                  id="password"
                  label="Password"
                  type="password"
                  v-model="password"
                  :rules="[rules.required]"
                ></v-text-field>
              </v-col>

              <v-col 
                cols="12" xs="12" sm="12" md="12"
              >
                <v-btn 
                  block 
                  tile 
                  color="primary"
                  depressed
                  @click="submit" 
                >
                  Login
                </v-btn>
              </v-col>

              <v-col 
                cols="12" xs="12" sm="4" md="4"
              >
                <v-btn 
                  block 
                  @click="toSignin"
                  tile
                  depressed
                >
                    Sign Up
                </v-btn>
              </v-col>

              <v-col
                cols="12" xs="12" sm="8" md="8"
              >
                <v-btn 
                  block
                  @click="toForget"
                  tile
                  depressed
                >
                  Forget the Password
                </v-btn>
              </v-col>

            </v-row>

          </v-card-text>
        </v-card>

      </v-row>
    </v-container>
    <!-- ？？ -->
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
          this.tip = "Login Failed";
          this.snackbar = true;
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
        console.log(this.$store.state.userID);
        window.location.href = "/";
      });
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
#building{
background:url("../assets/bg.png");
width:100%;			
height:100%;			
background-size: cover; 
position: absolute; 
background-repeat: no-repeat;
}
</style>
