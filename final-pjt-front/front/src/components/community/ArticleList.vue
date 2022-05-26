<template>
  <div class="haha">
    <div class="community d-flex justify-content-between">
      <h1>커뮤니티</h1>
      <router-link :to="{ name: 'articleNew' }">
        <button class="yp-btn yp-btn-white">게시글 작성</button>
      </router-link>
    </div>
    <div class="board">
      <table>
          <thead class="board__header">
            <tr>
              <th class="board__header__row" style="width: 4rem">번호</th>
              <th class="board__header__row">제목</th>
              <th class="board__header__row" style="width: 10rem">글쓴이</th>
              <th class="board__header__row" style="width: 8rem">작성일</th>
              <!-- <th class="board__header__row" style="width: 4rem">조회수</th> -->
            </tr>
          </thead>

          <tbody
          v-for="article in articles"
          :key="article.pk"
          class="board__body"
          >
            <tr>
              <td class="board__body__row">{{ article.pk }}</td>
              <router-link :to="{ name: 'article', params : { articlePk: article.pk} }">
                <td class="board__body__row hover">
                  {{ article.title }}
                  <!-- <span class="board__comment"
                    >[{{ article.comments_count }}]</span -->
                  
                </td>
              </router-link>
              <td class="board__body__row">
                <router-link :to="{ name: 'profile', params: { username: article.user.username } }">
                  {{ article.user.username }}
                </router-link> 
              </td>
              <td class="board__body__row">
                {{ article.created_at }}
              </td>
              <!-- <td class="board__body__row">{{ article.post_hit }}</td> -->
            </tr>
          </tbody>
      </table>
    </div>



    <!-- <div class="d-flex justify-content-center">
      <pagination></pagination>
    </div> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
// import Pagination from '@/components/community/Pagination.vue'
export default { 
  name: "article_list",
  components: {
    // Pagination
  },
  methods: {
    ...mapActions(['fetchArticles']),
  },
  computed: {
    ...mapGetters(['articles'])
  },
  created() {
    this.fetchArticles()
  },
  
}
</script>

<style scoped>
@import 'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap';
  
  table {
    font-family: 'Noto Sans KR',  sans-serif !important;
  }

  a {
    text-decoration: none;
    color: black;
    margin: 0 0 0 0;
    padding: 0 0 0 0;
  }
  .community {
    margin: 70px 30px 50px 30px;

  }

  .community > h1 {
    font-size: 55px;
    font-weight: 700;
  }

  #commu {
    height: 100%;
    width: 60rem;
  }

  .board table {
    box-shadow: 1px 2px 3px 2px rgba(0, 0, 0, 0.275);
    border-radius: 6px;
    overflow: hidden;
    width: 65vw;
    height: 100%;

  }

  .board__header {
    background-color: #f4f4f5;
    color: black;
  }

  .board__header__row {
    padding: 0.5rem;
    text-align: center;
    font-size: 16px;
    font-weight: 700;
  }
  .board__body {
    background-color: var(--board-body);
    /* color: gray; */
    border-top: 2px solid #f2f2f2;
  }
  .board__body__row {
    padding: 0.5rem;
    font-size: 16px;
    text-align: center;
    font-weight: 400;
    /* border-left: 1px solid #f2f2f2; */
  }
  /* th:nth-child(2) {
    width: 100%;
  } */
  /* --------버튼-------- */
  /*---------------------------------------------------- */
  /* 버튼 css */
    /* Buttons */
  
  #sub,
  #sub:hover,
  #sub:focus,
  #sub:active {
    color: rgb(0, 0, 0);
    text-decoration: none;
    outline: none;
    background-color: rgb(255, 255, 255);
    border-radius: 5px;
  }

  #sub {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 500;
    position: relative;
    height: 40px;
    width: 90px;
    z-index: 1;
  }

  #sub:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    /* border: 2px solid #fff; */
    border-radius: 5px;
    z-index: -1;
    /* transform: skew(-6deg); */
    background: none;
    transition: 0.3s background ease, 0.3s border ease;
  }

  .yp-btn,
  .yp-btn:hover,
  .yp-btn:focus,
  .yp-btn:active {
    color: rgb(0, 0, 0);
    text-decoration: none;
    outline: none;
    background-color: rgb(255, 255, 255);
    border-radius: 5px;
    border: 2px solid rgb(25, 25, 84);
  }

  .yp-btn {
    top: 10px;
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 600;
    font-size: 20px;
    position: relative;
    height: 60px;
    width: 220px;
    z-index: 1;
    box-shadow: 3px 5px 6px 1px rgba(0, 0, 0, 0.281);
    
  }

  .yp-btn:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border-radius: 5px;
    z-index: -1;
    background: none;
    transition: 0.3s background ease, 0.3s border ease;
  }


  .yp-btn-white:hover,
  .yp-btn-white:focus,
  .yp-btn-white.focus,
  .yp-btn-white:active,
  .yp-btn-white.active {
    color: rgb(0, 0, 0);
    border: 1px solid #fff;
  }
  .yp-btn-white:hover:before,
  .yp-btn-white:focus:before,
  .yp-btn-white.focus:before,
  .yp-btn-white:active:before,
  .yp-btn-white.active:before {
    /* border: 1px solid #fff; */
    border-radius: 5px;
    background: #FFD2E2;
  }

  input:checked + label {
    background: #FFD2E2;
    border-radius: 5px;
    color: black;
  }

  input {
    visibility: hidden;
  }

  label {
    display: flex;
    justify-content: center;
    align-items: center;
    -webkit-user-select:none;
    -moz-user-select:none;
    -ms-user-select:none;
    user-select:none;
    cursor: pointer;
  }
</style>