import store from '@/store'

export default {
  beforeRouteEnter (to, from, next) {
    if (store.getters.isAdmin) {
      next()
    } else {
      next({name: 'profile'})
    }
  }
}
