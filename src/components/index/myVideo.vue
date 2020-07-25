<template>
  <div class="video-container">
    <div class="video-wraper">
      <transition-group mode="out-in" appear enter-active-class="animated fadeIn" leave-active-class="animated fadeOut">
        <div class="video-item" v-for="(item, index) in video" :key="item.vedio_img" v-show="index==flag">
          <router-link :to="'/video/'+item.id">
            <img v-lazy="item.vedio_img" alt="" srcset="" width="100%">
          </router-link>
        </div>
      </transition-group>
      <div class="video-pagination" v-if="video&&video.length">
        <div class="video-pagination-left">
          <i class="fa fa-chevron-left" @click="pre"></i>
        </div>
        <div class="video-pagination-right">
          <i class="fa fa-chevron-right" @click="next"></i>
        </div>
      </div>
    </div>
    <div class="video-button">
      <el-button @click="$router.push('/allVideo')">点击进入视频专区</el-button>
    </div>
  </div>
</template>
<style lang="less" scoped>
.fa {
  color: #ccc;
  transition: color 0.5s ease;
  transform: scale(3);
  &:hover {
    color: #fff;
    transition: color 0.5s ease;
    cursor: pointer;
  }
}
.video {
  &-container {
    width: 100%;
    height: 130vh;
    @media screen and (max-width: 767px) {
      height: 70vh;
    }
    position: relative;
    background-color: #434a54;
    overflow: hidden;
  }
  .center(@w,@h) {
    position: relative;
    width: @w;
    height: @h;
    left: 50%;
    margin-left: -0.5 * @w;
  }
  &-pagination {
    position: absolute;
    height: 2rem;
    width: 100%;
    top: 40%;
    z-index: 2;
    margin-top: -1rem;
    &-left {
      float: left;
      clear: none;
    }
    &-right {
      float: right;
      clear: none;
    }
  }
  &-wraper {
    .center(50rem,35rem);
    top: 3rem;
    @media screen and (max-width: 840px) {
      transform: scale(0.5);
      top: -5rem;
    }
    @media screen and (max-width: 400px) {
      transform: scale(0.4);
      top: -5rem;
    }
    background: url("./../../assets/career/img/mockups/desktop.svg") no-repeat;
    background-position: center center;
  }
  &-item {
    position: absolute;
    width: 84%;
    height: 66%;
    top: 7%;
    left: 8%;
    z-index: 3;
    overflow: hidden;
  }
  &-button {
    position: relative;
    width: 10rem;
    left: 50%;
    margin-left: -5rem;
    bottom: -10rem;
    @media screen and (max-width: 840px) {
      bottom: 10rem;
    }
  }
}
</style>
<script>
import Swiper from "swiper";
export default {
  name: "myVideo",
  components: {},
  data() {
    return {
      video: [],
      flag: 0,
      timeId: null
    };
  },
  methods: {
    getVideo() {
      this.videoInfo.results.forEach(element => {
        this.video.push(element);
      });
    },
    play() {
      if (this.flag == this.video.length - 1) this.flag = 0;
      else this.flag++;
    },
    autoplay() {
      if (!this.timeId) this.timeId = setInterval(this.play, 3000);
    },
    stop() {
      if (this.timeId) {
        clearInterval(this.timeId);
        this.timeId = null;
        setTimeout(() => {
          this.autoplay();
        }, 2000);
      }
    },
    pre() {
      this.stop();
      if (this.flag == 0) this.flag = this.video.length - 1;
      else this.flag--;
    },
    next() {
      this.stop();
      if (this.flag == this.video.length - 1) this.flag = 0;
      else this.flag++;
    }
  },
  created() {
    if (!this.videoInfo)
      this.$store.dispatch("getData", {
        url: "/allVedio",
        mutation: "setVideoInfo",
        callback: this.getVideo
      });
    else this.getVideo();
  },
  mounted() {
    this.autoplay();
  },
  computed: {
    videoInfo() {
      return this.$store.state.videoInfo;
    }
  }
};
</script>
