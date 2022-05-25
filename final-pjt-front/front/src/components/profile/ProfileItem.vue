<template>
  <div class="app9">
    <div class="p-5">
      <div class="d-flex justify-content-center">
        <div class="d-flex flex-column">
          <img v-if="profile.profile_img" :src="profile.profile_img">
          <img v-else class="profile" src="@/assets/default_profile.jpg">
          <router-link 
          :to="{ name: 'profileImg' }">
            <button>프로필 사진 변경</button>
          </router-link>
        </div>
        <div class="d-flex flex-column justify-content-center align-items-center">
          <div class="d-flex">
            <h1>{{ profile.username }}'s profile</h1>
            <button @click="followProfile(username)" v-if="notMyAccount && isFollowing">언팔로우</button>
            <button @click="followProfile(username)" v-if="notMyAccount && !isFollowing">팔로우</button>

            <!-- 본인 프로필이면 팔로우 버튼 x
            팔로우 상태면 언팔로우버튼
            언팔로우 상태면 팔로우버튼 -->
          </div>
          <div>
            <span>{{ likeCount }} movie |</span>
            <span>{{ followersCount }} followers |</span>
            <span>{{ followingsCount }} followings</span>
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
      ...mapGetters(['profile', 'notMyAccount', 'isFollowing', 'currentUser']),
      likeCount() {
        return this.profile.like_movies?.length
      },
      followersCount() {
        return this.profile.followers?.length
      },
      followingsCount() {
        return this.profile.followings?.length
      },
    },
    
  data() {
    return {
      username: this.$route.params.username,
    }
  },
  methods: {
    ...mapActions(['fetchProfile', 'followProfile', 'updateImg']),

  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style scoped>
@import 'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap';
  * {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
  }
  .app9 {
    /* background-color: #b6b4c2;
    height: 25rem; */
  }
  img {
    border-radius: 70%;
    margin-right: 15px;
  }
</style>