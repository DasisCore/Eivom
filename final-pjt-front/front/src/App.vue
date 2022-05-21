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
          <router-link to="/" class="nav-link fw-bold text-secondary"
            active-class="active">Search icon</router-link>
          <router-link to="/profile" class="nav-link fw-bold text-secondary"
            active-class="active">Profile</router-link>
          <router-link to="/login" class="nav-link fw-bold text-secondary"
            active-class="active">Login icon</router-link>
        </div>
      </ul>
    </nav>
    <router-view/>

    <footer class="fs-3 text-center">
      footerbar
    </footer>
  </div>
</template>

<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Julius+Sans+One|Open+Sans:300,400');

  nav {
  height: 100%;
  font-family: 'Open Sans', sans-serif;
  font-size: 14px;
  background-color: rgba(244, 244, 244, 0.789);
  }
  
  /* a:hover {
    cursor: pointer;
    color: black !important;
    border-bottom: solid 3px;
    border-bottom-color: gray ;
  } */
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


</style>
