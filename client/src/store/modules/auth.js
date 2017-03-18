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

    api.auth.login(data).then(({data: {token, user}}) => {
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
  async check({ commit, dispatch }) {

    if (localStorage.getItem('token')) {
      commit(types.SET_AUTH, true)

      api.auth.getMe().then(({data: {user}}) => {
        commit(types.SET_USER, user)
      }).catch(() => {
        localStorage.removeItem('token')
        commit(types.SET_AUTH, false)
        commit(types.SET_USER, {})
        location.replace('/')
      })

    }
  },
}

const getters = {
}


export default {
  state,
  mutations,
  actions,
  getters,
}
