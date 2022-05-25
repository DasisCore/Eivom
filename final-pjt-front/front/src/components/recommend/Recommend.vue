<template>
  <div>
    <div class="container" style="background-color: #111;">
      <input type="checkbox" id="box" name="box">
      <label for="box" class="yp-btn yp-btn-white">Button</label>
    </div>
  </div>
</template>

<script>
export default {
  name: 'recommend_algo',

}
</script>

<style scoped>


  /* Buttons */
  .yp-btn,
  .yp-btn:hover,
  .yp-btn:focus,
  .yp-btn:active {
    color: #fff;
    text-decoration: none;
    outline: none;
  }

  .yp-btn {
    display: inline-block;
    position: relative;
    margin-left: 5px;
    margin-right: 5px;
    padding: 5px 10px;
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
    border: 2px solid #fff;
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
  }
  .yp-btn-white:hover:before,
  .yp-btn-white:focus:before,
  .yp-btn-white.focus:before,
  .yp-btn-white:active:before,
  .yp-btn-white.active:before {
    border: 2px solid #fff;
    background: #fff;
  }

</style>