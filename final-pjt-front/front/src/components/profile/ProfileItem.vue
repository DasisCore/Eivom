<template>
  <div class="app9">
    <div class="p-5">
      <div class="d-flex justify-content-center">
        <div class="d-flex flex-column">
          <img :src="profile.profile_img" alt="profile_img">
          {{ isEditing }}
          <!-- <span v-if="!isEditing">1234</span> -->
          <!-- {{ isEditing }} -->
          <!-- <input type="text" v-model="payloads.img"> -->
          <span v-if="isEditing">
            <input type="text">
            <button @click="onUpdate">Update</button> |
            <button @click="switchIsEditing">Cancle</button>
          </span>
          <span v-if="profile.username === currentUser.username && !isEditing">
            <button @click="switchIsEditing">Edit</button> |
          </span>
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
      isEditing: false,
      // payloads: {
      //   username: this.profile.username,
      //   img: this.profile.profile_img,
      // },
    }
  },
  methods: {
    ...mapActions(['fetchProfile', 'followProfile', 'updateImg']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateImg(this.payloads)
      this.isEditing = false
    }
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