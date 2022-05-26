<template>

  <div class="appdetail">
    <div class="margin">
      <div class="d-flex justify-content-between align-items-end">
        <h3>{{ article.title }}</h3>
        <div>
          <div v-if="isAuthor">
            <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
              <button class="yp-btn yp-btn-white button">Edit</button>
            </router-link>
            <button class="yp-btn yp-btn-white button" @click="deleteArticle(articlePk)">Delete</button>
          </div>
        </div>
      </div>
      <hr>
        <div class="d-flex align-items-center">
          <div>
            <img v-if="article.user.profile_img" :src="article.user.profile_img" alt="profile_img" class="profile_img">
            <img v-else class="profile" src="@/assets/default_profile.jpg">
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
      <div class="d-flex align-items-center">
        <button v-if="articleLiking" class="btn btn-link shadow-none" style="color:crimson; font-size:25px;"
          @click="likeArticle(articlePk)"
        ><i class="fa-solid fa-heart"></i></button>
        <button v-else class="btn btn-link shadow-none" style="color:crimson; font-size:25px;"
          @click="likeArticle(articlePk)"
        ><i class="fa-regular fa-heart"></i></button>
        <!-- {{ article.article_like }} -->
        <div class="likecomment">
          <span>좋아요 {{ likeCount }}</span> |
          <div>
            <i class="fa-regular fa-comment"></i>
            댓글 {{ article.comments.length }}
          </div>
        </div>
      </div>
      <hr>
      <!-- Comment UI -->
      <article-comment-list :comments="article.comments"></article-comment-list>
      <hr>
      <router-link :to="{ name: 'community' }">
        <button class="yp-btn yp-btn-white">목록</button>
      </router-link>
    </div>
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
      ...mapGetters(['isAuthor', 'article', 'articleLiking', 'currentUser']),
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

<style scoped>
@import 'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap';
  * {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
  }
.appdetail{
  /* margin-top: 3rem; */
  margin-left: 20rem;
  margin-right: 20rem;
  height: 80rem;
  background-color: #fff6ea;
}
.margin {
  margin: 25px;
}
.profile_img {
  width: 60px;
  height: 60px;
  border-radius: 70%;
}
.userinfo {
  display: flex;
  flex-direction: column;
}
.likecomment {
  display: flex;
  width: 150px;
  justify-content: space-between;
}
img {
  margin-right: 5px;
}
.button {
  margin:10px;
}
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
    border: 1.5px solid rgb(9, 9, 56);
  }

  .yp-btn {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 500;
    position: relative;
    height: 43.1px;
    width: 120px;
    z-index: 1;
  }
  .yp-btn.yp-btn-xs {
    padding: 4px 15px;
  }
  .yp-btn.yp-btn-sm {
    padding: 8px 20px;
  }
  .yp-btn.yp-btn-md {
    padding: 15px 40px;
  }
  .yp-btn.yp-btn-lg {
    padding: 15px 50px;
  }
  .yp-btn.yp-btn-full {
    margin-left: 0;
    margin-right: 0;
    width: 100%;
  }
  .yp-btn:before {
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
