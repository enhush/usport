import Vue from 'vue'
import Vuex from 'vuex'
import club from './modules/club'
import judge from './modules/judge'
import sportType from './modules/sportType'
import judgeLevel from './modules/judgeLevel'
import judgeRequest from './modules/judgeRequest'
import user from './modules/user'
import userDetail from './modules/userDetail'

import notification from './modules/notification'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    club,
    judge,
    sportType,
    judgeLevel,
    notification,
    judgeRequest,
    user,
    userDetail,
  }
})

export default store
