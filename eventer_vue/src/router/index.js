import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignInView from '../views/SignInView.vue'
import TestView from '../views/TestView.vue'
import ForgetPassword from '../views/ForgetPassword.vue'
import SignView from '../views/SignView.vue'
import NewSignInView from '../views/NewSignInView.vue'
import NewLoginView from '../views/NewLoginView.vue'
import NewForgetView from '../views/NewForgetView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signin',
    name: 'signin',
    component: SignInView
  },
  {
    path: '/forget',
    name: 'forget',
    component: ForgetPassword,
  },
  {
    path: '/sign',
    name: 'sign',
    component: SignView,
  },
  {
    path: '/test',
    name: 'test',
    component: TestView,
  },
  {
    path: '/t1',
    name: 't1',
    component: NewSignInView,
  },
  {
    path: '/t2',
    name: 't2',
    component: NewForgetView,
  },
  {
    path: '/t3',
    name: 't3',
    component: NewLoginView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
