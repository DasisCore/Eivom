<template>
  <div class="app6">

    <section class="timeline">
      <ul>
        <li>
          <div>
            <time>인사</time>
            <p>Eivom에 오신걸 환영합니다</p>
            <p>간단한 질문 후에 영화를 추천해 드리겠습니다.</p>
          </div>
        </li>
        <li>
          <div style="height: 300px;">
            <time>장르</time>
            이 장르는 있었으면 좋겠어요.
            <buttons id="genres" class="d-flex" style="height:200px;">
              <com class="row" style="width:370px;">
                <com class="d-flex justify-content-around align-items-center">
                  <input type="checkbox" id="action1" value=28 v-model="with_genres">
                  <label for="action1">액션</label>
                  <input type="checkbox" id="animation1" value=16 v-model="with_genres">
                  <label for="animation1">애니메이션</label>
                  <input type="checkbox" id="comedy1" value=35 v-model="with_genres">
                  <label for="comedy1">코미디</label>
                  <input type="checkbox" id="drama1" value=18 v-model="with_genres">
                  <label for="drama1">드라마</label>
                </com>
                <com class="d-flex justify-content-around align-items-center">
                  <input type="checkbox" id="fantasy1" value=14 v-model="with_genres">
                  <label for="fantasy1">판타지</label>
                  <input type="checkbox" id="romance1" value=10749 v-model="with_genres">
                  <label for="romance1">로맨스</label>
                  <input type="checkbox" id="SF1" value=878 v-model="with_genres">
                  <label for="SF1">SF</label>
                  <input type="checkbox" id="thriller1" value=53 v-model="with_genres">
                  <label for="thriller1">스릴러</label>
                </com>
              </com>
            </buttons>
          </div>
        </li>
        <li>
          <div>
            <time>장르</time>
            <p>이 장르는 없었으면 좋겠어요.</p>
            <buttons id="genres" class="d-flex" style="height:200px;">
              <com class="row" style="width:370px;">
                <com class="d-flex justify-content-around align-items-center">
                  <input type="checkbox" id="action2" value=28 v-model="without_genres">
                  <label for="action2">액션</label>
                  <input type="checkbox" id="animation2" value=16 v-model="without_genres">
                  <label for="animation2">애니메이션</label>
                  <input type="checkbox" id="comedy2" value=35 v-model="without_genres">
                  <label for="comedy2">코미디</label>
                  <input type="checkbox" id="drama2" value=18 v-model="without_genres">
                  <label for="drama2">드라마</label>
                </com>
                <com class="d-flex justify-content-around align-items-center">
                  <input type="checkbox" id="fantasy2" value=14 v-model="without_genres">
                  <label for="fantasy2">판타지</label>
                  <input type="checkbox" id="romance2" value=10749 v-model="without_genres">
                  <label for="romance2">로맨스</label>
                  <input type="checkbox" id="SF2" value=878 v-model="without_genres">
                  <label for="SF2">SF</label>
                  <input type="checkbox" id="thriller2" value=53 v-model="without_genres">
                  <label for="thriller2">스릴러</label>
                </com>
              </com>
            </buttons>
          </div>
        </li>
        <li>
          <div>
            <time>옛 영화</time>
            <p>옛날 영화도 좋아 하시나요?</p>
            <com>
              <input name="rel" type="radio" id="yes_rel" v-model="primary_release_date_gte" value="2000" />
              <label for="yes_rel">네</label>
              <input name="rel" type="radio" id="no_rel" v-model="primary_release_date_gte" value="2010" />
              <label for="no_rel">아니요</label>
            </com>
          </div>
        </li>
        <li>
          <div>
            <time>유명도</time>
            <p>유명한 영화 위주로 찾을까요?</p>
            <com>
              <input name="pop" type="radio" id="yes_pop" v-model="sort_by" value="popularity_asc" />
              <label for="yes_pop">네</label>
              <input name="pop" type="radio" id="no_pop" v-model="sort_by" value="popularity_desc" />
              <label for="no_pop">아니요</label>
            </com>
          </div>
        </li>
        <li>
          <div>
            <time>연령</time>
            <p>성인영화도 넣을까요?</p>
            <com>
              <input name="age" type="radio" id="yes_age" v-model="include_adult" value="true" />
              <label for="yes_age">네</label>
              <input name="age" type="radio" id="no_age" v-model="include_adult" value="false" />
              <label for="no_age">아니요</label>
            </com>
          </div>
        </li>
        <li>
          <div>
            <time>평점</time>
            <p>평점이 좋은 영화 위주로 찾을까요?</p>
            <com>
              <input name="vote" type="radio" id="yes_vote" v-model="vote_average_gte" value="6" />
              <label for="yes_vote">네</label>
              <input name="vote" type="radio" id="no_vote" v-model="vote_average_gte" value="4" />
              <label for="no_vote">아니요</label>
            </com>
          </div>
        </li>
        <li>
          <div>
            <p>제출할까요?</p>
            <button @click="submission">제출</button>
          </div>
        </li>
      </ul>
    </section>

    <div style="height: 500px">
      <h1 class="text-center"> 결과창 </h1>
    </div>
    
  </div>
