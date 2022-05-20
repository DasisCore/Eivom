<template>
  <div>
    MovieDetailView
    <div style="height: 100vh;">블라블라 영화 상세 내용</div>
    <hr>
    <div>
      <!-- <similar-movie-list ></similar-movie-list> -->
      <div class="d-flex">
        <router-link to="/moviedetail" class="nav-link fw-bold text-secondary"
        active-class="active">actor list</router-link>
        <router-link to="/moviedetail/similarmovies" class="nav-link fw-bold text-secondary"
        active-class="active">similar movie list</router-link>
        
      </div>
      <hr>
      <router-view/>
    </div>
    <hr>
    <movie-comment-list></movie-comment-list>

    
  </div>
</template>

<script>
import MovieCommentList from '../components/moviedetail/MovieCommentList.vue'


export default {
  name: 'MovieDetailView',
  components: {
    MovieCommentList,
  }
}
</script>

<style scoped>

  .active {
    color: black !important;
  }
</style>