<template>
  <div class="app3">
    Comunity Card
    <div>
      <community-card-item></community-card-item>
      <p></p>
      <community-card-item></community-card-item>
    </div>
  </div>
</template>

<script>
import CommunityCardItem from './CommunityCardItem.vue'

export default {
  name: 'community_card',
  components: {
    CommunityCardItem,
  }
}
</script>

<style>
  .app3 {
    height: 1000px;
    width: 40rem;
    background-color: #b7d7e2;
  }
</style>