</template>

<script>
// import Recommend from '../components/recommend/Recommend.vue'
import axios from 'axios'
import _ from "lodash"

const URL = "https://api.themoviedb.org/3/discover/movie"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default {
  name: 'RecommendView',
  components: {
    // Recommend,
  },
  data: function() {
    return {
      with_genres: [],
      without_genres: [],
      primary_release_date_gte: "",
      sort_by: "",
      include_adult: false,
      vote_average_gte: 5,
    }
  },
  methods: {
    submission() {
      let with_genre = ""
      for (let i = 0; i < this.with_genres.length - 1; i++){
        with_genre += this.with_genres[i] + ", " 
      }

      let without_genre = ""
      for (let i = 0; i < this.without_genres.length - 1; i++){
        without_genre += this.without_genres[i] + ", " 
      }

      const random_num = _.random(1, 10)

      axios.get(URL, {
        params: {
          api_key: API_KEY,
          language: 'ko-KR',
          with_genres: with_genre + this.with_genres[this.with_genres.length],
          without_genres: without_genre + this.without_genres[this.without_genres.length],
          "primary_release_date.gte": this.primary_release_date_gte,
          sort_by: this.sort_by,
          include_adult: this.include_adult,
          "vote_averagte.gte": this.vote_average_gte
        }
      })
        .then(res => {
          console.log(res.data.results[random_num])
        })
        .catch(err => {
          console.error(err)
        })
    }
  },
  mounted() {
    var items = document.querySelectorAll(".timeline li");

    function isElementInViewport(el) {
      var rect = el.getBoundingClientRect();
      return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <=
          (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
      );
    }

    function callbackFunc() {
      for (var i = 0; i < items.length; i++) {
        if (isElementInViewport(items[i])) {
          items[i].classList.add("in-view");
        }
      }
    }

    // listen for events
    window.addEventListener("load", callbackFunc);
    window.addEventListener("resize", callbackFunc);
    window.addEventListener("scroll", callbackFunc);
  }
}
</script>

