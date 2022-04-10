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
              <v-btn block @click="submit">
                Login/登陆
              </v-btn>
            </v-row>
            <!-- 以下:注册和忘记密码 -->
            <v-row>
              <v-col>
                <v-btn block>
                  <a href="/signin">
                    Sign In/注册
                  </a>
                </v-btn>
              </v-col>
              <v-col>
                <v-btn block>
                  <a href="/forget">
                    Forget the Password/忘记密码
                  </a>
                </v-btn>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-layout>
    </div>
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
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
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
      console.log(this.email, this.password);
      // 需要服务器返回登陆信息
      this.loginSuccess = true;
      console.log(this.loginSuccess);
      if (this.loginSuccess) {
        this.$store.commit("loginUpdate");
        console.log("cnm")
        console.log(this.$store.state.hasLogin);
        // window.location.href = "/";
      }
    },
  },
}
</script>

<style>

</style>