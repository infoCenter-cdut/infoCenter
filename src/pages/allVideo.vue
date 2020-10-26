<template>
  <div class="video-container">
    <my-slide :height="$store.state.screenWidth>767?82:62" :imgType="2" :bannerImg="bannerImg"></my-slide>
    <my-video></my-video>
  </div>
</template>
<style lang="less" scoped>
</style>
<script>
import mySlide from "./../components/subCom/mySlide.vue";
import myVideo from "./../components/allVideo/myVideo";
export default {
  name: "allVideo",
  data() {
    return {
      bannerImg: [
        {
          passage_img: require("./../assets/career/img/news/摄影.jpg"),
          first: "Materials collecting Department",
          second: "记录现场事实,捕捉精彩瞬间，带来艺术享受是我们的最终目标"
        },
        {
          passage_img: require("./../assets/career/img/news/摄影2.jpeg"),
          first: "Materials collecting Department",
          second: "记录现场事实,捕捉精彩瞬间，带来艺术享受是我们的最终目标"
        }
      ]
    };
  },
  components: {
    mySlide,
    myVideo
  }
};
</script>
