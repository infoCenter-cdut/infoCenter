<template>
  <div style="white:100%;height:100%">
    <myRealTime></myRealTime>
    <myHugeData></myHugeData>
    <my-encourage :enInfo="enInfo"></my-encourage>
    <my-image></my-image>
    <my-video></my-video>
  </div>
</template>
<script>
import myRealTime from "./myRealTime";
import myHugeData from "./myHugeData";
import myEncourage from "./myEncourage";
import myImage from "./myImage";
import myVideo from "./myVideo";
export default {
  name: "myIndex",
  mounted() {},
  data() {
    return {
      passageShow: 0,
      flag: 0,
      timeId: null,
      enInfo: [
        {
          content:
            '"人生自有其沉浮,每个人都应该学会忍受生活中属于自己的一份悲伤,只有这样,你才能体会到什么叫做成功,什么叫做真正的幸福"',
          author: "李嘉诚"
        },
        {
          content:
            '"假如刮一阵风或滴几滴雨就阻止我去做这些轻而易举的事情，这样的懒惰还能为我给自己规划的未来作什么准备呢？"',
          author: "夏洛蒂·勃朗特"
        },
        {
          content: '"我们活着不能与草木同腐,不能醉生梦死,枉度人生,要有所作为"',
          author: "方志敏"
        }
      ]
    };
  },
  methods: {},
  filters: {
    slice(data, num) {
      if (data) return data.substring(0, num);
    }
  },
  components: {
    myRealTime,
    myHugeData,
    myEncourage,
    myImage,
    myVideo
  },
  computed: {
    Passage() {
      return this.$store.state.Passage;
    },
    DmImg() {
      return this.$store.state.dmInfo;
    },
    Video() {
      return this.$store.state.videoInfo;
    }
  }
};
</script>
<style scoped>
.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
</style>
