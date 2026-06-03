import { createRouter, createWebHistory } from 'vue-router'
import MovieList from '../views/MovieList.vue'
import MovieDetail from '../views/MovieDetail.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', name: 'home', component: ReceptList},
        { path: '/movie/:id', name: 'movie-detail', component: ReceptDetail}
    ]
})

export default router
