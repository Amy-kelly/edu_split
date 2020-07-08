<template>
<el-carousel height="720px" :interval="3000" arrow="always">
        <el-carousel-item v-for="(banner, key) in banner_list" :key="key">
            <a href=""><img :src="banner.img" alt=""></a>
        </el-carousel-item>
    </el-carousel>
</template>

<script>
    export default {
        name: "Banner",
        data(){
            return{
                banner_list:[], // 轮播图的数据
            }
        },
        methods:{
            get_all_banner(){
                this.$axios({
                    url:'http://127.0.0.1:8000/homeapp/carousel/',
                    method: "get",
                }).then(res=>{
                    // 当前请求的返回值可以通过res接受到
                    console.log(res.data);
                    this.banner_list = res.data;
                }).catch(error=>{
                    console.log(error);
                })
            },
        },
        // 在当前页面渲染之前将数据获取并赋值给 data
        created() {
            // 获取轮播图数据
            this.get_all_banner();
        }

    }
</script>

<style scoped>

</style>
