import * as types from '../mutation-types'
import api from '@/common/api'

const state = {
  judgeLevels: []
}

const mutations = {
  [types.SET_JUDGE_LEVELS](state, data) {
    state.judgeLevels = data
  },
}

const actions = {

  read({ commit, dispatch }) {
    api.judgeLevel.read().then(({data: {data: judgeLevels}}) => {
      commit(types.SET_JUDGE_LEVELS, judgeLevels)
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
