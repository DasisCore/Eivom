<template>
  <div class="col-3 movie">
    <!-- <img :src="`https://image.tmdb.org/t/p/original${poster_path}`" alt="">
    <h4>{{ title }}</h4> -->
    <div class="containers">
      <img :src="`https://image.tmdb.org/t/p/original${poster_path}`" alt="">
      <div class="overlay">
        <div class = "items"></div>
        <div class = "items head">
          <p>{{ title }}</p>
          <hr>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
const URL = "https://api.themoviedb.org/3/movie/"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default {
  name: 'profile_movie_item',
  props: {
    movie: Object,
  },
  data: function(){
    return {
      title: '',
      poster_path: '',
    }
  },
  created() {
    axios.get(URL + this.movie.movie_id, {
      params: {
        api_key: API_KEY,
        language: 'ko-KR',
      }
    })
      .then(res => {
      this.title = res.data.title
      this.poster_path = res.data.poster_path
      // console.log(res.data)
      })
      .catch(err => console.log(err))
  }
}
</script>

<style scoped>
  .movie {
    margin-bottom: 30px;
  }
  img {
    width: 300px;
    height: 450px;
    position: absolute;
    border-radius: 9px;
  }
  h4 {
    text-align: center;
  }
  body {
  background-color: #FEF5DF;
}

.containers {
  width: 300px;
  height: 450px;
  background: url("https://image.tmdb.org/t/p/original${poster_path}");
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  margin: auto;
  background-color: black;
  background-size: cover;
  cursor: pointer;
  -webkit-box-shadow: 0 0 5px #000;
  box-shadow: 0 0 5px #000;
  border-radius: 9px;
}
.overlay {
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr 2fr 2fr 1fr;
  background: rgba(77, 77, 77, 0.9);
  color: #FEF5DF;
  opacity: 0;
  transition: all 1.0s;
  font-family: "Playfair Display", serif;
  border-radius: 9px;
}

.items {
  padding-left: 20px;
  letter-spacing: 3px;
}

.head {
  font-size: 30px;
  line-height: 40px;
  transform: translateY(40px);
  transition: all 0.7s;
}

/* .head hr {
  display: block;
  width: 0;
  border: none;
  border-bottom: solid 2px #FEF5DF;
  position: absolute;
  bottom: 0;
  left: 20px;
  transition: all 0.5s;
} */

/* .price {
  font-size: 22px;
  line-height: 10px;
  font-weight: bold;
  opacity: 0;
  transform: translateY(40px);
  transition: all 0.7s;
}
.price .old {
  text-decoration: line-through;
  color: #b3b3b3;
}

.cart {
  font-size: 12px;
  opacity: 0;
  letter-spacing: 1px;
  font-family: "Lato", sans-serif;
  transform: translateY(40px);
  transition: all 0.7s;
}
.cart i {
  font-size: 16px;
}
.cart span {
  margin-left: 10px;
} */

.containers:hover .overlay {
  opacity: 1;
}
.containers:hover .overlay .head {
  transform: translateY(0px);
}
.containers:hover .overlay hr {
  width: 75px;
  transition-delay: 0.4s;
}
/* .containers:hover .overlay .price {
  transform: translateY(0px);
  transition-delay: 0.3s;
  opacity: 1;
}
.containers:hover .overlay .cart {
  transform: translateY(0px);
  transition-delay: 0.6s;
  opacity: 1;
} */
</style>