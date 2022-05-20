<template>
  <div class="app">
    Community View
    <div class="d-flex">
      <article-list></article-list>
      <community-card></community-card>
    </div>
    <div class="d-flex justify-content-center">
      <pagination></pagination>
    </div>
  </div>
</template>

<script>
import ArticleList from '../components/community/ArticleList.vue'
import CommunityCard from '../components/community/CommunityCard.vue'
import Pagination from '../components/community/Pagination.vue'



export default {
  name: 'CommunityView',
  components: {
    ArticleList, CommunityCard, Pagination
  }
}
</script>

<style scoped>
.app {
  height: 80rem;
  background-color: #0f7aa0
}

</style>