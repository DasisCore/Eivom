<template>
    <div class="app3">
      <h3>이 영화 어때요</h3>
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

<style scoped>
@import 'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap';
  * {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
  }
  .app3 {
    height: 330px;
    /* width: 40rem; */
    /* background-color: lightgrey; */
    /* border: 2px solid; */
    display: flex;
    flex-direction: column;
    /* align-items: center; */
    justify-content: center;
    margin-top: 5rem;
    border-radius: 25px;
  }
</style>