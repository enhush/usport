import * as types from '../mutation-types'
import api from '@/common/api'
import helper from '@/common/helper'

const state = {
  judges: []
}

const mutations = {
  [types.SET_JUDGES] (state, data) {
    state.judges = data
  }
}

const actions = {

  async create ({ dispatch }, payload) {
    try {
      await api.judge.create(payload)
      dispatch('read')
      dispatch('showNotification', `Амжилттай`, {root: true})
    } catch (e) {
      helper.apiError(e, dispatch)
    }
  },

  async read ({ commit, dispatch }) {
    try {
      const {data: {data: judges}} = await api.judge.read()
      commit(types.SET_JUDGES, judges)
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
