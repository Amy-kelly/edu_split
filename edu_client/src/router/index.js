import Vue from 'vue'
import Router from 'vue-router'

import Home from "../components/Home";
import Login from "../components/Login";
import Register from "../components/Register";
import Course from "../components/Course";
import CourseDetail from "../components/CourseDetail";
import Cart from "../components/Cart";
import Order from "../components/Order";
import OrderSuccess from "../components/OrderSuccess";
Vue.use(Router)

export default new Router({
    mode:"history",
  routes: [
    {
      path: '/',
      name: 'Home',
      component:Home
    },
    {
      path: '/home',
      name: 'Home',
      component:Home
    },
    {
      path: '/login',
      name: 'Login',
      component:Login
    },
    {
      path: '/register',
      name: 'Register',
      component:Register
    },
     {
      path: '/python',
      name: 'Course',
      component:Course
    },
     {
      path: '/course/detail/:id',
      name: 'CourseDetail',
      component:CourseDetail
    },
      {
      path: '/cart',
      name: 'Cart',
      component:Cart
    },
      {
      path: '/order',
      name: 'Order',
      component:Order
    },
       {
      path: '/payments/result',
      name: 'OrderSuccess',
      component:OrderSuccess
    },
  ]
})
