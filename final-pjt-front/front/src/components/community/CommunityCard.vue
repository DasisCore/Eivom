<template>
    <div class="app3">
      <h2>이 영화는 어떠세요?</h2>
      <community-card-item></community-card-item>
    </div>
</template>

<script>
import CommunityCardItem from './CommunityCardItem.vue'

export default {
  name: 'community_card',
  components: {
    CommunityCardItem,
  },
}
</script>

<style>
  .app3 {
    height: 600px;
    width: 40rem;
    background-color: #b7d7e2;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
</style>