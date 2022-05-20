<template>
  <div>
    비슷한 영화 추천!
    <div class="d-flex">
      <similar-movie-item class="m-3"></similar-movie-item>
      <similar-movie-item class="m-3"></similar-movie-item>
      <similar-movie-item class="m-3"></similar-movie-item>
      <similar-movie-item class="m-3"></similar-movie-item>
      <similar-movie-item class="m-3"></similar-movie-item>
    </div>
  </div>
</template>

<script>
import SimilarMovieItem from './SimilarMovieItem.vue'

export default {
  name: 'similar_movie_list',
  components: {
    SimilarMovieItem,
  }

}
</script>

<style scoped>

</style>