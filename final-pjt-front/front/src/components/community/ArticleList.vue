<template>
  <div class="app2">
      <h1>커뮤니티</h1>
      <router-link :to="{ name: 'articleNew' }">
        <button>게시글 작성</button>
      </router-link>
    <div class="board">
      <table>
          <thead class="board__header">
            <tr>
              <th class="board__header__row" style="width: 4rem">번호</th>
              <th class="board__header__row">제목</th>
              <th class="board__header__row" style="width: 10rem">글쓴이</th>
              <th class="board__header__row" style="width: 6rem">작성일</th>
              <th class="board__header__row" style="width: 4rem">조회수</th>
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
              <td class="board__body__row">{{ article.post_hit }}</td>
            </tr>
          </tbody>
      </table>
    </div>
    <div class="d-flex justify-content-center">
      <pagination></pagination>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import Pagination from '@/components/community/Pagination.vue'
export default { 
  name: "article_list",
  components: {
    Pagination
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
.app2 {
  height: 600px;
  width: 80rem;
}

.board table {
  box-shadow: 0px 1px 2px 1px rgba(0, 0, 0, 0.1),
    0px 1px 2px 1px rgba(0, 0, 0, 0.06);
  border-radius: 8px;
  overflow: hidden;
  width: 100%;
}

.board__header {
  background-color: lightgrey;
  color: var(--board-header-text);
}

.board__header__row {
  padding: 0.5rem;
  text-align: center;
  font-size: 14px;
  font-weight: 500;
}
.board__body {
  background-color: var(--board-body);
  color: var(--board-body-text);
  border-top: 1px solid var(--board-body-line);
}
.board__body__row {
  padding: 0.5rem;
  font-size: 14px;
  text-align: center;
}
/* th:nth-child(2) {
  width: 100%;
} */
</style>