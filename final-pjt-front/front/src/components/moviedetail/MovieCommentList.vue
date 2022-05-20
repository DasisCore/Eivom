<template>
  <div style="background-color: #a3d2c2 ">
    영화 댓글 컴포넌트
    <p></p>
    <div>
      <movie-comment-item></movie-comment-item>
      <movie-comment-item></movie-comment-item>
      <movie-comment-item></movie-comment-item>
      <movie-comment-item></movie-comment-item>
      <movie-comment-item></movie-comment-item>
    </div>
    <div class="form-floating">
      <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea2" style="height: 100px"></textarea>
      <label for="floatingTextarea2">Comments</label>
      <button class="btn btn-primary">댓글 등록</button>
    </div>
    <br>
  </div>
</template>

<script>
import MovieCommentItem from './MovieCommentItem.vue'

export default {
  name: 'movie_comment_list',
  components: {
    MovieCommentItem,
  }

}
</script>

<style scoped>

</style>