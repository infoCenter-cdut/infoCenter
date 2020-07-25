<template>
  <div class="video-container">
    <div class="video-top">
      <div class="video-top-back">
        <router-link to="/allVideo">
          <i class="icon icon-images"></i>
        </router-link>
      </div>
      <div class="video-top-prev">
        <router-link :to="'/video/'+prev" v-if="prev!=-1">
          <i class="fa fa-chevron-left"></i>
        </router-link>
        <span v-else>--</span>
      </div>
      <div class="video-top-next">
        <router-link :to="'/video/'+next" v-if="next!=-1">
          <i class="fa fa-chevron-right"></i>
        </router-link>
        <span v-else>--</span>
      </div>
    </div>
    <div class="video-item-title">
      <a href="#">视频来源</a>：
      <a href="#">就业信息中心</a>
      -{{nowVideo.vedio_time|timeFormatter}}
    </div>
    <div class="video-title">
      <h2>{{nowVideo.vedio_name}}</h2>
    </div>
    <!-- <div id="youkuplayer" style="width:480px;height:400px"></div> -->
    <div class="video-box">
      <video-player class="video-player vjs-custom-skin" ref="videoPlayer" :playsinline="true" :options="playerOptions" data-setup='{ "techOrder": ["flash"] }'></video-player>
    </div>
    <div></div>
    <div class="video-news">
      <h4>热点咨询</h4>
      <div v-for="(item, index) in allNews" :key="index" class="video-news-img">
        <router-link :to="'/news/'+item.id">
          <img :src="item.passage_img" alt srcset>
        </router-link>
      </div>
    </div>
  </div>
</template>
<style lang="less" scoped>
.video {
  &-container {
    width: 100%;
    position: relative;
    margin-top: 3rem;
  }

  &-box {
    position: relative;
    width: 70%;
    left: 15%;
  }

  &-title {
    text-align: center;
  }

  &-news {
    position: relative;
    width: 70%;
    left: 15%;
    margin-bottom: 3rem;

    &-img {
      width: 33%;
      border: 1px solid white;
      border-radius: 2rem;
      overflow: hidden;
      display: inline-block;
    }
  }

  &-item-title {
    width: 70%;
    left: 15%;
    position: relative;
    margin-top: 2rem;
    color: #ccc;
    font-size: 0.9rem;

    a {
      color: #ccc;
      transition: color 0.5s ease;

      &:hover {
        color: #fd685b;
        transition: color 0.5s ease;
      }
    }
  }

  &-top {
    position: relative;
    border-bottom: 1px solid #ccc;
    height: 3rem;
    width: 70%;
    left: 15%;

    .icon,
    .fa {
      color: #ccc;
      transition: color 0.5s ease;

      &:hover {
        color: #fd685b;
        transition: color 0.5s ease;
      }
    }

    &-back {
      text-align: center;
      position: absolute;
      width: 5rem;
      left: 50%;
      margin-left: -2.5rem;
      margin-top: -1rem;
    }

    &-prev {
      float: left;
    }

    &-next {
      float: right;
      clear: none;
    }
  }
}
</style>
<script type="text/javascript" src="//player.youku.com/jsapi"></script>
<script>
export default {
  name: "myVideoDisplay",
  props: {
    next: {
      type: Number,
      default: -1
    },
    prev: {
      type: Number,
      default: -1
    },
    nowVideo: {
      type: Object,
      required: true
    }
  },
  created() {
    // console.log(this.nowVideo);
    // console.log(this.next);
    if (!this.news)
      this.$store.dispatch("getData", {
        url: "/allNews",
        mutation: "setNowPage",
        callback: this.getNews
      });
    else this.getNews();
    
  },
  methods: {
    getNews() {    
      this.news.forEach((element, i) => {
        if (i < 3) this.allNews.push(element);
      
      });
    }
  },
  data() {
    return {
      playerOptions: {//视频播放插件配置
        playbackRates: [0.7, 1.0, 1.5, 2.0], //播放速度
        autoplay: false, //如果true,浏览器准备好时开始回放。
        muted: false, // 默认情况下将会消除任何音频。
        loop: false, // 导致视频一结束就重新开始。
        preload: "auto", // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
        language: "zh-CN",
        aspectRatio: "16:9", // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
        fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
        sources: [{
          type: "",
          src: "https://v.youku.com/v_show/id_"+this.nowVideo.vedio_url+".html" //视频url地址
        }],
        poster: this.nowVideo.vedio_img, //你的封面地址
        notSupportedMessage: "此视频暂无法播放，请稍后再试", //允许覆盖Video.js无法播放媒体源时显示的默认信息。
        controlBar: {
          timeDivider: true,
          durationDisplay: true,
          remainingTimeDisplay: false,
          fullscreenToggle: true //全屏按钮
        }
      },
      allNews: [],
      // player: new YKU.Player('youkuplayer',{
      //         styleid: '0',
      //         client_id: 'bba75f02eb5c8131',
      //         vid: "https://v.youku.com/v_show/id_"+this.nowVideo.vedio_url+".html",
      //         newPlayer: true
      //         })
    };
  },
  computed: {
    nowId() {
      return this.$route.params.id;
    },
    news() {
      return this.$store.state.bannerImg;
    },
  
  },
  watch: {
    nowId(){
      this.playerOptions.poster=this.nowVideo.vedio_img;
      this.playerOptions.sources[0].src=this.nowVideo.vedio_url;
    }
  },
  filters: {
    timeFormatter(data) {
      let time = new Date(data);
      let y = time.getFullYear();
      let m = time.getMonth() + 1;
      let d = time.getDate();
      return `${y}年${m}月${d}日`;
    }
  }
};

</script>

                                
