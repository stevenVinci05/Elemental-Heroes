import { createRouter, createWebHistory } from 'vue-router'
import Summon from './views/Summon.vue'

const routes = [
  {
    path: '/',
    redirect: '/summon'
  },
  {
    path: '/summon',
    name: 'Summon',
    component: Summon
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
