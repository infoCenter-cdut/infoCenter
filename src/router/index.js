import Vue from "vue";
import Router from "vue-router";

const index = () => import("@/pages/index");
const allNews = () => import("@/pages/allNews");
const news = () => import("@/pages/news");
const dataDisplay = () => import("@/pages/dataDisplay");
const imgDisplay = () => import("@/pages/imgDisplay");
const allVideo = () => import("@/pages/allVideo");
const contactUs = () => import("@/pages/contactUs");
const videoDisplay = () => import("@/pages/videoDisplay");

Vue.use(Router);

export default new Router({
  mode:'history',
  routes: [
    {
      path: "",
      name: "index",
      component: index
    },
    {
      path: "/allNews/:search?",
      name: "allNews",
      component: allNews
    },
    {
      path: "/news/:id",
      name: "news",
      component: news
    },
    {
      path: "/dataDisplay",
      name: "dataDisplay",
      component: dataDisplay
    },
    {
      path: "/imgDisplay",
      name: "imgDisplay",
      component: imgDisplay
    },
    {
      path: "/allVideo/:search?",
      name: "allVideo",
      component: allVideo
    },
    {
      path: "/contactUs",
      name: "contactUs",
      component: contactUs
    },
    {
      path: "/video/:id",
      name: "video",
      component: videoDisplay
    }
  ],
});
