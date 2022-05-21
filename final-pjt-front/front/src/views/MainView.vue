<template>
  <div>

    <!-- 첫 메인화면 -->
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

    <!-- 움직이는 영상 + 영화 이름 -->
    <div class="" style="position: relative;">
      <video class="main_video" muted="" autoplay="" loop="" data-inline-media=""  preload="none" width="100%" height="100%" src="../assets/LaLa.mp4"></video>
      <div class="center">
        <div class="title">
          <h3 class="display-1">La La LAND</h3>
          <h3 class="fs-5">2016</h3>
        </div>
      </div>
    </div>

    <!-- 중간 파트 -->
    <div class="container">
      <div id="middle" class="d-flex justify-content-center">
        <div>
          <!-- 크기 가로 900 세로 1000으로 자른 뒤, css 이용해 height 600px로 조절 -->
          <div class="d-flex highlight">
            <img src="../assets/highlight.jpg" alt="highlight" class="img1">
            <div id="main_sentense" class="ms-5">
              <h3 class="display-1">감정의</h3>
              <h3 class="display-1">폭발.</h3>
            </div>
          </div>
          <div class="director">
            <div class="d-flex align-items-center">
              <p id="highlight_sen" class="me-5">
                차들로 빽빽이 들어찬 LA의 고속도로. 거북이 걸음이던 도로가 뚫리기 시작하지만 미아 지금 손에 든 연기 오디션 대본을 놓지 못한다. 세바스찬은 경적을 누르며 미아를 노려보고는 사라진다. 악연의 시작. 이후 미아는 감미로운 피아노 선율에 이끌려 재즈바로 향하는데, 연주자가 바로 세바스찬이다. 미아가 세바스찬에게 인사를 건네려고 다가가던 순간은 하필 그가 재즈바의 레퍼토리를 무시하고 연주한 탓에 해고된 직후. 세바스찬은 인사를 건네려 다가온 미아를 쌩하니 스쳐 지나가버린다. 세 번째로 두 사람은 파티에 온 손님과 출장 밴드의 키보드 연주자로 다시 만나는데...
              </p>
              <img id="director" src="../assets/director2.jpg" alt="">
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- back image + 제작노트 or 평론 부분 -->
    <div class="" style="position: relative;">
      <img class="main_video" src="../assets/back.jpg" alt="">
      <div class="center">
        <div class="title d-flex justify-content-center">
          <div id="review">
            <div>
              <p class="">&#60;라라랜드&#62;는 현실적인 공감을 얻을 이야기를 바탕으로 아름다운 LA의 사계절 아래 감미로운 선율의 음악과 다채로운 색채의 향연, 화려한 의상과 최고의 프로덕션을 선사하며 관객들을 황홀경으로 이끈다. 다미엔 차젤레 감독은 다양한 고전 영화에 대한 오마주는 물론 할리우드를 향한 애정과 존경을 영화 전반에 걸쳐 가감 없이 드러냈다. 또한 1950년대 할리우드 영화들이 많이 사용하던 2.55:1 비율의 시네마스코프 사이즈로 촬영해 고전 영화적인 느낌을 살렸다.</p>
              <p class="text-end">제작 노트 중.</p>
            </div>
          </div>
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
  import _ from 'lodash'
  let num = _.random(1, 9)
  console.log(num)

  export default {
    name: 'MainView',
    components: {
      MainCardList,
    },
    data: function() {
      return {
        
      }
    },
    created: {
      
    }
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

  /* @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@700&family=Open+Sans:ital,wght@1,800&display=swap'); */
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');
  /* @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;700&display=swap'); */
  #detail {
    height: 100vh;
  }

  .img1 {
    height: 600px
  }

  #middle {
    margin-top: 13rem;
    margin-bottom: 13rem;
  }

  .highlight {
    z-index: 10;
  }

  #main_sentense {
    padding-top: 150px;
  }

  #highlight_sen {
    color: #6e6e73;
    width:400px;
    padding-top: 100px;
  }

  .director {
    position: relative;
    top: -70px;
    left: 40px;
    z-index: -10;
  }

  #director {
    width: 20rem;
  }

  #review > div > p {
    width: 50vw;
    font-size: 0.75vw;
    color: #ffffffd1;
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
  }

  h1 {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 700;
  }

  h3 {
    font-family: 'Open Sans', sans-serif;
    font-weight: 700;
  }

  p {
    font-family: 'Noto Sans KR','Open Sans',  sans-serif;
    font-weight: 500;
  }

  .main {
    height: 100vh;
  }
  
  .main_video {
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