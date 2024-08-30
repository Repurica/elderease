import { createRouter, createWebHistory } from 'vue-router'
import homepage from '../pages/HomePage.vue'
import requestforhelper from '../pages/requestforhelper.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: homepage
    },
    {
      path: '/requestforhelper.vue',
      name: 'request',
      component: requestforhelper
    },
    
  ]
})

export default router
