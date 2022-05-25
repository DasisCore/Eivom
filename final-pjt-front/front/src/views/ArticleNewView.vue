<template>
  <div>
    <!-- <h1>New Article</h1> -->
    <article-form :article="article" action="작성하기"></article-form>
  </div>
</template>

<script>
  import ArticleForm from '@/components/community/ArticleForm.vue'
  export default {
    name: 'AritcleNewView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          pk: null,
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style></style>
