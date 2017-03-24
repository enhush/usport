import * as types from '../mutation-types'
import api from '@/common/api'
import helper from '@/common/helper'

const state = {
  authenticated: false,
  user: {},
  invalid: false
}

const mutations = {
  [types.SET_AUTH] (state, payload) {
    state.authenticated = payload
  },
  [types.SET_USER] (state, payload) {
    state.user = Object.assign({}, payload)
  },
  [types.SET_INVALID] (state, payload) {
    state.invalid = payload
  },
  [types.LOGGED_IN] (state, {token, user}) {
    localStorage.setItem('token', token)
    state.authenticated = true
    state.user = Object.assign({}, user)
  },
  [types.LOGGED_OUT] (state) {
    localStorage.removeItem('token')
    state.authenticated = false
    state.user = {}
  }
}

const actions = {
  async login ({ commit, dispatch }, payload) {
    try {
      const {data: userAndToken} = await api.user.login(payload)
      commit(types.LOGGED_IN, userAndToken)
      location.replace('/')
    } catch (e) {
      commit(types.LOGGED_OUT)
      commit(types.SET_INVALID, true)
    }
  },
  async checkAuth ({ commit, dispatch }) {
    if (localStorage.getItem('token')) {
      commit(types.SET_AUTH, true)
      try {
        const {data: {user}} = await api.user.get()
        commit(types.SET_USER, user)
      } catch (e) {
        dispatch('logout')
      }
    }
  },
  logout ({commit}) {
    commit(types.LOGGED_OUT)
    location.replace('/login')
  },

  async update ({ commit, dispatch }, payload) {
    try {
      const {data: {user}} = await api.user.update(payload)
      commit(types.SET_USER, user)

      dispatch('showNotification', `Амжилттай`)
    } catch (e) {
      helper.apiError(e, dispatch)
    }
  }
}

const getters = {
  isAdmin (state) {
    return state.user['role']
  },
  username (state) {
    return state.user['username'] || ''
  },
  email (state) {
    return state.user['email'] || ''
  }
}

export default {
  state,
  mutations,
  actions,
  getters
}
