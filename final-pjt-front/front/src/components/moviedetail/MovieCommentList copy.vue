<template>
  <div >
    <div id="comment_list" class="container">
      <div id="comment">댓글</div>
      <div>
        <movie-comment-item v-for="comment in get_comments" :key="comment.id" :comment="comment"></movie-comment-item>
      </div>
      
      <div v-if="isLoggedIn" id="comment_writer">
        <form @submit.prevent="create_movie_Comment(commentform)">
          <div class="d-flex row" style="margin: 10px 10px 10px 10px;">
            <div>
              <label for="comment_w" id="user">admin</label>
              <textarea name="" id="comment_w" cols="30" rows="10" autocomplete="off" autocorrect="off" maxlength="200" v-model="commentform.content"></textarea>
            </div>
            <div class=" d-flex justify-content-end">
              <button>등록</button>
            </div>
          </div>
        </form>
      </div>
      <br>
    </div>
  </div>
</template>

<script>
import MovieCommentItem from './MovieCommentItem.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'movie_comment_list',
  components: {
    MovieCommentItem,
  },
  props:{
    movie_id:Object,
  },
  data: function() {
    return {
      commentform: {
        movie_id: this.$route.params.movie_id,
        content: "",
      },

    }
  },
  methods: {
    ...mapActions(['create_movie_Comment']),
    test(){
      console.log(this.movie)
    },
  },
  computed: {
    ...mapGetters(['isLoggedIn', "get_comments", 'get_movie']),
  },
  created() {
  }

}
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');


  #comment_list {
    background-color: #f2f2f2;
    border-radius: 20px;
    /* height: 1000px; */
    margin-bottom: 200px;
  }

  #comment {
    padding: 20px 20px 20px 20px;
    font-family: 'Noto Sans KR',  sans-serif;
    font-size: 3rem;
    font-weight: 700;
    /* border-bottom: 1.5px solid #bcbcbc; */
  }

  #comment_writer {
    margin: 10px 10px 10px 10px;
    background-color: #ffffff;
    border: 2px solid rgba(0, 0, 0, 0.1);
    border-radius: 6px;
    padding: 16px 10px 10px 18px;
  }

  #user {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 900;
    font-size: 17px;
  }

  textarea {
    height: 5.2rem;
    border: none;
    color: black;
    width: 99%;
    font-family: 'Noto Sans KR',  sans-serif;
    padding: 5px 10px 5px 5px;
    outline-color: rgba(255, 255, 255, 0);
    resize: none;
  }

  textarea:focus {
    border: none;
  }

  button {
    border: none;
    background-color: rgba(255, 255, 255, 0);  
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
    color: #9a9a9a;
    margin-bottom: 10px;
    margin-right: 10px;

  }
</style>