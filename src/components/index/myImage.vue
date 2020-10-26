<template>
  <div class="create-container">
    <div class="create-title">
      <h2 class="white" v-if="screenWidth>767">创意空间</h2>
      <h3 class="white" v-else>创意空间</h3>
      <p v-text="info" class="white"></p>
      <div class="my-create-button">
        <el-button @click="$router.push('/imgDisplay')">点击进入图片专区</el-button>
      </div>
    </div>
    <div class="create-main">
      <div class="create-wraper">
        <img src="./../../assets/career/img/mockups/ipad-white.svg" alt="" width="100%">
        <transition-group appear mode="in-out" enter-active-class="animated fadeIn" leave-active-class="animated fadeOut">
          <div class="create-item" v-for="(item, index) in images" :key="item.img_url+index" v-show="flag==index&&index<3">
          <router-link to="/imgDisplay">
            <img v-lazy="item.img_url" width="100%" height="100%">
          </router-link>
        </div>
        </transition-group>
      </div>
      <div v-for="(item, index) in images" :key="item.img_url" v-if="images&&images.length" v-show="index<3" class="create-navgition">
        <div class="create-navgition-item" @click="change(index)" :class="{'create-focus':index==flag}"></div>
      </div>
    </div>
    <div style="margin-bottom:5rem"></div>
  </div>
</template>
<style lang="less" scoped>
.create {
  &-container {
    width: 100%;
    position: relative;
    background-color: #4fcead;
    overflow: hidden;
  }
  &-focus {
    background-color: #fff !important;
  }
  &-navgition {
    position: relative;
    width: 6rem;
    left: 50%;
    margin-left: -3rem;
    @media screen and (max-width: 767px) {
      margin-left: -3.5rem;
    }
    clear: none;
    &-item {
      width: 1rem;
      height: 1rem;
      border: 1px solid #ccc;
      background-color: #ccc;
      border-radius: 1rem;
      margin-left: 1rem;
      float: left;
      clear: none;
      transition: all 0.5s ease;
      &:hover {
        background-color: #fff;
        transition: all 0.5s ease;
        cursor: pointer;
      }
    }
  }
  &-main {
    position: relative;
    float: left;
    clear: none;
    width: 55%;
    left: 5%;
    top: 3rem;
    overflow: hidden;
    @media screen and (max-width: 767px) {
      left: 22.5%;
    }
  }
  &-item {
    position: absolute;
    width: 82%;
    left: 9%;
    height: 76%;
    z-index: 2;
    top: 10%;
    @media screen and (max-width: 500px) {
      top: 8%;
    }
  }
  &-wraper {
    width: 100%;
    background-color: transparent;
  }
  &-title {
    float: left;
    width: 30%;
    margin: 2rem 0 0 3rem;
    @media screen and (max-width: 767px) {
      width: 80%;
      margin-bottom: 0;
      & p {
        font-size: 0.8rem;
      }
    }
  }
}
</style>
<script>
export default {
  name: "myImage",
  data() {
    return {
      info:
        "我们致力于图片的修饰与美化，海报的创意制作与宣传单的设计，赋予复杂的就业数据美的特性并直观呈现，创意与美的结合，成就一场灵感的自由释放。",
      flag: 0,
      timeId: null
    };
  },
  created() {
    this.$nextTick(() => {
      this.autoplay();
    });
  },
  methods: {
    play() {
      if (this.flag == 2) this.flag = 0;
      else this.flag++;
    },
    autoplay() {
      if (!this.timeId) this.timeId = setInterval(this.play, 3000);
    },
    change(i) {
      this.stop();
      this.flag = i;
      setTimeout(this.autoplay, 2000);
    },
    stop() {
      if (this.timeId) {
        clearInterval(this.timeId);
        this.timeId = null;
      }
    }
  },
  computed: {
    screenWidth() {
      return this.$store.state.screenWidth;
    },
    images() {
      return this.$store.state.images;
    }
  }
};
</script>
