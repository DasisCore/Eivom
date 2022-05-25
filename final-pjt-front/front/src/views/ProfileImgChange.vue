<template>
  <div>

    {{ this.profile.profile_img }}
    {{ this.profile.username }}
    <input type="text" v-model="this.profile.profile_img">
    <button @click="onUpdate">Update</button> |
    <button @click="switchIsEditing">Cancle</button>

    <span v-if="profile.username === currentUser.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
    </span>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'profile_item',
  data() {
    return {
      isEditing: false,
      payload: {
        profile_img: this.profile.profile_img,
        username: this.profile.username
      }
    }
  },
  computed: {
      ...mapGetters(['profile', 'notMyAccount', 'isFollowing', 'currentUser']),
  },
  methods: {
    ...mapActions(['fetchProfile', 'followProfile', 'updateImg']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateImg(this.payload)
      this.isEditing = false
    }
  },
}
</script>

<style>

</style>