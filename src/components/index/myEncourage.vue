<template>
    <div class="swiper-container">
        <div class="swiper-wrapper">
            <div class="swiper-slide" v-for="(item, index) in enInfo" :key="index">
                <p class="centertxt content white">{{item.content}}</p>
                <div class="author centertxt white">-{{item.author}}-</div>
            </div>
        </div>
        <div class="swiper-pagination swiper-pagination-white"></div>
    </div>
</template>
<style lang="less" scoped>
.swiper-container {
  width: 100%;
  position: relative;
  background-color: #4fc1e9;
  .content {
    font-style: italic;
    font-size: 1.4rem;
  }
  .author {
    font-style: italic;
    font-size: 1rem;
    opacity: 0.7;
  }
  .swiper-slide {
    margin: 4rem 0;
  }
}
</style>
<script>
import "swiper/dist/css/swiper.css";
import Swiper from "swiper";
export default {
  name: "myEncourage",
  props: {
    enInfo: {
      type: Array,
      required: true
    }
  },
  mounted() {
    new Swiper(".swiper-container", {//swiper轮播组件配置
      loop: true,
      pagination: {
        el: ".swiper-pagination",
        clickable: true
      },
      autoplay: {
        delay: 2000
      },
      effect: "slide",
      fadeEffect: {
        // crossFade: true
      }
    });
  },
  data() {
    return {};
  }
};
</script>
