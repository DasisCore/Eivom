<template>
  <div class="app8">
    
    
    <profile-item></profile-item>
    <profile-movie-list :likeMovies="profile.like_movies"></profile-movie-list>
    <profile-comment-list></profile-comment-list>
  </div>
</template>

<script>
import ProfileItem from '../components/profile/ProfileItem.vue'
import ProfileMovieList from '../components/profile/ProfileMovieList.vue'
import ProfileCommentList from '../components/profile/ProfileCommentList.vue'
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'ProfileView',
  components: {
    ProfileItem, ProfileMovieList, ProfileCommentList
  },
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },

}
</script>

<style scoped>
  .app8 {
  height: 220rem;
  background-color: #9aa7d0
  }
</style>