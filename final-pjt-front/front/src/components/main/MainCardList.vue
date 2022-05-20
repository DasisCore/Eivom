<template>
  <div>
    MainCardList
    <div class="d-flex">
      <main-card-item class="m-3"></main-card-item>
      <main-card-item class="m-3"></main-card-item>
      <main-card-item class="m-3"></main-card-item>
      <main-card-item class="m-3"></main-card-item>
    </div>
  </div>
</template>

<script>
import MainCardItem from './MainCardItem.vue'

export default {
  name: 'MainCardList',
  components: {
    MainCardItem,
  }
  
}
</script>

<style scoped>

</style>