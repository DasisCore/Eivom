<template>
  <div class="app10">
    profile Movie Item
    <div class="d-flex justify-content-around">
      <profile-movie-item></profile-movie-item>
      <profile-movie-item></profile-movie-item>
      <profile-movie-item></profile-movie-item>
      <profile-movie-item></profile-movie-item>
    </div>
    <p></p>
    <p></p>
    <div class="d-flex justify-content-around">
      <profile-movie-item></profile-movie-item>
      <profile-movie-item></profile-movie-item>
      <profile-movie-item></profile-movie-item>
      <profile-movie-item></profile-movie-item>
    </div>
  </div>
</template>

<script>
import ProfileMovieItem from './ProfileMovieItem.vue'

export default {
  name: 'profile_movie_item',
  components: {
    ProfileMovieItem,
  }
}
</script>

<style>
  .app10 {
    height: 80rem;
    background-color:	#c9bbc8;
  }
</style>