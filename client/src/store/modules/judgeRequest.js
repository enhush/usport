import * as types from '../mutation-types'
import api from '@/common/api'

const state = {
  judgeRequests: [],
}

const mutations = {
  [types.SET_JUDGE_REQUESTS](state, data) {
    state.judgeRequests = data
  },
}

const actions = {

  read({ commit, dispatch }) {
    api.judgeRequest.read().then(({data: {data: judgeRequests}}) => {
      commit(types.SET_JUDGE_REQUESTS, judges)
    }).catch(({response: {data: {message = 'Алдаа'}}}) => {
      dispatch('showNotification', message, {root: true})
    })
  }
}

const getters = {
}


export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
}
