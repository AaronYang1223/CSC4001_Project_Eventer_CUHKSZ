import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
// tinymce编辑器
import tinymce from 'tinymce'
import VueTinymce from '@packy-tang/vue-tinymce'
import store from './store/store.js'
import Axios from 'axios'
Vue.prototype.$axios = Axios;
Vue.prototype.$tinymce = tinymce
Vue.use(VueTinymce)
Vue.use(Vuex)

Vue.config.productionTip = false

// console.log(store.state.hasLogin)

// Filters
Vue.filter('to-uppercase', function(value){
  return value.toUpperCase()
});

Vue.filter('snippet', function(value){
  if(value.length >=190){
    return value.slice(0,190) + "......"
  }
  return value.slice(0,190)
});

Vue.filter('snippet_event', function(value){
  if(value.length >=10){
    return value.slice(0,10) + "..."
  }
  return value.slice(0,10)
});

// Custom directives
Vue.directive('rainbow', {
  bind(el){
      el.style.color = "#" + "4B" + Math.random().toString(16).slice(2, 4) + "FF";
  }
});

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')

