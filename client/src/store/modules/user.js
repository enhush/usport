import * as types from '../mutation-types'
import api from '@/common/api'

const state = {
  authenticated: false,
  user: {},
  invalid: false,
}

const mutations = {
  [types.SET_AUTH] (state, data) {
    state.authenticated = data
  },
  [types.SET_USER] (state, data) {
    state.user = Object.assign({}, data)
  },
  [types.SET_INVALID] (state, data) {
    state.invalid = data
  },
}

const actions = {
  login({ commit, dispatch }, {data, router}) {
    api.user.login(data).then(({data: {token, user}}) => {
      localStorage.setItem('token', token)

      commit(types.SET_AUTH, true)
      commit(types.SET_USER, user)

      router.replace({name: 'club'})
    }).catch(() => {
      commit(types.SET_AUTH, false)
      commit(types.SET_INVALID, true)
      localStorage.removeItem('token')

    })
  },
  checkAuth({ commit, dispatch }) {

    if (localStorage.getItem('token')) {
      commit(types.SET_AUTH, true)

      api.user.getMe().then(({data: {user}}) => {
        commit(types.SET_USER, user)
      }).catch(() => {
        dispatch('logout')
      })

    }
  },
  logout({commit}) {
    localStorage.removeItem('token')
    commit(types.SET_AUTH, false)
    commit(types.SET_USER, {})
    location.replace('/')
  },

  update({ commit, dispatch }, payload) {
    api.user.update(payload).then(({data: {user}}) => {
      dispatch('showNotification', `Амжилттай`)
      commit(types.SET_USER, user)
    }).catch(({response: {data: {message = 'Алдаа'}}}) => {
      dispatch('showNotification', message)
      if (message.includes("jwt-error")) {
        dispatch('logout')
      }
    })
  },
}

const getters = {
  isAdmin(state) {
    return state.user['role']
  },
  username(state) {
    return state.user['username'] || ''
  },
  email(state) {
    return state.user['email'] || ''
  },
}


export default {
  state,
  mutations,
  actions,
  getters,
}
