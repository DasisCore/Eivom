<template>
  <div class="app9">
    <div class="p-5">
      <div class="d-flex justify-content-center">
        <img :src="profile.profile_img" alt="profile_img">
        <div class="d-flex flex-column justify-content-center align-items-center">
          <h1>Hi, {{ profile.username }}</h1>
          <div>
            <span>{{ profile.like_movies.length }} movie |</span>
            <span>{{ profile.followers.length }} followers |</span>
            <span>{{ profile.followings.length }} followings</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'profile_item',
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
  .app9 {
    background-color: #b6b4c2;
    height: 25rem;

  }
</style>