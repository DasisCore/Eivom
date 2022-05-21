<template>
  <div>

    <div class="main d-flex justify-content-center align-items-center">
      <div>
        <div class="byline">
          <h1 class="display-1">영화,</h1>
          <div class="text-end">
            <h1 class="display-1">그 이상의 즐거움.</h1>
            <h3 class="fw-bold">Movie, Pleasure beyond</h3>
          </div>
        </div>
      </div>
    </div>

    <div class="" style="position: relative;">
      <video class="gifImg" muted="" autoplay="" loop="" data-inline-media=""  preload="none" width="100%" height="100%" src="../assets/LaLa.mp4"></video>
      <div class="center">
        <div class="title">
          <p class="display-1">La La LAND</p>
          <p class="">2016</p>
        </div>
      </div>
    </div>

    <!-- 영화 카드 리스트 -->
    <div class="page d-flex justify-content-center">
      <main-card-list></main-card-list>
    </div>
  </div>
</template>


<script>
import MainCardList from '../components/main/MainCardList.vue'

export default {
  name: 'MainView',
  components: {
    MainCardList,
  },
}

  window.addEventListener('scroll', function(){
      scrollMotion()
  });

  function scrollMotion(){
      const ele = document.querySelectorAll('.title');
      let eleOffsetArr = [];

      ele.forEach(e => {
          let eleOffset = e.getBoundingClientRect().top + window.pageYOffset - 800;
          eleOffsetArr.push(eleOffset)
          console.log(eleOffset)
      });
      
      eleOffsetArr.forEach((offset, idx) => {
              ele[idx].style.cssText = ( window.scrollY > offset 
              ? 'opacity:1; transform: translateY(0);'
              : 'opacity:0; transform: translateY(50px);' )
      });
  }
</script>


<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@700&family=Open+Sans:ital,wght@1,800&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');


  h1 {
    font-family: 'Noto Sans KR','Open Sans',  sans-serif;
  }

  h3 {
    font-family: 'Open Sans', sans-serif;
  }

  p {
    font-family: 'Noto Sans KR','Open Sans',  sans-serif;
  }

  .main {
    height: 100vh;
  }
  
  .gifImg {
    width: 100%;
    filter: brightness(0.7);
  }

  .center {
    position: absolute;
    top: 40%;
    width: 100%;
    text-align: center;
    z-index: 1;
  }

  .page {
    height: 100vh;
  }

  .byline {
      color: #000000;
      opacity: 0;
      transform: translateY(-15px);
      animation: subtext .8s ease-out both;
  }

  .byline {
    animation-delay: 0.5s;
  }

  @keyframes subtext {
      100% {
          opacity: 1;
          transform: translateX(0);
      }
  }

  .title {
    opacity: 0;
    transform: translatey(50px);
    transition: all 0.5s;
    font-size: 20px;
    /* text-align: center; */
    color: #ffffff;
  }

</style>