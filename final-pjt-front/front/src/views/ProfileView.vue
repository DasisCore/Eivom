<template>
  <div class="app8">
    <div class="d-flex justify-content-center">
      <img :src="profile.profile_img" alt="profile_img">
      <div class="d-flex flex-column justify-content-center align-items-center">
        <h1>Hi, {{ profile.username }}</h1>
        <div>
          <span>{{ profile.like_movies }} movie</span>
          <span>{{ profile.followers }} followers</span>
          <span>{{ profile.followings }} followings</span>
        </div>
      </div>
    </div>
    
    <profile-item></profile-item>
    <profile-movie-list></profile-movie-list>
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