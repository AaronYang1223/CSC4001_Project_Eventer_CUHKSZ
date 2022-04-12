import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'

import Axios from 'axios'
Vue.prototype.$axios = Axios;

Vue.config.productionTip = false

// Filters
Vue.filter('to-uppercase', function(value){
  return value.toUpperCase()
});

Vue.filter('snippet', function(value){
  return value.slice(0,190) + "......"
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
  render: h => h(App)
}).$mount('#app')
