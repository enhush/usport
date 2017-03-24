import * as types from '../mutation-types'
import api from '@/common/api'
import helper from '@/common/helper'

const state = {
  judgeLevels: []
}

const mutations = {
  [types.SET_JUDGE_LEVELS] (state, data) {
    state.judgeLevels = data
  }
}

const actions = {

  async read ({ commit, dispatch }) {
    try {
      const {data: {data: judgeLevels}} = await api.judgeLevel.read()
      commit(types.SET_JUDGE_LEVELS, judgeLevels)
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
