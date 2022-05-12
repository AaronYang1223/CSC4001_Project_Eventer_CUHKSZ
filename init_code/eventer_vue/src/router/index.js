import Vue from 'vue'
import Vuex from 'vuex'
import VueRouter from 'vue-router'
import HomepageView from '../views/HomepageView.vue'
import PersonalCenterView from '../views/PersonalCenterView.vue'
import NewSignInView from '../views/NewSignInView.vue'
import NewLoginView from '../views/NewLoginView.vue'
import NewForgetView from '../views/NewForgetView.vue'
import NewPostView from '../views/NewPostView.vue'
import NewEventView from '../views/NewEventView.vue'
import PostView from '../views/PostView.vue'
import EventView from '../views/EventView.vue'
import ChangePasswardView from '../views/ChangePasswardView.vue'
import store from '../store/store.js'



Vue.use(VueRouter)
Vue.use(Vuex)

const whiteList = ["/login", "/forget", "/signin", "/change"]; // 定义一个白名单列表

// 主要网页的路由地址
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomepageView
  },
  {
    path: '/personal',
    name: 'personal',
    component: PersonalCenterView
  },
   
  {
    path: '/signin',
    name: 'signin',
    component: NewSignInView,
  },
  {
    path: '/forget',
    name: 'forget',
    component: NewForgetView,
  },
  {
    path: '/login',
    name: 'login',
    component: NewLoginView,
  },
  {
    path: '/newpost',
    name: 'newpost',
    component: NewPostView,
  },
  {
    path: '/newevent',
    name: 'newevent',
    component: NewEventView,
  },
  {
    path: '/post/:id',
    name: 'post',
    component: PostView,
  },
  // 生成不同id的post与event
  {
    path: '/event/:id',
    name: 'event',
    component: EventView,
  },
  {
    path: '/change',
    name: 'change',
    component: ChangePasswardView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// 路由守卫
router.beforeEach(async (to, from, next) => {
  var isTokenAvailable;
  isTokenAvailable = store.state.hasLogin; // 校验是否登陆
  if (!isTokenAvailable && whiteList.includes(to.path)) { // 如果是访问的白名单中的页面
    return next(); // 不需要校验，直接返回继续访问该页面
  }
  if (isTokenAvailable) { // 如果已经登陆
    if(whiteList.includes(to.path)) { // 如果访问的是login页面，则回到首页
      next("/");
    } else { // 如果访问的不是login页面，则继续访问当前要访问的页面
      next();
    }
  } else { 
    //如果没有登陆，进入登陆页面
    next("/login");
    // }
  }
});

export default router
