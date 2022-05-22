import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '../views/MainView.vue'
import RecommendView from '../views/RecommendView.vue'
import CommunityView from '../views/CommunityView.vue'
import ProfileView from '../views/ProfileView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import SignUpView from '../views/SignUpView.vue'
import NotFound404 from '../views/NotFound404.vue'

// 임시 영화 상세 페이지 라우터
import MovieDetailView from '../views/MovieDetailView.vue'

// 중첩 라우터
import SimilarMovieList from '../components/moviedetail/SimilarMovieList.vue'
import MovieActorsList from '../components/moviedetail/MovieActorsList.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'mainpage',
    component: MainView
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: RecommendView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },

  // 임시로 만든 영화 상세 페이지 라우터
  {
    path: '/moviedetail',
    name: 'moviedetail',
    component: MovieDetailView,
    children: [
      {
        path: '/moviedetail',
        name: 'movieactors',
        component: MovieActorsList
      },
      {
        path: '/moviedetail/similarmovies',
        name: 'similarmovies',
        component: SimilarMovieList
      },
    ]
  },



]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
