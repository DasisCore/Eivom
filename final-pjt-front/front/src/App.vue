<template>
  <div id="app">


    
    <nav>
      <ul class="nav align-items-center justify-content-between">
        <div class="d-flex align-items-center justify-content-between">
          <div class="">
            <router-link to="/" class="nav-link fw-bold text-secondary">
              <img src="./assets/Eivom_uppercase.png" alt="" class="nav-link">
          </router-link>
          </div>

          <li class="nav-item short_menu">
            <router-link to="/" class="nav-link fw-bold text-secondary"
            active-class="active">main</router-link>
          </li>

          <li class="nav-item long_menu">
            <router-link to="/recommend" class="nav-link fw-bold text-secondary"
            active-class="active">recommend</router-link>
          </li>

          <li class="nav-item long_menu">
            <router-link to="/community" class="nav-link fw-bold text-secondary"
            active-class="active">community</router-link>
          </li>

          <li class="nav-item long_menu">
            <router-link to="/moviedetail" class="nav-link fw-bold text-secondary"
            active-class="active"> 임시 영화 상세 페이지 링크 </router-link>
          </li>
          
        </div>

        <div class="d-flex me-3">
          <!-- <router-link to="/" class="nav-link fw-bold text-secondary"
            active-class="active">Search icon</router-link> -->
          <div>
            <div class="search-form">
              <div class="search-box">
                <input type="text" />
                <span></span>
              </div>
            </div>
          </div>
          <router-link :to="{ name : 'profile' }" class="nav-link fw-bold text-secondary"
            active-class="active">Profile</router-link>
          <router-link to="/logout" class="nav-link fw-bold text-secondary"
            active-class="active" v-if="isLoggedIn">Logout icon</router-link>
          <router-link to="/login" class="nav-link fw-bold text-secondary"
            active-class="active" v-else>Login icon</router-link>
        </div>
      </ul>
    </nav>
    <router-view/>

    <footer class="fs-3 text-center">
      footerbar
    </footer>
  </div>
</template>


<script>
import { mapGetters } from 'vuex'
export default {
  name: 'App',
  components: {

    },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
}
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Julius+Sans+One|Open+Sans:300,400');

  nav {
  height: 100%;
  font-family: 'Open Sans', sans-serif;
  font-size: 14px;
  background-color: #f5f5f7;
  }
  
  .short_menu:hover:after {
  content: "";
  display: block;
  width: 30px;
  border-bottom: 2px solid #bcbcbc;
  margin: 3px auto;
  }

  .long_menu:hover:after {
  content: "";
  display: block;
  width: 60px;
  border-bottom: 2px solid #bcbcbc;
  margin: 3px auto;
  }


  img {
    height: 3.5rem;
  }

  .active {
    color: black !important;
  }

  /* 
  
  
  
  
  
  */

  @import url(https://fonts.googleapis.com/css?family=Open+Sans:300);
  h1{ text-align:center; font-family: 'Open Sans', sans-serif; font-size:24px; margin-top:10%; color:#33739A;}
  /* 서치 아이콘 위치 설정 */
  .search-form {
    /* position: absolute; */
    /* right: 20%;
    left: 90%; */
    /* top: 100px; */
    margin-right: 10px;
    margin-top: 10px;
    transform: translate(-0%);
  }

  .search-box input[type="text"] {
    border: none;
    background: none;
    z-index: 1;
    width: 25px;
    height: 20px;
    transition: all .25s ease-in .25s;
    color: transparent;
    font-size: .75rem;
    line-height: 25px;
  }
  .search-box input[type="text"]:hover {
    cursor: pointer;
  }
  .search-box input[type="text"]:hover:focus {
    cursor: text;
  }
  .search-box input[type="text"]:hover + span {
    background: rgba(255, 255, 255, 0.2);
  }
  .search-box input[type="text"]:focus {
    width: 250px;
    padding: 0px 15px;
    outline: none;
    color: black;
    background: none;

  }
  .search-box input[type="text"]:focus + span {
    top: -4px;
    width: 250px;
    height: 30px;
    border: none;
    background: #ebeff1;
  }
  .search-box input[type="text"]:focus + span::before {
    width: 2px;
    opacity: 0;
    transition: all .25s ease-in;
  }
  .search-box input[type="text"] + span {
    z-index: -1;
    position: absolute;
    border: 2px solid #948C8C;
    top: 0;
    width: 15px;
    height: 15px;
    transition: all .25s ease-in .25s;
    border-radius: 25px;
    left: 0px;
  }
  .search-box input[type="text"] + span::before {
    transition: all .25s ease-in .5s;
    transform-origin: left top;
    content: '';
    position: absolute;
    width: 8px;
    height: 4px;
    border-radius: 5px;
    background:#948C8C;
    transform: rotate(45deg) translate(26px, -2px);
    top: -9px;
    left: -9px;
  }
</style>
