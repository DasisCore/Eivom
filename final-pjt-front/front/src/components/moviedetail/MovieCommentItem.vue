<template>
  <div>
    <div id="comment">
      <!-- <div class="d-flex">
        <img src="@/assets/director1.jpg" alt="">
        <div>영화 댓글</div>
      </div> -->
      <div class="d-flex justify-content-between">
        <div class="d-flex">
          <div class="box" style="background: #BDBDBD;">
            <img v-if="profile_img" class="profile" :src="profile_img">
            <img v-else class="profile" src="@/assets/default_profile.jpg">
          </div>
          <div class="ms-3">
            <div class="d-flex">
              <div>{{ comment.user.username }}</div>
              <div class="d-flex" style="margin-left:10px;">
                <button v-if="!isEditing" @click="switchIsEditing">수정</button>
                <button v-if="isEditing" @click="onUpdate">업데이트</button>
                <button @click="delete_movie_Comment(payload)">삭제</button>
                <button v-if="isEditing" @click="switchIsEditing">취소</button>
              </div>
            </div>
            <div v-if="!isEditing">{{ payload.content }}</div>
            <span v-if="isEditing">
              <input type="text" v-model="payload.content">
            </span>
          </div>
        </div>
        <div class="d-flex">
          <div>
            <div id="star" class="text-end">{{ counting_star }}</div>
            <div>{{ comment.updated_at }}</div>
          </div>
        </div>
      </div>
    </div>


  </div>
  
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'movie_comment_item',
  props:{
    comment: Object,
  },
  data: function(){
    return {
      isEditing: false,
      payload: {
        moviePk: this.comment.movie,
        commentPk: this.comment.id,
        content: this.comment.content
      },
    }
  },
  computed: {
    counting_star() {
      return `★`.repeat(this.comment.rate)
    },
    profile_img() {
      return this.comment.profile_img
    }
  },
  methods: {
    ...mapActions(['delete_movie_Comment', 'update_movie_Comment' ]),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.update_movie_Comment(this.payload)
      this.isEditing = false
    },
  }
}
</script>

<style scoped>

  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

  #comment {
    margin: 10px 10px 10px 10px;
    padding: 10px 20px 10px 10px;
    font-family: 'Noto Sans KR',  sans-serif;
    font-size: 1.5rem;
    font-weight: 500;
    border-radius: 5px;
    background-color:	#ffffff;
    /* border-bottom: 1.5px solid #bcbcbc; */
  }

  .box {
      width: 65px;
      height: 65px; 
      margin: 5px;
      border-radius: 70%;
      overflow: hidden;
  }
  .profile {
      width: 100%;
      height: 100%;
      object-fit: cover;
  }

  #star {
    color: rgb(250, 187, 0);
  }

  button {
    border: none;
    font-family: 'Noto Sans KR',  sans-serif;
    font-size: 0.9rem;
    font-weight: 300;
    background-color: rgba(255, 255, 255, 0);
    color: #acacac;
    margin-right: 5px
  }
</style>