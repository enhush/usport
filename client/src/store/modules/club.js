import * as types from '../mutation-types'
import api from '@/common/api'
import helper from '@/common/helper'

const state = {
  clubs: []
}

const mutations = {
  [types.SET_CLUBS] (state, data) {
    state.clubs = data
  }
}

const actions = {

  async create ({ dispatch }, payload) {
    try {
      await api.club.create(payload)
      dispatch('read')
      dispatch('showNotification', `Амжилттай`, {root: true})
    } catch (e) {
      helper.apiError(e, dispatch)
    }
  },

  async read ({ commit, dispatch }) {
    try {
      const {data: {data: clubs}} = await api.club.read()
      commit(types.SET_CLUBS, clubs)
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
