<template>
  <div>
  <form @submit.prevent="onSubmit" class="article-comment-list-form">
    <label for="comment"></label>
    <input type="text" id="comment" v-model="content" required>
    <button>Comment</button>
  </form>
  <router-link :to="{ name: 'community' }">
    <button>목록</button>
  </router-link>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ArticleCommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['article']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ articlePk: this.article.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>
.comment-list-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
}
</style>