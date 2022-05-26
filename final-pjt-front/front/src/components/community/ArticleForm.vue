<template>
  <div class="container">
    <form @submit.prevent="onSubmit">
      <div class="input">
        <input class="title_input form-control" v-model="newArticle.title" type="text" id="title" placeholder="제목을 입력하세요."/>
        <button class="yp-btn yp-btn-white">{{ action }}</button>
      </div>
      <div>
        <textarea class="content_input form-control" v-model="newArticle.content" type="text" id="content" placeholder="내용을 입력하세요."></textarea>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === '작성하기') {
          this.createArticle(this.newArticle)
        } else if (this.action === '수정하기') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }
</script>

<style scoped>
  .container {
    background-color: #fff6ea;
    margin-top: 1rem;
    height: 800px;
  }
  .input{
    display:flex;
    justify-content: space-between;
    align-items: center;
  }
  .title_input {
  width: 1180px;
  border: 1px solid var(--toast-border);
  background-color: white;
  border-radius: 4px;
  padding: 0.6rem;
  margin-top: 1rem;
  margin-right: 0.5rem;
  margin-bottom: 1rem;
  padding-left: 1.5rem;
  outline: none;
}
.content_input {
  width: 100%;
  height: 700px;
  border: 1px solid var(--toast-border);
  background-color: white;
  border-radius: 4px;
  padding: 0.6rem;
  margin-right: 0.5rem;
  margin-bottom: 2rem;
  padding-left: 1.5rem;
  outline: none;
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
