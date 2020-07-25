<template>
  <div>
    <div>
      <mySlide :bannerImg="img.slice(0, 4)" :height="100"></mySlide>
    </div>
    <myIndex></myIndex>
  </div>
</template>
<style scoped>
</style>
<script>
import myIndex from "@/components/index/myIndex";
import mySlide from "@/components/subCom/mySlide";
export default {
  name: "index",
  created() {
    if (!this.bannerImg)
      this.$store.dispatch('getData', { url: '/allNews', mutation: 'setBannerImg', callback: this.getImg })
    else {
      this.getImg();
    }
  },
  data() {
    return {
      img: [],
    };
  },
  components: {
    myIndex,
    mySlide
  },
  methods: {
    getImg() {
      this.img = this.$store.state.bannerImg;
    }
  },
  computed: {}
};

</script>
