
import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
  theme:{
    dark: false
  },
  icons: {
    iconfont: 'mdi', // 默认值 - 仅用于展示目的
  },
  breakpoint: {
    mobileBreakpoint: 'sm' // 这个值等于960
  },
});
