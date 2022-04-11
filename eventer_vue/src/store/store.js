import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

const state = {
  userID: "",
  userEmail:"",
  userNickName: "Unknown",
  avatar:"",
	msg: '123456',
  hasLogin: false,
}

const mutations = {
	loginUpdate (state) {
    state.hasLogin = true
  },
  logoutUpdate (state) {
    state.hasLogin = false
  },
  userEmailUpdate (state, useremail){
    state.userEmail = useremail
  },
  userNicknameUpdate (state, nickname){
    state.userNickname = nickname
  },
  userAvatarUpdate (state, avatar_url){
    state.avatar = avatar_url
  }
}

const actions = {
	
}

export default new Vuex.Store({
	state,
	actions,
	mutations,
  plugins: [createPersistedState()]
})


// import createPersistedState from "vuex-persistedstate"
// const store = new Vuex.Store({
//   // ...
//   plugins: [createPersistedState({
//       storage: window.sessionStorage,
//       reducer(val) {
//       	return {
//       	// 只储存state中的assessmentData
//     	  assessmentData: val.assessmentData
//     	}
// 	 }
//   })]

