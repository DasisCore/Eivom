<template>
  <div class="app12">
    profile comment list
    <ul>
      <!-- <profile-comment-list-item 
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.pk">
      </profile-comment-list-item>         -->
      <profile-comment-list-item>
      </profile-comment-list-item> 
    </ul>

    <profile-comment-list-form></profile-comment-list-form>
  </div>
</template>

<script>
import ProfileCommentListItem from './ProfileCommentListItem.vue'
import ProfileCommentListForm from './ProfileCommentListForm.vue'

export default {
  name: 'profile_comment_list',
  components: {
    ProfileCommentListItem,
    ProfileCommentListForm
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