<template>
  <div class="real-time-info">
    <div class="real-time-main float">
      <h4 class="real-time-main-text">微关注</h4>
      <div class="real-time-img">
        <el-row :gutter="5">
          <el-col :span="span" v-for="(x) in nowShow" :key="x.passage_img+1" class="float">
            <div class="grid-content bg-purple float img">
              <img :src="x.passage_img" alt="" width="100%" @click="$router.push({path:'/news/'+x.id})">
              <div class="real-time-bg">
                <i class="icon icon-doc white"></i>
              </div>
            </div>
            <h5 class="real-time-type">文章类型：{{x.Type}}</h5>
            <h4 class="real-time-title float">{{x.title}}</h4>
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="real-time-btn">
      <el-button type="primary" plain @click="$router.push('/allNews')">
        点击进入新闻专区
      </el-button>
    </div>
  </div>
</template>
<style lang="less" scoped>
.img{
  position: relative;
  border-radius: 2rem;
  overflow: hidden;
  &:hover .real-time-bg{
    opacity: 1;
    transition: opacity 1s ease;
  }
  &:hover{
    cursor: pointer;
  }
}
  .icon{
    margin-top: 25%;
  }
  .white {
    color: white;
  }

  .float {
    clear: none !important;
  }

  .real-time {
    &-info {
      width: 100%;
      background-color: #fff;
      position: relative;
      margin-top: 1rem;
    }
    &-bg{
      position: absolute;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(96,197,234,.9);
      opacity: 0;
      pointer-events: none;
      transition: opacity 1s ease;
    }
    &-type{
      color: #ccc;
    }
    &-img {
      padding-top: 5rem;
    }

    &-btn {
      position: relative;
      width: 10rem;
      left: 50%;
      margin-left: -5rem;
      margin-bottom: 10rem;
      bottom: -8rem;

      & a:hover {
        color: black;
      }
    }

      &-main {
        width: 80%;
        margin-left: 10%;
        text-align: center;

        &-text {
          .real-time-center(4rem);
          border-bottom: 2px solid rgba(0, 0, 0, 0.1);
        }
      }
    }

    .real-time-center(@w) {
      position: absolute;
      width: @w;
      left: 50%;
      @now: -@w*0.5;
      margin-left: @now;
    }

</style>
<script>
  import Waterfall from 'vue-waterfall/lib/waterfall'
  import WaterfallSlot from 'vue-waterfall/lib/waterfall-slot'
  export default {
    name: "myRealTime",
    created() {
      if (!this.passage)
        setTimeout(this.getImg, 2000);
      else
        this.getImg();
      if (this.screenWidth < 767)
        this.span = 24;
      else
        this.span = 6;
    },
    methods: {
      async getImg() {
        await this.passage.forEach((x, i) => {
          let nowImg = new Image();
          nowImg.src = x.passage_img;
          x.width = nowImg.width;
          x.height = nowImg.height;
          this.all.push(x);
        });
        this.nowShow = this.all.slice(0, 8);
        console.log(this.nowShow);
        
        this.$previewRefresh(); //图片异步加载需要执行此函数才能正常使用预览！！！
      },
    },
    data() {
      return {
        gap: 300,
        all: [],
        nowShow: [],
        span: 6,
      };
    },
    components: {
      Waterfall,
      WaterfallSlot,
    },
    computed: {
      passage() {
        return this.$store.state.bannerImg;
      },
      screenWidth() {
        return this.$store.state.screenWidth;
      }
    }
  };

</script>
