<template>
  <div id="owl">
    <h1 class="fw-bold">배우</h1>
    <carousel v-if="actors.length > 0"
    :items="5.5"
    :loop="true"
    :margin="30"
    :nav="false"
    :dot="true"
    :responsive="{
      0: {
        items: 10
      },
      768: {
        items: 6
      }
    }">
      <movie-actors-item v-for="actor in actors" :key="actor.id" :actor="actor"></movie-actors-item>
    </carousel>
  </div>
</template>

<script>
import MovieActorsItem from './MovieActorsItem.vue'
import carousel from "vue-owl-carousel2";

import axios from "axios"
const URL = "https://api.themoviedb.org/3/movie/"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

  export default {
    name: 'movie_actor_list',
    components: {
      MovieActorsItem,
      carousel
    },
    props: {
      movieID: Number,
    },
    data: function() {
      return {
        actors: {},
      }
    },
    computed: {

    },
    created() {
      axios.get(URL + this.movieID + "/credits", {
        params: {
          api_key: API_KEY,
        }
      })
        .then(res => {
          // console.log(res.data.cast.slice(0, 15))
          this.actors = res.data.cast.slice(0, 15)
          })
        .catch(err => {
          console.log(err)
        })
    }
  }



</script>

<style scoped>
  /* .carousel {
    position: relative;
    border-radius: 20px;
    overflow: hidden;
  }
  .carousel-text {
    position: absolute;
    bottom: 0;
    margin-left: 20px;
    z-index: 551;
    color: #ffffff;
  }
  .carousel-bg {
    width: 100%;
    position: absolute;
    bottom: 0;
    height: 100%;
    background: linear-gradient(transparent, #000000);
    opacity: 0.8;
    z-index: 550;
  } */


</style>