import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from './components/Login'
import Home from './components/Home'
import Club from './components/admin/Club'
import ClubAdd from './components/admin/ClubAdd'

import store from './store'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      name: 'home',
      path: '/',
      component: Home,
      meta: {
        restricted: true,
      },
      children: [
        {
          name: 'club',
          path: 'club',
          component: Club,
        },
        {
          name: 'club-add',
          path: 'club-add',
          component: ClubAdd,
        },
        {
          path: '*',
          redirect: 'club'
        }
      ]
    },
    {
      name: 'login',
      path: '/login',
      component: Login,
    },
    {
      path: '*',
      redirect: '/login',
    }
  ],
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.restricted)) {
    store.state.auth.authenticated
      ? next()
      : next({name: 'login'})
  } else {
    (to.name == 'login' && store.state.auth.authenticated)
      ? next({name: 'home'})
      : next()
  }
})

export default router
