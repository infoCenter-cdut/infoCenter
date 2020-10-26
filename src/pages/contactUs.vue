<template>
  <div style="width: 100%">
    <my-slide :bannerImg="bannerImg" :height="$store.state.screenWidth>767?120:80" :imgType="2"></my-slide>
    <myContact></myContact>
  </div>
</template>
<style lang="less" scoped>
</style>
<script>
import mySlide from './../components/subCom/mySlide.vue'
import myContact from '../components/contactUs/myContact.vue'
export default {
  name: 'contactUs',
  data() {
    return {
      bannerImg: [{
        passage_img: require('./../assets/career/img/contact.jpeg'),
        first: '成都理工大学就业指导中心学生就业信息中心',
        second: '只为遇见更好的你',
      }],
    }
  },
  methods: {

  },
  components: {
    mySlide,
    myContact
  }
}

</script>
