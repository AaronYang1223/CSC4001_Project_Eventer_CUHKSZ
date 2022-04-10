<template>
  <v-app>
    <v-content>
      <!-- <v-container py-5> -->
        <v-layout align-center justify-center py-3>
          <!-- <v-flex xs12 sm8 md4> -->
            <v-card class="px-2 pb-3"  min-width=600px max-width=700px>
              <v-card-text>
                <v-layout justify-center pt-2>
                  <v-avatar size="40px" color="pink">
                    <v-icon dark>lock</v-icon>
                    <!-- <img src="https://vuetifyjs.com/apple-touch-icon-180x180.png" alt="avatar"> -->
                  </v-avatar>
                </v-layout>
                <v-layout justify-center py-3>
                  <div class="headline">Login</div>
                </v-layout>

                <v-form>
                  <v-text-field
                    name="login"
                    label="Email Address"
                    type="text"
                    required
                    v-model="email"
                    :rules="emailRules"
                  ></v-text-field>
                  <v-text-field
                    id="password"
                    name="Password"
                    label="Password"
                    type="password"
                    required
                    v-model="password"
                    :rules="passwordRules"
                  ></v-text-field>
                </v-form>
                
              </v-card-text>
              <v-card-actions>
                <v-row
                align="center"
                justify="space-around"
                >
                  <v-col>
                    <a href="/sign">
                      <v-btn block depressed>Sign In/注册</v-btn>
                    </a>
                  </v-col>
                  <v-col>
                    <a href="javascript:void(0);" @click="toMallInfo('M000989')">
                      <v-btn block depressed>Login Test/登陆</v-btn>
                    </a>
                  </v-col>
                  <v-col>
                    <v-btn block color="info" @click="submit">Login/登陆</v-btn>
                  </v-col>
                </v-row>
              </v-card-actions>
            </v-card>
          <!-- </v-flex> -->
        </v-layout>
      <!-- </v-container> -->
    </v-content>
    <v-snackbar v-model="snackbar">
      登录失败
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
  </v-app>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      email: "",
      loginSuccess: true,
      snackbar: false,
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+/.test(v) || "E-mail must be valid"
      ],
      password: "",
      passwordRules: [v => !!v || "Password is required"]
    };
  },
  methods: {
    submit: function(){
      console.log(this.email, this.password);
    },
    toMallInfo: function(account_id){
      console.log("cnm");
      console.log(this.email, this.password);
      //服务器接受信息
      axios.get('api/profile/',{
          params:{
            email:this.email,
            password:this.password
          }
      })
      .then((response)=>{
        if(response.data['status']=='valid'){
          this.codeCorrect = true;
        }
        else if(response.data['status']=='error'){
          this.codeCorrect = false;
          }
      });

      if (!this.loginSuccess) {
        this.snackbar= true;
        return false;
      }
      account_id = this.email;
      account_id;
      this.$router.push({
      path: '/test',
      query: {
        account_id: this.email,
        }
      });
      this.$router.push({
      name: 'test',
      params: {
        account_id: this.email,
      }
      })
    },
  }
};
</script>