<template>
  <div class="cards">
    <div class="card__left">
      <img
        class="card__left__img"
        :src="`https://image.tmdb.org/t/p/original${poster_path}`"
      />
    </div>
    <div class="card__right">
      <div class="card__right__header">
        <div class="card__right__header__title">
          <h3>{{ title }}</h3>
        </div>
        
      </div>

      <div class="card__right__genres">
        <span
          class="card__right__genre"
          v-for="genre in genres"
          :key="genre.id"
        >
          {{ genre.name }}
        </span>
        <div class="card__right__header__score">
          <i class="fa-solid fa-star" style="color: yellow"></i>
          <p>{{ vote_average }}</p>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import axios from "axios"
const URL = "https://api.themoviedb.org/3/movie/"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY
let num1 = _.random(50, 10000)
export default {
data: function(){
    return {
      movieID: 453395,
      title: '',
      original_title: '',
      backdrop_path: '',
      genres: [],
      release_date: '',
      runtime: '',
      vote_average: '',
      overview: '',
      poster_path: '',
      menubar: true,
    }
  },
  created() {
    axios.get(URL + num1, {
      params: {
        api_key: API_KEY,
        language: 'ko-KR',
      }
    })
      .then(res => {
      console.log(res.data)
      this.title = res.data.title
      this.poster_path = res.data.poster_path
      this.original_title = res.data.original_title
      this.backdrop_path = res.data.backdrop_path
      this.genres = res.data.genres
      this.release_date = res.data.release_date

      const hour = parseInt(res.data.runtime / 60)
      const min = parseInt(res.data.runtime % 60)
      this.runtime = hour + "h " + min + "m"

      this.vote_average = res.data.vote_average
      this.overview = res.data.overview
      // console.log(res.data)
      })
      .catch(err => console.log(err))

  }
}
</script>

<style>
  .app5 {
    height: 300px;
    width: 300px;
    background-color: #aed4b6;
    
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