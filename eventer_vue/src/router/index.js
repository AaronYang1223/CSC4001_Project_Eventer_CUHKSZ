import Vue from 'vue'
import VueRouter from 'vue-router'
import HomepageView from '../views/HomepageView.vue'
import PersonalCenterView from '../views/PersonalCenterView.vue'
import NewPostView from '../views/NewPostView.vue'
import NewEventView from '../views/NewEventView.vue'
import LoginView from '../views/LoginView.vue'

Vue.use(VueRouter)

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
    path: '/post',
    name: 'post',
    component: NewPostView
  },
  {
    path: '/event',
    name: 'event',
    component: NewEventView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
