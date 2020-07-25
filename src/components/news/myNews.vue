<template>
  <div class="news-container">
    <div class="news-top">
      <div class="news-back">
        <router-link to="/allNews">
          <i class="icon icon-images"></i>
        </router-link>
      </div>
      <div class="news-prev">
        <router-link :to="'/news/'+prev" v-if="prev!=-1">
          <i class="fa fa-chevron-left"></i>
        </router-link>
        <span v-else>--</span>
      </div>
      <div class="news-next">
        <router-link :to="'/news/'+next" v-if="next!=-1">
          <i class="fa fa-chevron-right"></i>
        </router-link>
        <span v-else>--</span>
      </div>
    </div>
    <div class="news-info animated" :class="{'fadeIn':update}">
      <a href="#">文章类型</a>：{{nowNew.Type}}- {{nowNew.passage_time|timeFormatter}}
    </div>
    <div class="news-title animated" :class="{'flipInX':update}">
      <h1 v-if="screenWidth>767">{{nowNew.title}}</h1>
      <h3 v-else>{{nowNew.title}}</h3>
    </div>
    <div class="news-img animated" :class="{'fadeIn':update}">
      <img :src="nowNew.passage_img" alt="" style="margin:0 auto;">
    </div>
    <div class="news-content animated" :class="{'fadeIn':update}">
      <div v-for="(item,i) in contentSlice" :key="i">
        <p v-text="item"></p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "myNews",
  created() {
    // console.log(this.nowNew);
    
    this.getContent();
  },
  data() {
    return {
      content: "",
      contentSlice: [],
      update: true
    };
  },
  methods: {
    getContent() {//异步更新update,实现动画效果
      this.update = false;
      setTimeout(() => {
      
        // $.ajax({
        //   async: true,
        //   url: this.nowNew.content,
        //   contentType: "text/json,charset=utf-8",
        //   scriptCharset: "gb2312",
        //   dataType: 'jsonp',  
        //   crossDomain: true,
        //   success: result => {
        //     this.content = result;
        //     this.contentSlice = this.content.split(/\s\s+/g);
        //     console.log(result);
        //   }
        // });

        //获取新闻文章内容，filename.slice(21)是/media/newspassage/+文章名
        this.$http.get('http://www.cdutzy.com'+this.nowNew.content.slice(21)).then(res=>{
          // console.log(res);
          this.content = res.data;
          this.contentSlice = this.content.split(/\s\s+/g);
          // console.log(this.content);
          
        },fail=>{
          console.log(fail);
        })

        this.update = true;
      }, 0);//将此匿名函数重新放入事件队列末尾
    }
  },
  filters: {
    timeFormatter(data) {//时间格式化过滤器
      let time = new Date(data);
      let y = time.getFullYear();
      let m = time.getMonth() + 1;
      let d = time.getDate();
      let h = time.getHours();
      let min = time.getMinutes();
      return (
        `${y}年${m}月${d}日` +
        h.toString().padStart(2, 0) +
        ":" +
        min.toString().padStart(2, 0)
      );
    }
  },
  props: {
    next: {
      type: Number,
      default: -1
    },
    prev: {
      type: Number,
      default: -1
    },
    nowNew: {
      type: Object,
      required: true
    }
  },
  computed: {
    nowId() {
      return this.$route.params.id;
    },
    screenWidth() {
      return this.$store.state.screenWidth;
    }
  },
  watch: {
    nowId() {//路由发生变化时重新获取数据
      this.getContent();
    }
  }
};
</script>

<style lang="less" scoped>
.news-container {
  width: 70%;
  margin: 0.5rem 15% 2rem;
  
  .news-info {
    .normol() {
      margin: 0;
      color: #ccc;
      font-weight: 400;
      font-size: 0.8rem;
    }
    .normol();
    a {
      .normol();
      &:hover {
        color: #fd685b;
      }
    }
  }
  .news-title {
    text-align: center;
    h1 {
      margin-top: 0.5rem;     
      font-size: 2.5rem;
    }
    h3 {
      margin-top: 0.5rem;
    }
  }
  .news-img {
    width: 100%;
  }
  .news-content {
    margin: 2rem 0 5rem;
  }
}
.news-top {
  position: relative;
  border-bottom: 1px solid #ccc;
  height: 5rem;
  .news-back {
    position: absolute;
    left: 50%;
    transform: scale(0.7);
    margin-left: -14px;
    .icon-images {
      color: #ccc;
      &:hover {
        color: #fd685b;
      }
    }
  }
  .news-prev {
    position: absolute;
    top: 1.5rem;
    .fa-chevron-left {
      color: #ccc;
      &:hover {
        color: #fd685b;
      }
    }
  }
  .news-next {
    .news-prev();
    .fa-chevron-right {
      color: #ccc;
      &:hover {
        color: #fd685b;
      }
    }
    right: 0;
  }
}
</style>
