<template>
  <div class="img-container">
    <mySlide :bannerImg="img" :imgType="2" :height="$store.state.screenWidth>767?82:62"></mySlide>
    <div class="img-nav">
      <el-tabs v-model="now" @tab-click="page=0" :stretch="true">
        <el-tab-pane label="全部图片" name="全部图片">
          <el-row :gutter="5" class="float">
            <el-col :span="span" v-for="(x) in nowShow" :key="x.img_url+1" class="float">
              <div class="grid-content bg-purple float img animated zoomIn">
                <img v-lazy="x.img_url" alt="" :preview="1" :preview-text="x.img_auth+' '+x.img_name">
                <div class="img-bg">
                  <i class="icon icon-search"></i>
                  <p class="centertxt small">{{x.img_name}}</p>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-tab-pane>
        <el-tab-pane name="LOGO" label="LOGO">
          <el-row :gutter="5" class="float">
            <el-col :span="span" v-for="(x) in nowShow" :key="x.img_url+1" class="float">
              <div class="grid-content bg-purple float img animated zoomIn">
                <img v-lazy="x.img_url" alt="" :preview="2" :preview-text="x.img_auth+' '+x.img_name">
                <div class="img-bg float">
                  <i class="icon icon-search"></i>
                  <p class="centertxt small">{{x.img_name}}</p>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-tab-pane>
        <el-tab-pane label="办公类" name="办公类">
          <el-row :gutter="5" class="float">
            <el-col :span="span" v-for="(x) in nowShow" :key="x.img_url+1" class="float">
              <div class="grid-content bg-purple float img animated zoomIn">
                <img v-lazy="x.img_url" alt="" :preview="3" :preview-text="x.img_auth+' '+x.img_name">
                <div class="img-bg float">
                  <i class="icon icon-search"></i>
                  <p class="centertxt small">{{x.img_name}}</p>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-tab-pane>
        <el-tab-pane label="宣传类" name="宣传类">
         <el-row :gutter="5" class="float">
            <el-col :span="span" v-for="(x) in nowShow" :key="x.img_url+1" class="float">
              <div class="grid-content bg-purple float img animated zoomIn">
                <img v-lazy="x.img_url" alt="" :preview="4" :preview-text="x.img_auth+' '+x.img_name">
                <div class="img-bg float">
                  <i class="icon icon-search"></i>
                  <p class="centertxt small">{{x.img_name}}</p>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-tab-pane>
        <el-tab-pane label="展示类" name="展示类">
          <el-row :gutter="5" class="float">
            <el-col :span="span" v-for="(x) in nowShow" :key="x.img_url+1" class="float">
              <div class="grid-content bg-purple float img animated zoomIn">
                <img v-lazy="x.img_url" alt="" :preview="5" :preview-text="x.img_auth+' '+x.img_name">
                <div class="img-bg">
                  <i class="icon icon-search"></i>
                  <p class="centertxt small">{{x.img_name}}</p>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-tab-pane>
        <el-tab-pane label="工作类" name="工作类">
          <el-row :gutter="5" class="float">
            <el-col :span="span" v-for="(x) in nowShow" :key="x.img_url+1" class="float">
              <div class="grid-content bg-purple float img animated zoomIn">
                <img v-lazy="x.img_url" alt="" :preview="6" :preview-text="x.img_auth+' '+x.img_name">
                <div class="img-bg">
                  <i class="icon icon-search"></i>
                  <p class="centertxt small">{{x.img_name}}</p>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-tab-pane>
      </el-tabs>
      <div class="img-btn">
        <el-button class="img-btn-left" @click="page--" :disabled="!pre">
          <i class="fa fa-chevron-left"></i>
        </el-button>
        <el-button class="img-btn-right" @click="page++" :disabled="!next">
          <i class="fa fa-chevron-right"></i>
        </el-button>
      </div>
    </div>
  </div>
