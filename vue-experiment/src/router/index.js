import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import ScopedStyle from '@/components/ScopedStyle'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/scopedstyle',
      name: 'scopedstyle',
      component: ScopedStyle
    }
  ]
})
