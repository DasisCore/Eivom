<template>
  <div style="background-color: #dcf6f9">
    <p class="display-3 fw-bold">로그인</p>
    <div class="d-flex justify-content-center">
      <div style="height: 300px">
        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1">@</span>
          <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" style="border-right: 0px;">
          <span class="input-group-text" id="basic-addon1" style="background-color: white;">&#60;</span>
        </div>
        <router-link to="/signup" class="nav-link fw-bold text-secondary fs-1"
        active-class="active">signup</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
}
</script>

<style scoped>

</style>