import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
	msg: '123456',
  hasLogin: false,
}

const mutations = {
	loginUpdate (state) {
    state.hasLogin = true
  }
}

const actions = {
	
}

export default new Vuex.Store({
	state,
	actions,
	mutations,
})
