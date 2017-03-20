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
          name: 'judge-request',
          path: '/judge-request',
          component: helper.lazyView('admin/judge-request/JudgeRequest'),
        },
        {
          name: 'judge-request-add',
          path: '/judge-request/add',
          component: helper.lazyView('admin/judge-request/JudgeRequestAdd'),
        },
        {
          name: 'profile',
          path: '/profile',
          component: helper.lazyView('user/profile'),
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
    store.state.user.authenticated
      ? next()
      : next({name: 'login'})
  } else {
    (to.name == 'login' && store.state.user.authenticated)
      ? next({name: 'home'})
      : next()
  }
})

export default router
