import { createRouter, createWebHistory } from 'vue-router'
import ReceptList from '../views/ReceptList.vue'
import ReceptDetail from '../views/ReceptDetail.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', name: 'home', component: ReceptList},
        { path: '/recept/:id', name: 'recept-detail', component: ReceptDetail}
    ]
})

export default router
