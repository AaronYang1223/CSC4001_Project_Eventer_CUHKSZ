import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
// tinymce编辑器
import tinymce from 'tinymce'
import VueTinymce from '@packy-tang/vue-tinymce'
import store from './store/store.js'
Vue.prototype.$tinymce = tinymce
Vue.use(VueTinymce)
Vue.use(Vuex)

Vue.config.productionTip = false
import Axios from 'axios'
Vue.prototype.$axios = Axios;
// console.log(store.state.hasLogin)

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')