<style scoped>

  #genres > com > com > button {
    height: 30px;
    width: 65px;
    font-size: 10px;
  }


  *,
  *::before,
  *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  /* TIMELINE
  –––––––––––––––––––––––––––––––––––––––––––––––––– */


  .timeline ul {
    background: #ffffff;
    padding: 50px 0;
  }

  .timeline ul li {
    list-style-type: none;
    position: relative;
    width: 6px;
    margin: 0 auto;
    padding-top: 50px;
    background: #DBDBDB;
  }

  .timeline ul li::after {
    content: "";
    position: absolute;
    left: 50%;
    bottom: 0;
    transform: translateX(-50%);
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: inherit;
    z-index: 1;
  }
  
  .timeline ul li div {
    position: relative;
    bottom: 0;
    width: 400px;
    padding: 15px;
    background: #c7c9cc;
    border-radius: 7px;
    box-shadow: 10px 10px 10px rgb(173, 173, 173);
  }

  .timeline ul li div::before {
    content: "";
    position: absolute;
    bottom: 3px;
    width: 0;
    height: 0;
    border-style: solid;
  }

  /* 오른쪽 박스 위치 */
  .timeline ul li:nth-child(odd) div {
    left: 45px;
  }

  /* 오른쪽 꼬리표 */
  .timeline ul li:nth-child(odd) div::before {
    left: -12px;
    border-width: 8px 16px 8px 0;
    border-color: transparent #c7c9cc transparent transparent;
  }

  /* 왼쪽 박스 위치 */
  .timeline ul li:nth-child(even) div {
    left: -439px;
  }

  /* 왼쪽 꼬리표 */
  .timeline ul li:nth-child(even) div::before {
    right: -12px;
    border-width: 8px 0 8px 16px;
    border-color: transparent transparent transparent #c7c9cc;
  }


  time {
    display: block;
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 8px;
  }


  /* EFFECTS
  –––––––––––––––––––––––––––––––––––––––––––––––––– */

  .timeline ul li::after {
    transition: background 0.5s ease-in-out;
  }

  .timeline ul li.in-view::after {
    background: #FFD2E2;
  }

  .timeline ul li div {
    visibility: hidden;
    opacity: 0;
    /* transition: all 0.5s ease-in-out; */
  }

  .timeline ul li:nth-child(odd) div {
    transform: translate3d(200px, 0, 0);
  }

  .timeline ul li:nth-child(even) div {
    transform: translate3d(-200px, 0, 0);
  }

  .timeline ul li.in-view div {
    transform: none;
    visibility: visible;
    opacity: 1;
  }


  /* GENERAL MEDIA QUERIES
  –––––––––––––––––––––––––––––––––––––––––––––––––– */

  @media screen and (max-width: 900px) {
    .timeline ul li div {
      width: 250px;
    }
    .timeline ul li:nth-child(even) div {
      left: -289px;
      /*250+45-6*/
    }
  }

  @media screen and (max-width: 600px) {
    .timeline ul li {
      margin-left: 20px;
    }
    .timeline ul li div {
      width: calc(100vw - 91px);
    }
    .timeline ul li:nth-child(even) div {
      left: 45px;
    }
    .timeline ul li:nth-child(even) div::before {
      left: -15px;
      border-width: 8px 16px 8px 0;
      border-color: transparent #f45b69 transparent transparent;
    }
  }


  /* EXTRA/CLIP PATH STYLES
  –––––––––––––––––––––––––––––––––––––––––––––––––– */
  .timeline-clippy ul li::after {
    width: 40px;
    height: 40px;
    border-radius: 0;
  }

  .timeline-rhombus ul li::after {
    clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
  }

  .timeline-rhombus ul li div::before {
    bottom: 12px;
  }

  .timeline-star ul li::after {
    clip-path: polygon(
      50% 0%,
      61% 35%,
      98% 35%,
      68% 57%,
      79% 91%,
      50% 70%,
      21% 91%,
      32% 57%,
      2% 35%,
      39% 35%
    );
  }

  .timeline-heptagon ul li::after {
    clip-path: polygon(
      50% 0%,
      90% 20%,
      100% 60%,
      75% 100%,
      25% 100%,
      0% 60%,
      10% 20%
    );
  }

  .timeline-infinite ul li::after {
    animation: scaleAnimation 2s infinite;
  }

  @keyframes scaleAnimation {
    0% {
      transform: translateX(-50%) scale(1);
    }
    50% {
      transform: translateX(-50%) scale(1.25);
    }
    100% {
      transform: translateX(-50%) scale(1);
    }
  }

</style>
