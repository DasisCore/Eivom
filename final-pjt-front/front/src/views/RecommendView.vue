<template>
  <div class="app6">
    RecommendView
    <recommend></recommend>
  </div>
</template>

<script>
import Recommend from '../components/recommend/Recommend.vue'


export default {
  name: 'RecommendView',
  components: {
    Recommend,
  },
}
</script>

<style scoped>
  .app6 {
    height: 100vh;
    background-color: #dccbb7
  }
</style>
