<template>
  <div class="app8">
    ProfileView
    <profile-item></profile-item>
    <profile-movie-list></profile-movie-list>
    <profile-comment-list></profile-comment-list>
  </div>
</template>

<script>
import ProfileItem from '../components/profile/ProfileItem.vue'
import ProfileMovieList from '../components/profile/ProfileMovieList.vue'
import ProfileCommentList from '../components/profile/ProfileCommentList.vue'

export default {
  name: 'ProfileView',
  components: {
    ProfileItem, ProfileMovieList, ProfileCommentList
  }

}
</script>

<style scoped>
  .app8 {
  height: 220rem;
  background-color: #9aa7d0
  }
</style>