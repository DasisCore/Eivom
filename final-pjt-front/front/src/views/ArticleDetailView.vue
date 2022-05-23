<template>
  <div>
    <div class="d-flex justify-content-between">
      <h3>{{ article.title }}</h3>
      <div>
        <div v-if="isAuthor">
          <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
            <button>Edit</button>
          </router-link>
          |
          <button @click="deleteArticle(articlePk)">Delete</button>
        </div>
      </div>
    </div>
    <hr>
      <div class="d-flex">
        <div>
          <img :src="article.user.profile_img" alt="profile_img" class="profile_img">
        </div>
        <div>
          <p>{{ article.user.username }}</p>
          <p>{{ article.created_at }}</p>
        </div>
      </div>
    <hr>
    <p>{{ article.content }}</p>
    
    <!-- Article Edit/Delete UI -->
    

    <!-- Article Like UI -->
    <div class="d-flex">
      <button
        @click="likeArticle(articlePk)"
      >좋아요</button>
      <span>좋아요 {{ likeCount }}</span> |
      <div>
        <i class="fa-regular fa-comment"></i>
        댓글 {{ article.comments.length }}
      </div>
    </div>
    <hr>
    <!-- Comment UI -->
    <article-comment-list :comments="article.comments"></article-comment-list>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import ArticleCommentList from '@/components/community/ArticleCommentList.vue'



  export default {
    name: 'ArticleDetail',
    components: { ArticleCommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article']),
      likeCount() {
        return this.article.article_like?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ])
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style>

.profile_img {
  width: 60px;
  height: 60px;
}
</style>
