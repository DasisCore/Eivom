<template>
<<<<<<< HEAD
    <div class="app3" v-if="poster_path != '' ">
      <h2>이 영화는 어떠세요?</h2>
        <div class="cards">
          <div class="card__left">
            <img class="card__left__img" :src="`https://image.tmdb.org/t/p/original${poster_path}`"/>
          </div>
        <div class="card__right">
          <div class="card__right__header">
            <div class="card__right__header__title">
              <h3>{{ title }}</h3>
            </div>
          </div>
          <div class="card__right__genres">
            <span class="card__right__genre" v-for="genre in genres" :key="genre.id">
              {{ genre.name }}
            </span>
            <div class="card__right__header__score">
              <i class="fa-solid fa-star" style="color: #ffac33"></i>
              <p>{{ vote_average }}</p>
            </div>
          </div>
        </div>
      </div>
=======
    <div class="app3">
      <h3>이 영화 어때요</h3>
      <community-card-item></community-card-item>
>>>>>>> 8e702aadde5b5d6b19bf16a078cf5d285d9ea4d7
    </div>
</template>

<script>
// import CommunityCardItem from './CommunityCardItem.vue'

import _ from 'lodash'
import axios from "axios"
const URL = "https://api.themoviedb.org/3/movie/top_rated"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY
let page = _.random(1, 480)
let num = _.random(0,19)


export default {
  
  name: 'community_card',
  components: {
    // CommunityCardItem,
  },
  data: function(){
    return {
      title: '',
      original_title: '',
      backdrop_path: '',
      genres: [],
      release_date: '',
      vote_average: '',
      overview: '',
      poster_path: '',
    }
  },
  created() {
    axios.get(URL, {
      params: {
        api_key: API_KEY,
        language: 'ko-KR',
        page: page
      }
    })
      .then(res => {
      console.log(res.data.results[num])
      this.title = res.data.results[num].title
      this.poster_path = res.data.results[num].poster_path
      this.original_title = res.data.results[num].original_title
      this.backdrop_path = res.data.results[num].backdrop_path
      this.genres = res.data.results[num].genres_ids
      this.release_date = res.data.results[num].release_date
      this.vote_average = res.data.results[num].vote_average
      this.overview = res.data.results[num].overview
      })
      .catch(err => console.log(err))
  }

}
</script>

<style scoped>
@import 'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap';
  * {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
  }
  .app3 {
    margin-top: 190px;
    width: 30vw;
    height: 400px;
    /* width: 40rem; */
<<<<<<< HEAD
    background-color: rgb(245, 245, 245);
=======
    /* background-color: lightgrey; */
>>>>>>> 8e702aadde5b5d6b19bf16a078cf5d285d9ea4d7
    /* border: 2px solid; */
    display: flex;
    flex-direction: column;
    /* align-items: center; */
    justify-content: center;
    /* margin-top: 5rem; */
    border-radius: 15px;
  }

  .card__left__img {
    width: 150px;
  }

  .cards {
  width: 30rem;
  display: flex;
  justify-content: space-evenly;
  border-radius: 4px;
  padding: 1rem 0rem;
  border-bottom: 1px solid var(--recommend-border);
  margin-left: 35px;
  margin-right: 35px;
  }

  .card__right{
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .card__right__header {
    display: flex;
    justify-content: space-between;
    align-items: space-between;
  }

  .card__right__header__score{
    display: flex;
  }
</style>