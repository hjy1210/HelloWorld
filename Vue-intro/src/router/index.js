import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/pages/Home'
import Cart from '@/pages/Cart'

// Admin Components
import Index from '@/pages/admin/Index'
import New from '@/pages/admin/New'
import Products from '@/pages/admin/Products'
import Edit from '@/pages/admin/Edit'
import Details from '@/pages/Details'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/details/:id',
      name: 'Details',
      component: Details
    },
    {
      path: '/admin',
      component: Index,
      children: [
        {
          path: 'new',
          name: 'New',
          component: New
        },
        {
          path: '',
          name: 'Products',
          component: Products
        },
        {
          path: 'edit/:id',
          name: 'Edit',
          component: Edit
        }
      ]
    },
    {
      path: '/Cart',
      name: 'Cart',
      component: Cart
    }

  ]
})
