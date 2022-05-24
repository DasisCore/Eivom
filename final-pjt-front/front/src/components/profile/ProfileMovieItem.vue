<template>
  <div class="app11">
    <img :src="`https://image.tmdb.org/t/p/original${poster_path}`" alt="">
    <h4>{{ title }}</h4>
  </div>
</template>

<script>
import axios from "axios"
const URL = "https://api.themoviedb.org/3/movie/"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default {
  name: 'profile_movie_item',
  props: {
    movie: Object,
  },
  data: function(){
    return {
      title: '',
      poster_path: '',
    }
  },
  created() {
    axios.get(URL + this.movie.movie_id, {
      params: {
        api_key: API_KEY,
        language: 'ko-KR',
      }
    })
      .then(res => {
      this.title = res.data.title
      this.poster_path = res.data.poster_path
      // console.log(res.data)
      })
      .catch(err => console.log(err))
  }
}
</script>

<style scoped>

  .app11 {
    height:400px;
    width: 300px;
    background-color: #e5c1cd;
  }
  img {
    width: 300px;
  }
  h4 {
    text-align: center;
  }
</style>