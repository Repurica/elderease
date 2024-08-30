import { createRouter, createWebHistory } from 'vue-router'
import homepage from '../pages/HomePage.vue'
import requestforhelper from '../pages/requestforhelper.vue'
import requestforcheckup from '../pages/requestforcheckup.vue' // Adjust the path if necessary

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
    { path: '/requestforcheckup.vue',
      name: 'requestforcheckup', 
      component: requestforcheckup
    }
  ]
})

export default router
