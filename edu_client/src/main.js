// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

//配置axios
import axios from "axios"

Vue.prototype.$axios = axios

//配置element-ui
import Element from "element-ui"
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(Element)

// 导入极验
import "../static/js/gt.js"

import "../static/css/global.css"

// vue-video-player
require('video.js/dist/video-js.css');
require('vue-video-player/src/custom-theme.css');
import VideoPlayer from 'vue-video-player'

Vue.use(VideoPlayer);

//配置状态机vuex
import store from "./store/index";

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store,
    components: {App},
    template: '<App/>'
})
