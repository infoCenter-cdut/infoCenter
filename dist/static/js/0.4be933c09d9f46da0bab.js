webpackJsonp([0],{KA1d:function(t,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i={name:"mySlide",props:{bannerImg:{type:Array,default:[]},height:{type:[Number],default:100},imgType:{type:Number,default:1}},created:function(){this.screenWidth<1400&&(this.marginTop=-7e3/this.screenWidth+"rem");var t=this.height/100*this.$store.state.screenHeight;this.$store.commit("setBannerHeight",t)},mounted:function(){this.play()},data:function(){return{flag:0,timeId:null,marginTop:0,sx:"",tx:""}},methods:{play:function(){this.timeId||(this.timeId=setInterval(this.autoPlay,3e3))},autoPlay:function(){this.flag=this.flag==this.bannerImg.length-1?0:this.flag+1},change:function(t,e){t||(this.stop(),this.flag=e)},stop:function(){clearInterval(this.timeId),this.timeId=null},getNext:function(){return this.flag==this.bannerImg.length-1?this.flag:this.flag+1},getPre:function(){return 0==this.flag?this.flag:this.flag-1},touchStart:function(t){this.sx=t.touches[0].pageX,this.stop()},touchMove:function(t){if(1==this.imgType){var e=t.touches[0].pageX;this.$refs.img[this.flag].style="transform:translateX("+(e-this.sx)+"px)",e>this.sx?this.getPre()!=this.flag&&(this.$refs.img[this.getPre()].style="transform:translateX("+(e-this.sx-this.screenWidth)+"px"):e<this.sx&&this.getNext()!=this.flag&&(this.$refs.img[this.getNext()].style="transform:translateX("+(this.screenWidth+e-this.sx)+"px")}else{var s=t.touches[0].pageX;this.$refs.img2[this.flag].style=this.nowImg+";transform:translateX("+(s-this.sx)+"px)",s>this.sx?this.getPre()!=this.flag&&(this.$refs.img2[this.getPre()].style=this.preImg+";transform:translateX("+(s-this.sx-this.screenWidth)+"px"):s<this.sx&&this.getNext()!=this.flag&&(this.$refs.img2[this.getNext()].style=this.nextImg+";transform:translateX("+(this.screenWidth+s-this.sx)+"px")}},touchEnd:function(t){1==this.imgType?(this.tx=t.changedTouches[0].pageX,this.tx>this.sx?(this.$refs.img[this.flag].style=this.$refs.img[this.getPre()].style="",this.flag=this.getPre()):this.tx<this.sx&&(this.$refs.img[this.flag].style=this.$refs.img[this.getNext()].style="",this.flag=this.getNext())):(this.tx=t.changedTouches[0].pageX,this.tx>this.sx?(this.$refs.img2[this.flag].style=this.nowImg,this.$refs.img2[this.getPre()].style=this.preImg,this.flag=this.getPre()):this.tx<this.sx&&(this.$refs.img2[this.flag].style=this.nowImg,this.$refs.img2[this.getNext()].style=this.nextImg,this.flag=this.getNext()))},preOne:function(){this.timeId&&this.stop(),this.flag=(this.flag+this.bannerImg.length-1)%this.bannerImg.length},nextOne:function(){this.timeId&&this.stop(),this.flag=(this.flag+this.bannerImg.length+1)%this.bannerImg.length}},computed:{_height:function(){return"number"==typeof this.height?this.height+"vh":this.height},screenWidth:{get:function(){return this.$store.state.screenWidth},set:function(){}},nowImg:function(){return"background-image:url("+this.bannerImg[this.flag].passage_img+")"},preImg:function(){return"background-image:url("+this.bannerImg[this.getPre()].passage_img+")"},nextImg:function(){return"background-image:url("+this.bannerImg[this.getNext()].passage_img+")"}},watch:{screenWidth:function(){this.screenWidth<1400&&(this.marginTop=-7e3/this.screenWidth+"rem")}}},n={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"slide-container",style:{height:t._height},on:{mouseover:t.stop,mouseout:t.play,touchstart:t.touchStart,touchmove:t.touchMove,touchend:t.touchEnd}},[t._l(t.bannerImg,function(e,i){return s("div",{key:i,staticClass:"slide-item",style:{height:t._height}},[s("transition",{attrs:{appear:"",mode:"out-in","enter-active-class":"myAniIn","leave-active-class":"myAniOut"}},[s("div",{directives:[{name:"show",rawName:"v-show",value:1==t.imgType&&t.flag==i,expression:"imgType==1&&flag==index"}],ref:"img",refInFor:!0,staticClass:"slide-item-img"},[s("img",{attrs:{src:e.passage_img,width:"100%"}})])]),t._v(" "),s("transition",{attrs:{appear:"",mode:"out-in","enter-active-class":"myAniIn","leave-active-class":"myAniOut"}},[s("div",{directives:[{name:"show",rawName:"v-show",value:2==t.imgType&&t.flag==i,expression:"imgType==2&&flag==index"}],ref:"img2",refInFor:!0,staticClass:"slide-item-imgTwo",style:{"background-image":"url("+e.passage_img+")"}})]),t._v(" "),s("div",{directives:[{name:"show",rawName:"v-show",value:e.title&&i==t.flag,expression:"(item.title)&&index==flag"}],staticClass:"slide-item-title",style:{"margin-top":t.marginTop}},[t.$store.state.screenWidth>767?s("h1",{staticClass:"white myAniTitleIn"},[t._v(t._s(e.title))]):s("h3",{staticClass:"white myAniTitleIn"},[t._v(t._s(e.title))]),t._v(" "),s("el-button",{on:{click:function(s){t.$router.push("/news/"+e.id)}}},[t._v("\n        READ MORE\n      ")])],1),t._v(" "),e.first&&i==t.flag?s("div",{staticClass:"slide-item-other"},[s("h3",{staticClass:"slide-item-first white animated zoomIn"},[t._v(t._s(e.first))]),t._v(" "),s("span",{staticClass:"white animated fadeIn"},[t._v(t._s(e.second))])]):t._e(),t._v(" "),s("transition",{attrs:{appear:"","enter-active-class":"myAniSourceIn"}},[e.source&&i==t.flag?s("div",{staticClass:"slide-item-from centertxt hidden-xs"},[t._v("\n        文章来源：\n        "),s("span",[t._v(t._s(e.source))])]):t._e()])],1)}),t._v(" "),t.bannerImg&&t.bannerImg.length>1?s("div",{staticClass:"slide-pagination",style:{"margin-left":-.9*t.bannerImg.length+"rem"}},t._l(t.bannerImg,function(e,i){return s("span",{key:i,staticClass:"slide-pagination-item",class:{"slide-pagination-item-active":i==t.flag},on:{click:function(e){t.change(null,i)}}})}),0):t._e(),t._v(" "),t.bannerImg.length>1?s("div",{staticClass:"slide-navigation hidden-xs"},[s("i",{staticClass:"icon icon-arrow-left-simple",on:{click:t.preOne}}),t._v(" "),s("i",{staticClass:"icon icon-arrow-right-simple",on:{click:t.nextOne}})]):t._e()],2)},staticRenderFns:[]};var a=s("VU/8")(i,n,!1,function(t){s("XsyB"),s("hd2e")},"data-v-f29eff18",null);e.a=a.exports},XsyB:function(t,e){},hd2e:function(t,e){}});