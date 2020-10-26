<template>
  <div class="video-container">
    <my-slide :height="$store.state.screenWidth>767?82:62" :imgType="2" :bannerImg="bannerImg"></my-slide>
    <myVideoDisplay :next="nextId" :prev="prevId" :nowVideo="nowVideo"></myVideoDisplay>
  </div>
</template>
<style lang="less" scoped>
.video {
  &-container {
    position: relative;
    width: 100%;
  }
}
</style>
<script>
import mySlide from "./../components/subCom/mySlide.vue";
import myVideoDisplay from "./../components/video/myVideoDisplay.vue";
export default {
  name: "myVideo",
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
      ],
      nowIndex: -1,
      nowVideo: {},
      nextId: -1,
      prevId: -1,
    };
  },
  created() {
    // console.log(this.videoInfo);
    if (this.videoInfo) this.getVideo();
    
    
  },
  methods: {
     getVideo() {
      let arr = this.videoInfo.results;
      // console.log(arr);
      
      this.nowVideo = arr.filter(x => x.id != this.nowId);
      arr.forEach((x, i) => {
        if (x.id == this.nowId) {         
          this.nowIndex = i;
          this.nowVideo = x;          
        }
      });
      if (this.nowIndex == 0) this.prevId = -1;
      else this.prevId = arr[this.nowIndex - 1].id;
      if (this.nowIndex == arr.length - 1) this.nextId = -1;
      else this.nextId = arr[this.nowIndex + 1].id;


    }
  },
  components: {
    mySlide,
    myVideoDisplay
  },
  computed: {
    nowId() {
      return parseInt(this.$route.params.id);
    },
    videoInfo() {
      return this.$store.state.videoInfo;
    },
  },
  watch: {
    nowId() {}
  }
};
</script>
