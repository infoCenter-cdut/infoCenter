<template>
  <div class="slide-container" @mouseover="stop" @mouseout="play" @touchstart="touchStart" @touchmove="touchMove" @touchend="touchEnd" :style="{'height':_height}">
    <div class="slide-item" v-for="(item, index) in bannerImg" :key="index" :style="{'height':_height}">
      <transition appear mode="out-in" enter-active-class="myAniIn" leave-active-class="myAniOut">
        <div class="slide-item-img" v-show="imgType==1&&flag==index" ref="img">
          <img :src="item.passage_img" width="100%">
        </div>
      </transition>
      <transition appear mode="out-in" enter-active-class="myAniIn" leave-active-class="myAniOut">
        <div class="slide-item-imgTwo" ref="img2" v-show="imgType==2&&flag==index" :style="{'background-image':'url('+item.passage_img+')'}">
        </div>
      </transition>
      <div v-show="(item.title)&&index==flag" class="slide-item-title" :style="{'margin-top':marginTop}">
        <h1 class="white myAniTitleIn" v-if="$store.state.screenWidth>767">{{item.title}}</h1>
        <h3 class="white myAniTitleIn" v-else>{{item.title}}</h3>
        <el-button @click="$router.push('/news/'+item.id)">
          READ MORE
        </el-button>
      </div>
      <div v-if="item.first&&index==flag" class="slide-item-other">
        <h3 class="slide-item-first white animated zoomIn">{{item.first}}</h3>
        <span class="white animated fadeIn">{{item.second}}</span>
      </div>
      <transition appear enter-active-class="myAniSourceIn">
        <div class="slide-item-from centertxt hidden-xs" v-if="item.source&&index==flag">
          文章来源：
          <span>{{item.source}}</span>
        </div>
      </transition>
    </div>
    <div class="slide-pagination" v-if="bannerImg&&bannerImg.length>1" :style="{'margin-left':-(bannerImg.length*0.9)+'rem',}">
      <span @click="change(null,index)" v-for="(item, index) in bannerImg" :key="index" class="slide-pagination-item" :class="{'slide-pagination-item-active':index==flag}"></span>
    </div>
    <div class="slide-navigation hidden-xs" v-if="bannerImg.length>1">
      <i class="icon icon-arrow-left-simple" @click="preOne"></i>
      <i class="icon icon-arrow-right-simple" @click="nextOne"></i>
    </div>
  </div>
</template>
<script>
export default {
  name: "mySlide",
  props: {//轮播配置
    bannerImg: {
      type: Array,
      default: []
    },
    height: {
      type: [Number],
      default: 100
    },
    imgType: {
      type: Number,
      default: 1
    }
  },
  created() {
    if (this.screenWidth < 1400)
      this.marginTop = -5 * 1400 / this.screenWidth + "rem";
    let nowHeight = this.height / 100 * this.$store.state.screenHeight;
    // console.log(nowHeight);
    this.$store.commit("setBannerHeight", nowHeight);
  },
  mounted() {
    this.play();
  },
  data() {
    return {
      flag: 0,
      timeId: null,
      marginTop: 0,
      sx: "",
      tx: ""
    };
  },
  methods: {
    play() {
      if (!this.timeId) this.timeId = setInterval(this.autoPlay, 3000);
    },
    autoPlay() {
      this.flag = this.flag == this.bannerImg.length - 1 ? 0 : this.flag + 1;
    },
    change(e, i) {
      if (!e) {
        this.stop();
        this.flag = i;
      }
    },
    stop() {
      clearInterval(this.timeId);
      this.timeId = null;
    },
    getNext() {
      if (this.flag == this.bannerImg.length - 1) return this.flag;
      return this.flag + 1;
    },
    getPre() {
      if (this.flag == 0) return this.flag;
      return this.flag - 1;
    },
    touchStart(e) {//移动端滑动开始事件
      this.sx = e.touches[0].pageX;
      // console.log(this.sx);
      this.stop();
    },
    touchMove(e) {//移动端滑动事件，进行图片切换位移
      if (this.imgType == 1) {
        let nx = e.touches[0].pageX;
        this.$refs.img[this.flag].style =
          "transform:translateX(" + (nx - this.sx) + "px)";
        if (nx > this.sx) {
          if (this.getPre() != this.flag) {
            this.$refs.img[this.getPre()].style =
              "transform:translateX(" +
              (nx - this.sx - this.screenWidth) +
              "px";
            // console.log(this.getPre());
          }
        } else if (nx < this.sx) {
          if (this.getNext() != this.flag)
            this.$refs.img[this.getNext()].style =
              "transform:translateX(" +
              (this.screenWidth + nx - this.sx) +
              "px";
        }
      } else {
        let nx = e.touches[0].pageX;
        this.$refs.img2[this.flag].style =
          this.nowImg + ";transform:translateX(" + (nx - this.sx) + "px)";
        if (nx > this.sx) {
          if (this.getPre() != this.flag) {
            this.$refs.img2[this.getPre()].style =
              this.preImg +
              ";transform:translateX(" +
              (nx - this.sx - this.screenWidth) +
              "px";
            // console.log(this.getPre());
          }
        } else if (nx < this.sx) {
          if (this.getNext() != this.flag)
            this.$refs.img2[this.getNext()].style =
              this.nextImg +
              ";transform:translateX(" +
              (this.screenWidth + nx - this.sx) +
              "px";
        }
      }
    },
    touchEnd(e) {//
      if (this.imgType == 1) {
        this.tx = e.changedTouches[0].pageX;
        if (this.tx > this.sx) {
          this.$refs.img[this.flag].style = this.$refs.img[
            this.getPre()
          ].style =
            "";
          this.flag = this.getPre();
        } else if (this.tx < this.sx) {
          this.$refs.img[this.flag].style = this.$refs.img[
            this.getNext()
          ].style =
            "";

          this.flag = this.getNext();
        }
      } else {
        this.tx = e.changedTouches[0].pageX;
        if (this.tx > this.sx) {
          this.$refs.img2[this.flag].style = this.nowImg;
          this.$refs.img2[this.getPre()].style = this.preImg;
          this.flag = this.getPre();
        } else if (this.tx < this.sx) {
          this.$refs.img2[this.flag].style = this.nowImg;
          this.$refs.img2[this.getNext()].style = this.nextImg;
          this.flag = this.getNext();
        }
      }
    },
    preOne() {
      if (this.timeId) this.stop();
      this.flag =
        (this.flag + this.bannerImg.length - 1) % this.bannerImg.length;
    },
    nextOne() {
      if (this.timeId) this.stop();
      this.flag =
        (this.flag + this.bannerImg.length + 1) % this.bannerImg.length;
    }
  },
  computed: {
    _height() {//组件高度
      if (typeof this.height == "number") return this.height + "vh";
      return this.height;
    },
    screenWidth: {
      get() {
        return this.$store.state.screenWidth;
      },
      set() {}
    },
    nowImg() {
      return (
        "background-image:url(" + this.bannerImg[this.flag].passage_img + ")"
      );
    },
    preImg() {
      return (
        "background-image:url(" +
        this.bannerImg[this.getPre()].passage_img +
        ")"
      );
    },
    nextImg() {
      return (
        "background-image:url(" +
        this.bannerImg[this.getNext()].passage_img +
        ")"
      );
    }
  },
  watch: {
    screenWidth() {
      if (this.screenWidth < 1400)
        this.marginTop = -5 * 1400 / this.screenWidth + "rem";
    }
  }
};
</script>
<style scoped src="./../../assets/css/mySlide.css">

</style>
<style lang="less" scoped src="./../../assets/less/mySlide.less">
</style>
