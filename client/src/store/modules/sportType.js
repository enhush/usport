import * as types from '../mutation-types'
import api from '@/common/api'
import helper from '@/common/helper'

const state = {
  sportTypes: []
}

const mutations = {
  [types.SET_SPORT_TYPES] (state, data) {
    state.sportTypes = data
  }
}

const actions = {

  async read ({ commit, dispatch }) {
    try {
      const {data: {data: sportTypes}} = await api.sportType.read()
      commit(types.SET_SPORT_TYPES, sportTypes)
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
