<template>
  <div class="my-huge-data">
    <div class="my-huge-data-main">
      <h4>漫游大数据</h4>
    </div>
    <div class="my-huge-data-middle">
      <p>我们致力于收集各类有关毕业生就业的问题，并制定了一系列的专业问卷来获取信息</p>
      <p>通过对收集到的数据进行专业的数据处理和分析，找出企业和学生在思考方式之间的不同，并对其进行可视化展示</p>
      <p>
        <strong>以最专业的态度和技术，做最通俗易懂的数据分析</strong>
      </p>
      <div class="my-huge-data-echart" v-if="screenWidth>768">
        <div class="echart-item-outer">
          <div class="my-huge-data-echart-itemPc my-huge-data-echart-item" v-for="(i) in 4" :key="i"></div>
        </div>
      </div>
      <div class="my-huge-data-echart" v-else>
        <div class="my-huge-data-echart-itemPe my-huge-data-echart-item" v-for="(i) in 4" :key="i"></div>
      </div>
    </div>
    <div class="my-huge-data-button">
      <el-button type="primary" plain @click="$router.push('/dataDisplay')">
        点击进入数据专区
      </el-button>
    </div>
  </div>
</template>
<style lang="less" scoped>
@itemSize: 15rem;
.my-huge-data-center(@w) {
  position: absolute;
  width: @w;
  @now: -@w* 0.5;
  left: 50%;
  margin-left: @now;
}

.my-huge-data {
  width: 100%;
  position: relative;
  background-color: #f5f5f5;
  @media screen and (min-width: 768px) {
    height: 100vh;
  }
  @media screen and (max-width: 767px) {
    height: 210vh;
  }
  &-main {
    .my-huge-data-center(6rem);

    & h4 {
      border-bottom: 2px solid rgba(0, 0, 0, 0.1);
    }

    top: 5%;
  }

  &-middle {
    position: absolute;
    top: 15%;
    width: 100%;
    & p {
      width: 100%;
      text-align: center;
      font-size: 1rem;
    }
  }
  &-button {
    .my-huge-data-center(10rem);
    bottom: 5%;
    & a:hover {
      color: black;
    }
  }
  &-echart {
    width: 100%;
    @media screen and (max-width: 767px) {
      height: 140vh;
      overflow: hidden;
    }
    &-itemPc {
      float: left;
      clear: none;
      width: @itemSize;
      height: @itemSize;
      @media screen and (max-width: 976px) {
        width: @itemSize*0.6;
        height: @itemSize*0.6;
      }
    }
    &-itemPe {
      width: @itemSize;
      height: @itemSize;
      margin: 0 auto;
    }
  }
}
.echart-item-outer {
  margin: 0 auto;
  width: 4 * @itemSize;
  @media screen and (max-width: 976px) {
    width: @itemSize*2.4;
  }
}
</style>
<script>
export default {
  name: "myHugeData",
  data() {
    return {
      opt: [
        //echarts数据配置
        { color: "#FD685B", num: 73 },
        { color: "#FFCE54", num: 85 },
        { color: "#A0D468", num: 70 },
        { color: "#AC92EC", num: 95 }
      ]
    };
  },
  mounted() {
    let node = document.getElementsByClassName("my-huge-data-echart-item");
    this.drawLine(node, this.opt); //echarts渲染数据
  },
  methods: {
    drawLine(node, opt) {
      for (let i = 0; i < node.length; i++) {
        var myChart = this.$echarts.init(node[i]);
        myChart.setOption({
          color: [opt[i].color, "rgba(0,0,0,0)"], //手动设置每个图例的颜色
          legend: {
            show: false
          },
          graphic: {
            type: "text",
            left: "center",
            top: "center",
            style: {
              text: opt[i].num + "%",
              textAlign: "center",
              fill: "#000",
              fontSize: 20,
              width: 300,
              height: 300
            }
          },
          series: [
            //系列列表
            {
              name: "首页饼状图", //系列名称
              type: "pie", //类型 pie表示饼图
              radius: ["60%", "70%"], //饼图的半径,第一项是内半径,第二项是外半径,内半径为0就是真的饼,不是环形
              itemStyle: {
                //图形样式
                normal: {
                  //normal 是图形在默认状态下的样式；emphasis 是图形在高亮状态下的样式，比如在鼠标悬浮或者图例联动高亮时。
                  label: {
                    //饼图图形上的文本标签
                    show: false //平常不显示
                  },
                  labelLine: {
                    //标签的视觉引导线样式
                    show: false //平常不显示
                  }
                },
                emphasis: {
                  //normal 是图形在默认状态下的样式；emphasis 是图形在高亮状态下的样式，比如在鼠标悬浮或者图例联动高亮时。
                  label: {
                    show: false
                  }
                }
              },
              data: [{ value: opt[i].num }, { value: 100 - opt[i].num }]
            }
          ]
        });
      }
    }
  },
  computed: {
    screenWidth() {
      return this.$store.state.screenWidth;
    }
  },
  watch: {
    screenWidth() {
      //页面宽度发生变化，echarts重新渲染
      let node = document.getElementsByClassName("my-huge-data-echart-item");
      this.drawLine(node, this.opt);
    }
  }
};
</script>
