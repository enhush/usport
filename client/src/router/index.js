import VueRouter from 'vue-router'

import helper from '@/common/helper'
import store from '@/store'

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      name: 'home',
      path: '/',
      component: helper.lazyView('Home'),
      meta: {
        restricted: true,
      },
      children: [
        {
          name: 'club',
          path: '/club',
          component: helper.lazyView('admin/club/Club'),
        },
        {
          name: 'club-add',
          path: '/club/add',
          component: helper.lazyView('admin/club/ClubAdd'),
        },
        {
          name: 'judge',
          path: '/judge',
          component: helper.lazyView('admin/judge/Judge'),
        },
        {
          name: 'judge-add',
          path: '/judge/add',
          component: helper.lazyView('admin/judge/JudgeAdd'),
        },
        {
          path: '*',
          redirect: 'club'
        },
      ]
    },
    {
      name: 'login',
      path: '/login',
      component: helper.lazyView('Login'),
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
