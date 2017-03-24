import * as types from '../mutation-types'
import api from '@/common/api'
import helper from '@/common/helper'

const state = {
  judgeRequests: []
}

const mutations = {
  [types.SET_JUDGE_REQUESTS] (state, data) {
    state.judgeRequests = data
  }
}

const actions = {

  async read ({ commit, dispatch }) {
    try {
      const {data: {data: judgeRequests}} = await api.judgeRequest.read()
      commit(types.SET_JUDGE_REQUESTS, judgeRequests)
    } catch (e) {
      helper.apiError(e, dispatch)
    }
  }
}

const getters = {
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}
