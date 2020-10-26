<template>
  <div>
    <mySlide :bannerImg="bannerImg" :height="screenWidth>767?82:62" :imgType="2"></mySlide>
    <myNews></myNews>
  </div>
</template>
<script>
import myNews from "@/components/allNews/myNews";
import mySlide from "@/components/subCom/mySlide";
export default {
  name: "allNews",
  mounted() {},
  data() {
    return {
      flag: false,
      bannerImg: [
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
  methods: {},
  components: {
    myNews,
    mySlide
  },
  computed: {
    screenWidth(){
      return this.$store.state.screenWidth;
    }
  },
  watch: {}
};
</script>
<style scoped>
@media screen and (min-width: 768px) {
}
</style>