</template>
<style lang="less" scoped src="./../assets/less/imgDisplay.less">
</style>
<script>
  import mySlide from "./../components/subCom/mySlide.vue";
  import Waterfall from 'vue-waterfall/lib/waterfall'
  import WaterfallSlot from 'vue-waterfall/lib/waterfall-slot'
  import {
    Spin
  } from "iview";
  export default {
    //图片懒加载
    name: "imgDisplay",
    data() {
      return {
        activeName: "全部图片",
        img: [{
            passage_img: require("./../assets/career/img/dmImg/dmbg1.jpg"),
            first: "Art Designing Department",
            second: "创意与美的结合，成就一场灵感的自由释放"
          },
          {
            passage_img: require("./../assets/career/img/dmImg/dmbg2.jpg"),
            first: "Art Designing Department",
            second: "创意与美的结合，成就一场灵感的自由释放"
          },
          {
            passage_img: require("./../assets/career/img/dmImg/dmbg3.jpg"),
            first: "Art Designing Department",
            second: "创意与美的结合，成就一场灵感的自由释放"
          },
          {
            passage_img: require("./../assets/career/img/dmImg/dmbg4.jpg"),
            first: "Art Designing Department",
            second: "创意与美的结合，成就一场灵感的自由释放"
          }
        ],
        all: [],
        logo: [],
        officeDec: [],
        propagate: [],
        display: [],
        work: [],
        now: '全部图片',
        page: 0,
        nowShow: [],
        next: null,
        pre: null,
        pageSize: 10,
        gap: 500,
        span:12,
      };
    },
    created() {
      if (!this.images) {
        this.$store.dispatch("getData", {
          url: "/allImages",
          mutation: "setImages",
          callback: this.getImg
        });
      } else {
        this.getImg();
      }
      if (this.screenWidth < 767){
        this.gap = 300;
        this.span=24;
      }
    },
    mounted() {},
    methods: {
      async getImg() {
        await this.images.forEach((x, i) => {
          let nowImg = new Image();
          nowImg.src = x.img_url;
          x.width = nowImg.width;
          x.height = nowImg.height;
          this.all.push(x);
          if (x.img_type == "LOGO") this.logo.push(x);
          else if (x.img_type == "办公室美华") {
            this.officeDec.push(x);
          } else if (x.img_type == "宣传类") {
            this.propagate.push(x);
          } else if (x.img_type == "展示类") {
            this.display.push(x);
          } else this.work.push(x);
        });
        // this.$Spin.hide();
        if (this.all.length > this.pageSize) {
          this.nowShow = this.all.slice(0, this.pageSize);
          this.next = 1;
        } else {
          this.nowShow = this.all;
        }
        this.$previewRefresh(); //图片异步加载需要执行此函数才能正常使用预览！！！
      },
      rePut() {
        if (this.page == 0)
          this.pre = 0;
        else
          this.pre = 1;
        if (this.now == "全部图片") {
          this.nowShow = this.all.slice(this.pageSize * this.page, this.pageSize * this.page + this.pageSize);
          if (this.page * this.pageSize + this.pageSize <= this.all.length) {
            this.next = 1;
          } else {
            this.next = 0;
          }
        } else if (this.now == "LOGO") {
          this.nowShow = this.logo.slice(this.pageSize * this.page, this.pageSize * this.page + this.pageSize);
          if (this.page * this.pageSize + this.pageSize <= this.logo.length) {
            this.next = 1;
          } else {
            this.next = 0;
          }
        } else if (this.now == "办公类") {
          this.nowShow = this.officeDec.slice(this.pageSize * this.page, this.pageSize * this.page + this.pageSize);
          if (this.page * this.pageSize + this.pageSize <= this.officeDec.length) {
            this.next = 1;
          } else {
            this.next = 0;
          }
        } else if (this.now == "宣传类") {
          this.nowShow = this.propagate.slice(this.pageSize * this.page, this.pageSize * this.page + this.pageSize);
          if (this.page * this.pageSize + this.pageSize <= this.propagate.length) {
            this.next = 1;
          } else {
            this.next = 0;
          }
        } else if (this.now == "展示类") {
          this.nowShow = this.display.slice(this.pageSize * this.page, this.pageSize * this.page + this.pageSize);
          if (this.page * this.pageSize + this.pageSize <= this.display.length) {
            this.next = 1;
          } else {
            this.next = 0;
          }
        } else if (this.now == "工作类") {
          this.nowShow = this.work.slice(this.pageSize * this.page, this.pageSize * this.page + this.pageSize);
          if (this.page * this.pageSize + this.pageSize <= this.work.length) {
            this.next = 1;
          } else {
            this.next = 0;
          }
        }
      }
    },
    components: {
      mySlide,
      Waterfall,
      WaterfallSlot,
      Spin,
    },
    computed: {
      images() {
        return this.$store.state.images;
      },
      screenWidth() {
        return this.$store.state.screenWidth;
      },
    },
    watch: {
      page() {
        this.rePut();
      },
      now() {
        this.rePut();
      },
      screenWidth() {
        if (this.screenWidth < 767){
          this.gap = 300;
          this.span=24;
        }
      }
    }
  };

</script>
