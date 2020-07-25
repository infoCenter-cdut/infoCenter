<template>
  <div style="width:100%">
   <mySlide :bannerImg="bannerImg0" :height="screenWidth>767?82:62" :imgType="2"></mySlide>
    <my-news :next="nextId" :prev="prevId" :nowNew="nowNew"></my-news>
  </div>
</template>
<style lang="less" scoped>
</style>
<script>
import mySlide from "./../components/subCom/mySlide";
import myNews from "./../components/news/myNews";
export default {
  name: "news",
  components: {
    mySlide,
    myNews
  },
  created() {
    // console.log(this.bannerImg);
    
    if (this.bannerImg) this.getImg();
  },
  data() {
    return {
      nowImg: [],
      nowIndex: -1,
      nowNew: {},
      nextId: -1,
      prevId: -1,
      bannerImg0: [
        {
          first: "Materials collecting Depatment",
          second: "集思广益，与时俱进，只为带来更真实的文字",
          passage_img: require("./../assets/career/img/news/N1.jpg")
        },
        {
          first: "Materials collecting Depatment",
          second: "集思广益，与时俱进，只为带来更真实的文字",
          passage_img: require("./../assets/career/img/news/N2.jpg")
        }
      ]
    };
  },
  methods: {
    getImg() {
      let arr = this.bannerImg;
      // console.log(arr);
      
      this.nowImg = arr.filter(x => x.id != this.nowId);
      arr.forEach((x, i) => {
        if (x.id == this.nowId) {
          this.nowIndex = i;
          this.nowNew = x;
        }
      });
      if (this.nowIndex == 0) this.prevId = -1;
      else this.prevId = arr[this.nowIndex - 1].id;
      if (this.nowIndex == arr.length - 1) this.nextId = -1;
      else this.nextId = arr[this.nowIndex + 1].id;


    }
  },
  computed: {
    bannerImg() {
      return this.$store.state.bannerImg;
    },
    nowId() {
      return this.$route.params.id;
    },
     screenWidth(){
      return this.$store.state.screenWidth;
    }
  },
  watch: {
    bannerImg() {
      this.getImg();
    },
    nowId() {
      this.getImg();
    }
  }
};
</script>
