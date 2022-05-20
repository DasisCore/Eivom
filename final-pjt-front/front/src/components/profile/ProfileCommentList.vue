<template>
  <div class="app12">
    profile comment list
    <!-- v-for 부분 -->
    <profile-comment-item></profile-comment-item>
    <p></p>
    <profile-comment-item></profile-comment-item>
    <p></p>
    <profile-comment-item></profile-comment-item>
    <p></p>
    <profile-comment-item></profile-comment-item>
    <p></p>
    <profile-comment-item></profile-comment-item>
    <!--  -->
    <p></p>
    <input type="text" placeholder="댓글입력창">
    <p></p>
    <button class="btn btn-primary">등록</button>
  </div>
</template>

<script>
import ProfileCommentItem from './ProfileCommentItem.vue'

export default {
  name: 'profile_comment_list',
  components: {
    ProfileCommentItem,
  }
}
</script>

<style scoped>
  .app12 {
    height: 90vh;
    background-color: #f3dbcf;
  }

  input {
    height: 150px;
    width: 80vw;
  }
</style>