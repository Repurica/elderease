import { createRouter, createWebHistory } from 'vue-router';
import homepage from '../pages/HomePage.vue';
import requestforhelper from '../pages/requestforhelper.vue';
import requestforcheckup from '../pages/requestforcheckup.vue';
import Emergency from '../pages/emergency.vue';
import profile from '../pages/profile.vue';
import speak from '../pages/SpeaktoMe.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: homepage
    },
    {
      path: '/requestforhelper',
      name: 'requestforhelper',
      component: requestforhelper
    },
    {
      path: '/requestforcheckup',
      name: 'requestforcheckup',
      component: requestforcheckup
    },
    {
      path: '/emergency',
      name: 'emergencyalert',
      component: Emergency
    },
    {
      path: '/profile',
      name: 'profile',
      component: profile
    },
    {
      path: '/SpeaktoMe',
      name: 'speaktome',
      component: speak
    }
  ]
});

export default router;
