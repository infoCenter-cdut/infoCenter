<template>
  <div style="width:100%;position: relative;">
    <my-slide :bannerImg="bannerImg" :height="$store.state.screenWidth>767?82:62" :imgType="2">
    </my-slide>

    <div class="data-echart" ref="echart"></div>
    <div class="data-aside hidden-xs" v-if="$store.state.screenWidth>767">
      <div class="data-aside-select">
        <el-select v-model="search" filterable :placeholder="barTitle[0]" @change="change" style="width:20rem">
          <el-option v-for="(item,i) in barTitle" :key="i" :label="item" :value="item"></el-option>
        </el-select>
        <span class="data-aside-select-icon">
          <i class="icon icon-search small"></i>
        </span>
      </div>
      <div class="data-aside-about">
        <h4>关于数据分析</h4>
        <p>我们致力于收集各类有关毕业生就业的问题，并制定了一系列的专业问卷获取信息 通过对收集到的数据进行专业的数据处理和分析，找出企业和学生在思考方式之间的差距，并对其进行可视化展示 以最专业的态度和技术，做最通俗易懂的数据分析</p>
      </div>
      <div class="data-aside-hot">
        <h4>热点咨询</h4>
        <ul>
          <li v-for="(item,index) in passageTitle" :key="index">
            <router-link :to="'/news/'+passageUrl[index]"><span>{{item}}</span></router-link>
          </li>
        </ul>
      </div>
      <div class="data-aside-magazine">
        <h4>就业杂志</h4>
        <a :href="mgUrl">
          <img :src="mgImg" alt="">
        </a>
        <p>{{mgTitle}}</p>
      </div>
      <div class="data-aside-ad">
        <h5>广告位招租</h5>
      </div>
    </div>

    
    <div v-if="$store.state.screenWidth<768" class="data-aside-pe">
      <div class="data-aside-select-pe">
        <el-select v-model="search" filterable :placeholder="barTitle[0]" @change="change" style="width:19rem" size="mini">
          <el-option v-for="(item,i) in barTitle" :key="i" :label="item" :value="item"></el-option>
        </el-select>
        <span class="data-aside-select-icon-pe">
          <i class="icon icon-search small"></i>
        </span>
      </div>
      <div class="data-aside-about-pe">
        <h4>关于数据分析</h4>
        <p>我们致力于收集各类有关毕业生就业的问题，并制定了一系列的专业问卷获取信息 通过对收集到的数据进行专业的数据处理和分析，找出企业和学生在思考方式之间的差距，并对其进行可视化展示 以最专业的态度和技术，做最通俗易懂的数据分析</p>
      </div>
      <div class="data-aside-hot-pe">
        <h4>热点咨询</h4>
        <ul>
          <li v-for="(item,index) in passageTitle" :key="index">
            <router-link :to="'/news/'+passageUrl[index]"><span>{{item}}</span></router-link>
          </li>
        </ul>
      </div>
      <div class="data-aside-magazine-pe">
        <h4>就业杂志</h4>
        <a :href="mgUrl">
          <img :src="mgImg" alt="">
        </a>
        <p>{{mgTitle}}</p>
      </div>
      <div class="data-aside-ad">
        <h5>广告位招租</h5>
      </div>
    </div>
  </div>
</template>
<style lang="less" scoped src="./../assets/less/dataDisplay.less">

</style>
<script>
import mySlide from "./../components/subCom/mySlide";
export default {
  name: "dataDisplay",
  created() {
    if (!this.magazine)
      this.$store.dispatch('getData', { url: '/allMagazine', mutation: 'setMagazine', callback: this.getData });
    else {
      this.getData();
    }
  },
  mounted() {    
    if (this.barData) {   
      this.getInfo();
      this.drawLine(this.$refs.echart);
    }
  },
  data() {
    return {
      bannerImg: [{
          first: "Data exploring Department",
          second: "深入剖析问卷数据,掌握更为全面的就业形式",
          passage_img: require("./../assets/career/img/dataImg/1.jpg")
        },
        {
          first: "Data exploring Department",
          second: "深入剖析问卷数据,掌握更为全面的就业形式",
          passage_img: require("./../assets/career/img/dataImg/2.jpg")
        },
        {
          first: "Data exploring Department",
          second: "深入剖析问卷数据,掌握更为全面的就业形式",
          passage_img: require("./../assets/career/img/dataImg/3.jpeg")
        }
      ],
      nowShow: 0,
      barTitle: [],
      search: "",
      passageTitle: [],
      passageUrl: [],
      mgUrl: "",
      mgImg: "",
      mgTitle: "",

    };
  },
  methods: {
    drawLine(node, j = 0) {     
      let arr = this.barData[j].bar_dataset.split(/\s/g);
      for (let i = 0; i < arr.length; i++)
        arr[i] = parseFloat(arr[i]);
      let arr2 = this.barData[j].bar_axis.split(/,|，|\s/g);
      let myChart = this.$echarts.init(node);
      myChart.setOption({
        title: { text: this.barData[j].bar_title },
        tooltip: {},
        xAxis: {
          data: arr2,
        },
        legend: {
          data: [this.barData[j].bar_title.substring(this.barData[j].bar_title.length - 2, this.barData[j].bar_title.length)],
          width: 10,
          height: 10,
        },
        yAxis: {},
        series: [{
          name: this.barData[j].bar_title.substring(this.barData[j].bar_title.length - 2, this.barData[j].bar_title.length),
          type: this.barData[j].data_type,
          data: arr,
        }]
      });
    },
    getInfo() {
      this.barData.forEach(x => {
        this.barTitle.push(x.bar_title);
      });
      this.passage.forEach(x => {
        this.passageTitle.push(x.title);
        this.passageUrl.push(x.id);
      });
      // this.mgUrl = this.magazine[0].magazine;
      // this.mgImg = this.magazine[0].cover;
      // this.mgTitle = this.magazine[0].title;
      
      // console.log(this.$refs.echart)
      this.drawLine(this.$refs.echart);
    },
    change(e) {
      this.barTitle.forEach((x, i) => {
        if (x == e)
          this.nowShow = i;
      });
      this.drawLine(this.$refs.echart, this.nowShow);
    },
    getData() {
      if (!this.barData)
        this.$store.dispatch("getData", { url: "/allBarData", mutation: "setBarData", callback: this.getInfo });
    }
  },
  computed: {
    barData() {
      return this.$store.state.barData;
    },
    passage() {
      return this.$store.state.bannerImg;
    },
    magazine() {
      return this.$store.state.magazine;
    },
  },
  components: {
    mySlide
  }
};

</script>
