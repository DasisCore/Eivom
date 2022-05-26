<template>
  <li class="comment-list-item" style="list-style:none">
    <div class="d-flex justify-content-between">
      <div>
        <img v-if="comment.user.profile_img" :src="comment.user.profile_img" alt="profile_img" class="profile_img">
        <img v-else class="profile_img" src="@/assets/default_profile.jpg">
        <router-link :to="{ name: 'profile', params: { username: comment.user.username } }">
          <span>{{ comment.user.username }} </span>
        </router-link> 
        
        <span class="spanfont" v-if="!isEditing">{{ payload.content }}         </span>

        <span v-if="isEditing">
          <input type="text" v-model="payload.content">
          <button class="yp-btn yp-btn-white" @click="onUpdate">Update</button> |
          <button class="yp-btn yp-btn-white" @click="switchIsEditing">Cancle</button>
        </span>

        <span v-if="currentUser.username === comment.user.username && !isEditing">
          <button style="color:gray; font-size:12px;" class="btn btn-link" @click="switchIsEditing">Edit</button>
          <button style="color:gray; font-size:12px;" class="btn btn-link" @click="deleteComment(payload)">Delete</button>
        </span>
      </div>
      <p>{{ comment.created_at }}</p>
    </div>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'article_comment_item',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },
}
</script>

<style scoped>
@import 'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap';
  * {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
  }
  .spanfont {
    font-weight: 300;
  }
  img {
    width: 50px;
    border-radius: 70%;
  }
  a {
    text-decoration: none;
    color: black;
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
    height: 30px;
    width: 80px;
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