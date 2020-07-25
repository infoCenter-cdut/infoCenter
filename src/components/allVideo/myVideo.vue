<template>
  <div class="video-container">
    <div class="video-main">
      <div class="video-main-item" v-for="(item, index) in videoInfo" :key="index" v-show="!flag||index in searchShow">
        <div class="video-main-item-img">
          <img :src="item.vedio_img" alt="" width="100%">
        </div>
        <div class="video-main-item-title">
          <router-link :to="'/video/'+item.id">
            <h2>{{item.vedio_name}}</h2>
          </router-link>
          <a href="#">视频来源</a>：
          <a href="#">就业信息中心</a> -{{item.vedio_time|timeFormatter}}
        </div>
        <div></div>
      </div>
      <div class="video-btn">
        <div class="video-btn-left">
          <el-button @click="prevPage">
            <i class="fa fa-chevron-left"></i>
            <span v-if="video&&!video.previous">暂无</span>
          </el-button>
        </div>
        <div class="video-btn-right">
          <el-button @click="nextPage">
            <span v-if="video&&!video.next">暂无</span>
            <i class="fa fa-chevron-right"></i>
          </el-button>
        </div>
      </div>
    </div>
    <div class="video-aside">
      <div class="video-aside-search">
        <span class="pre-input">
          <i class="icon icon-search"></i>
        </span>
        <input type="text" v-model="searching" @keyup.enter="goSearch" placeholder="Search...">
      </div>
      <div class="video-aside-about">
        <h4>ABOUT THE BLOG</h4>
        <p>穿梭人群中，只为抓住精彩。瞬刻之间，图像之中，艺术与现实的结合，纪实感和形式感的体现。采集瞬间之美，留住永恒精彩。</p>
      </div>
      <div class="video-aside-magazine">
        <h4>杂志板块</h4>
        <a :href="mgUrl">
          <img :src="mgImg" alt="">
        </a>
        <p>{{mgTitle}}</p>
      </div>
    </div>
    <div style="padding:2rem"></div>
  </div>
</template>
<style lang="less" scoped src="./../../assets/less/myVideo.less">
</style>
<script>
export default {
  name: "myVideo",
  created() {//异步获取数据
    if (!this.video)
      this.$store.dispatch("getData", {
        url: "/allVedio",
        mutation: "setVideoInfo",
        callback: this.getVideo
      });
    else {
      this.getVideo();    
    }
    // console.log(this.video);
    // console.log('ccccccccccc');
    // if (!this.magazine) {
    //   this.$store.dispatch("getData", {
    //     url: "/allMagazine",
    //     mutation: "setMagazine",
    //     callback: this.getMagazine
    //   });
    // }
    if (this.search) {
      this.searchShow = [];
      this.videoInfo.forEach((x, i) => {
        if (x.vedio_name.indexOf(this.search) != -1) this.searchShow.push(i);
      });
      if (this.searchShow.length == 0) {
        this.open();
        this.flag = false;
      } else {
        this.flag = true;
      }
    } else this.flag = false;
  },
  mounted() {
    // if (this.magazine) this.getMagazine();
    if (this.video) this.getVideo();
    
  },
  data() {
    return {
      videoInfo: [],
      all: {},
      flag: true,
      searching: "",
      searchShow: [],
      mgUrl: "",
      mgTitle: "",
      mgImg: ""
    };
  },
  filters: {
    timeFormatter(data) {
      let time = new Date(data);
      let y = time.getFullYear();
      let m = time.getMonth() + 1;
      let d = time.getDate();
      return `${y}年${m}月${d}日`;
    }
  },
  methods: {
    getVideo() {
      this.all = this.video;
      (this.videoInfo = []),
        this.video.results.forEach(x => {
          this.videoInfo.push(x);
        });
    },
    // getMagazine() {
    //   this.mgUrl = this.magazine[0].magazine;
    //   this.mgImg = this.magazine[0].cover;
    //   this.mgTitle = this.magazine[0].title;
    // },
    goSearch() {
      this.$router.push({ path: "/allVideo/" + this.searching });
    },
    open() {
      const h = this.$createElement;

      this.$notify({
        title: "tips",
        message: h("i", { style: "color: teal" }, "无此项搜索结果哦"),
        duration: 1500
      });
    },
    prevPage() {
      //重新绑定页面数据
      if (this.video.previous) {
        this.$http.get(this.video.previous).then(res => {
          this.$store.commit("setVideoInfo", res.data);
          this.getVideo();
          // console.log(res.data);
        });
        //点击回到顶部
        document.body.scrollTop = document.documentElement.scrollTop = 1;
      }
     
    },
    nextPage() {
      if (this.video.next) {
        this.$http.get(this.video.next).then(res => {
          this.$store.commit("setVideoInfo", res.data);
          this.getVideo();
          // console.log(res.data);
        });
        document.body.scrollTop = document.documentElement.scrollTop = 1;
      }
    }
  },
  computed: {
    video() {
      return this.$store.state.videoInfo;
    },
    magazine() {
      return this.$store.state.magazine;
    },
    search() {
      return this.$route.params.search;
    }
  },
  watch: {
    search() {
      if (this.search) {
        this.searchShow = [];
        this.videoInfo.forEach((x, i) => {
          if (x.vedio_name.indexOf(this.search) != -1) this.searchShow.push(i);
          // console.log(x.vedio_name, this.search);
        });
        if (this.searchShow.length == 0) {
          this.flag = false;
          this.open();
        } else {
          this.flag = true;
        }
      } else this.flag = false;
    }
  }
};
</script>
