<template>
  <v-app>
    <v-main>
      <!-- <v-container py-5> -->
        <v-layout align-center justify-center py-3>
          <!-- <v-flex xs12 sm8 md4> -->
            <v-card class="px-2 pb-3" min-width=600px max-width=700px>
              
              <v-card-text>
                <v-layout justify-center pt-2>
                  <v-avatar size="40px" color="pink">
                    <v-icon dark>SI</v-icon>
                    <!-- <img src="https://vuetifyjs.com/apple-touch-icon-180x180.png" alt="avatar"> -->
                  </v-avatar>
                </v-layout>
                <v-layout justify-center py-3>
                  <div class="headline">Sign in</div>
                </v-layout>

                <v-form>
                  <v-text-field
                    name="login"
                    label="Email Address"
                    type="text"
                    required
                    v-model="email"
                    :rules="[rules.required, rules.emailMatch]"
                  ></v-text-field>
                  <v-text-field
                    id="password"
                    name="Password"
                    label="Password"
                    type="password"
                    required
                    v-model="password"
                    :rules="[rules.required, rules.min]"
                  ></v-text-field>
                  <v-text-field
                    id="password_confirmed"
                    name="Password"
                    label="Password Confirmed"
                    type="password"
                    required
                    v-model="password_confirmed"
                    :rules="[rules.required, rules.min, rules.samepassword]"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-btn block color="info" @click="submit">Sign In</v-btn>
              </v-card-actions>
            </v-card>
          <!-- </v-flex> -->
        </v-layout>
      <!-- </v-container> -->
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "SignInView",
  data() {
    return {
      email: "",
      password: "",
      password_confirmed: "",
      rules: {
        required: value => !!value || 'Required.',
        min: v => v.length >= 8 || 'Min 8 characters',
        samepassword:  value => value == this.password || "Password not same",
        emailMatch: v => /.+@+cuhk|link+.+cuhk+./.test(v) || "E-mail must be valid",
      },
    };
  },
  methods: {
    submit() {
      console.log(this.email, this.password);
    }
  }
};
</script>