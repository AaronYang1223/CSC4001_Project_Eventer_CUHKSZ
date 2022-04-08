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
              <v-btn block>
                <a href="javascript:void(0);" @click="toMallInfo('M000989')">
                  Login Test/登陆
                </a>
              </v-btn>
            </v-row>
            <!-- 以下:注册和忘记密码 -->
            <v-row>
              <v-col>
                <v-btn block>
                  <a href="/t1">
                    Sign In/注册
                  </a>
                </v-btn>
              </v-col>
              <v-col>
                <v-btn block>
                  <a href="/t2">
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
      loginSuccess: true,
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
    },
    toMallInfo: function(account_id){
      console.log(this.email, this.password);
      //服务器接受信息
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
  },
}
</script>

<style>

</style>