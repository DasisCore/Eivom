<template>
  <div class="app">
    <div>
      <div class="d-flex">
        <div>
          <article-list></article-list>
          <!-- <div class="d-flex justify-content-center">
            <pagination></pagination>
          </div> -->
        </div>
        <div>
          <community-card></community-card>
        </div>
      </div>
      
    </div>
    
  </div>
</template>

<script>
import ArticleList from '../components/community/ArticleList.vue'
import CommunityCard from '../components/community/CommunityCard.vue'
// import Pagination from '../components/community/Pagination.vue'



export default {
  name: 'CommunityView',
  components: {
    ArticleList, CommunityCard
    // , Pagination
  }
}
</script>

<style scoped>
.app {
  height: 40rem;
}

</style>