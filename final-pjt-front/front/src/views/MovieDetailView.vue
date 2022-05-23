<template>
  <div>
    MovieDetailView
    <div class="container-lg">
      <div class="d-flex justify-content-center align-items-center" style="height: 100vh;">
        <div class="container text-end">
          <h2 class="text-uppercase">{{title}}</h2>
          <div>
            <h3>{{original_title}}</h3>
          </div>
        </div>
      </div>
      <div class="container-fluid parallax bg-img1"
      :style="`background: linear-gradient(rgba(0,0,0,.3), rgba(0,0,0,.3)), url('https://image.tmdb.org/t/p/original/${ backdrop_path }');`">
        <div class="heading text-center">
          <!-- <h2>{{restAPI.release_date}}</h2> -->
          <h2 class="text-uppercase">{{title}}</h2>
        </div>
      </div>

      <div class="container-fluid py-5 bg-faded" id="hm">
        <div class="container-xxl d-flex justify-content-end">
          <div>
            <div class="d-flex justify-content-end">
              <div>
                <div class="d-flex">
                  <div v-for=" genre in genres" :key="genre.id">{{ genre.name }}&nbsp;&nbsp;</div>
                  <div>{{ runtime }}</div>
                </div>
                <div class="text-end">
                  개봉일 {{ release_date }}
                </div>
                <div class="text-end">
                  평점 {{ vote_average }}
                  <p></p>
                </div>
              </div>
            </div>
            <div class="text-end" style="width: 550px">
              {{ overview }}
            </div>
          </div>
        </div>
      </div>  

      <!-- <div class="container-fluid parallax bg-img2" 
      :style="`background: linear-gradient(rgba(0,0,0,.3), rgba(0,0,0,.3)), url('https://image.tmdb.org/t/p/original/${ bgImg2 }');`">
        <div class="middle">
          <div class="container" style="max-width: 550px">
            <blockquote class="text-center">
              <i class="fa fa-quote-left fa-3x fa-pull-left" aria-hidden="true"></i>
              <p class="mb-1 lead">Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste nam et facere perspiciatis optio autem facilis minus nostrum suscipit repudiandae. Assumenda, soluta minima. Eligendi possimus quisquam sed, qui ut alias.</p>
              <footer class="text-uppercase text-white">Hayao Miyazaki</footer>
            </blockquote>
          </div>
        </div>
      </div> -->
      <hr>
      <div>
        <similar-movie-list ></similar-movie-list>
        <div class="d-flex">
          <router-link to="/moviedetail" class="nav-link fw-bold text-secondary"
          active-class="active">actor list</router-link>
          <router-link to="/moviedetail/similarmovies" class="nav-link fw-bold text-secondary"
          active-class="active">similar movie list</router-link>
          
        </div>
        <hr>
        <router-view/>
      </div>
      <hr>
      <movie-comment-list></movie-comment-list>


    </div>
  </div>
</template>

<script>
import MovieCommentList from '../components/moviedetail/MovieCommentList.vue'
import axios from "axios"
// import _ from "lodash"

const URL = "https://api.themoviedb.org/3/movie/"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY


export default {
  name: 'MovieDetailView',
  // props: {
  //   movieID: Number,
  // },
  data: function(){
    return {
      movieID: 453395,
      title: '',
      original_title: '',
      backdrop_path: '',
      genres: [],
      release_date: '',
      runtime: '',
      vote_average: '',
      overview: '',
    }
  },
  components: {
    MovieCommentList,
  },
  created() {
    axios.get(URL + this.movieID, {
      params: {
        api_key: API_KEY,
        language: 'ko-KR',
      }
    })
      .then(res => {
      this.title = res.data.title
      this.original_title = res.data.original_title
      this.backdrop_path = res.data.backdrop_path
      this.genres = res.data.genres
      this.release_date = res.data.release_date

      const hour = parseInt(res.data.runtime / 60)
      const min = parseInt(res.data.runtime % 60)
      this.runtime = hour + "h " + min + "m"

      this.vote_average = res.data.vote_average
      this.overview = res.data.overview
      console.log(res.data)
      })

  }
}
</script>

<style scoped>

  .active {
    color: black !important;
  }

  /* .active {
    color: red;
  } */

  .loading {
    margin-top: 3.5rem;
    width:100%;
    height:100%;
    position:fixed;
    left:0px;
    top:0px;
    background:#fff;
    z-index:1000;
    transition: opacity 1s;
  }

  @import url('https://fonts.googleapis.com/css?family=Julius+Sans+One|Open+Sans:300,400');

  body, html {
    height: 100%;
    font-family: 'Open Sans', sans-serif;
    font-size: 14px;
  }

  h1 {
    font-family: 'Julius Sans One', sans-serif;
    font-size: 4.5rem;
    letter-spacing: 0.5rem;
  }

  h2 {
    font-family: 'Julius Sans One', sans-serif;
    font-size: 2.5rem;
    letter-spacing: 0.5rem;
  }

  p {
    margin-top: 1rem;
  }

  a {
    color:#5bc0de;
  }

  a:hover {
    color: #31b0d5;
    text-decoration: none;
  }

  #hm {
    min-height: 100%;
    height: 300px;
  }

  .heading {
    color: #FFF;
    left: 0;
    position: absolute;
    text-align: center;
    top: 40%;
    width: 100%;
  }

  .middle {
    color: #FFF;
    left: 0;
    position: absolute;
    text-align: center;
    top: 30%;
    width: 100%;
  }

  .bg-img1 {
    background-repeat: no-repeat;
    background-size: cover !important;
    /* background: linear-gradient(rgba(0,0,0,.3), rgba(0,0,0,.3)), url('https://wallpapercave.com/wp/wp1906348.png'); */
    height: 800px;
  }

  .bg-img2 {
    background-repeat: no-repeat;
    background-size: cover !important;
    /* background: linear-gradient(rgba(0,0,0,.3), rgba(0,0,0,.3)), url('https://i.pinimg.com/originals/96/18/6b/96186b308addc3c4700a26adb3aac278.gif'); */
    height: 1000px;
}

  .parallax {
    background-attachment: fixed !important;;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    min-height: 100%;
    position: relative;
  }

  .container {
    margin-right: auto;
    margin-left: auto;
    max-width: 850px;
  }

  .card {
    margin-bottom: 1rem;
    margin-top: 1rem;
  }

  .card-text {
    font-size: 1rem;
    font-weight: 300;
  }

  @media only screen and (max-device-width: 1024px) {
    .parallax {background-attachment: scroll;}
    .heading {top: 30%;} 
    .middle {top: 15%;}
  }

</style>