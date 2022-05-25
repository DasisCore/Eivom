<template>
  <div class="app9" >
    <div id="back_profile" :style="`background-color:${colors[random_num]}`">
      <div id="movie_logo"> 계정 </div>
      <div class="d-flex justify-content-center">
        <div id="main_profile"  class="d-flex justify-content-between">
          <div class="d-flex flex-column">
            <router-link :to="{ name: 'profileImg' }">
              <img v-if="profile.profile_img" :src="profile.profile_img">
              <img v-else class="profile" src="@/assets/default_profile.jpg">
            </router-link>
          </div>
          <div class="d-flex flex-column" style="margin-top: 80px">
            <div class="d-flex">
              <div style="font-size: 50px">
                <div style="margin:0;">Hello,</div>
                <div>{{ profile.username }}.</div>
              </div>
              <button @click="followProfile(username)" v-if="notMyAccount && isFollowing">언팔로우</button>
              <button @click="followProfile(username)" v-if="notMyAccount && !isFollowing">팔로우</button>

              <!-- 본인 프로필이면 팔로우 버튼 x
              팔로우 상태면 언팔로우버튼
              언팔로우 상태면 팔로우버튼 -->
            </div>
            <div>
              <span>{{ likeCount }} movie &nbsp;</span>
              <span>{{ followersCount }} followers &nbsp;</span>
              <span>{{ followingsCount }} followings</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from "lodash"

import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'profile_item',
  computed: {
      ...mapGetters(['profile', 'notMyAccount', 'isFollowing', 'currentUser']),
      likeCount() {
        return this.profile.like_movies?.length
      },
      followersCount() {
        return this.profile.followers?.length
      },
      followingsCount() {
        return this.profile.followings?.length
      },
    },
    
  data() {
    return {
      username: this.$route.params.username,
      colors : ["#F4BFBF", "#CCF3EE" ,"#E3FCBF", "#FFE69A", "#FFF6EA", "#B3E8E5", "#FFFFFF"],
      // 빨: F4BFBF 파:CCF3EE  초: E3FCBF 노:FFE69A 보:F0D9FF 베이지:FFF6EA 민트:B3E8E5 흰:FFFFFF
      random_num: 0,

    }
  },
  methods: {
    ...mapActions(['fetchProfile', 'followProfile', 'updateImg']),

  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
    this.random_num = _.random(0, 6)
  },
}
</script>

<style scoped>
@import 'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap';
  * {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
  }

  img {
    border-radius: 70%;
    margin-right: 15px;
    width: 300px;
    height: 300px;
  }

  a {
    border-radius: 70%;
    margin-right: 15px;
  }

  #back_profile {
    height: 35rem;
  }

  #movie_logo {
    padding: 50px 50px 50px 200px;
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 700;
    font-size: 2.0rem
  }

  #movie_logo:after {
  content: "";
  display: block;
  width: 56px;
  border-bottom: 2px solid #bcbcbc;
  margin: 3px auto;
  position: absolute;
  margin-left: 3px;
  }

  #main_profile {
    width: 700px
  }

  span {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 700;
    font-size: 1.31rem;
  }

</style>