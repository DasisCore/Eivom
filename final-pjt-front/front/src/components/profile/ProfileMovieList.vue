<template>
  <div class="app10 container">
    profile Movie Item
    <div class="d-flex justify-content-around row">
      <profile-movie-item v-for="movie in likeMovies"
      :movie="movie"
      :key="movie.id"></profile-movie-item>
    </div>
  </div>
</template>

<script>
import ProfileMovieItem from './ProfileMovieItem.vue'

export default {
  name: 'profile_movie_item',
  components: {
    ProfileMovieItem,
  },
  props: {
    likeMovies: Array,
  }
}
</script>

<style>
  .app10 {
    height: 65rem;
    background-color:	#c9bbc8;
  }
</style>