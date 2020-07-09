<template>
    <div>
        <Header :headers="data_list"></Header>
        <Banner></Banner>
        <Footer :footers="data_list"></Footer>
    </div>
</template>

<script>
    import Banner from "./common/Banner";
    import Header from "./common/Header";
    import Footer from "./common/Footer";
    export default {
        name: "Home",
        data(){
            return{
                data_list:[],

            }
        },
        methods:{
            get_all_data(){
                this.$axios({
                    url:'http://127.0.0.1:8000/homeapp/nav/',
                    method: "get",
                }).then(res=>{
                    // 当前请求的返回值可以通过res接受到
                    console.log(res.data);
                    this.data_list = res.data;
                }).catch(error=>{
                    console.log(error);
                })
            },
        },
        // 在当前页面渲染之前将数据获取并赋值给 data
        created() {
            // 获取轮播图数据
            this.get_all_data();
        },
        components: {
            "Footer":Footer,
            "Header":Header,
            "Banner":Banner
        }
    }
</script>

<style scoped>
 .el-carousel__item h3 {
        color: #475669;
        font-size: 18px;
        opacity: 0.75;
        line-height: 300px;
        margin: 0;
    }

    .el-carousel__item:nth-child(2n) {
        background-color: #99a9bf;
    }

    .el-carousel__item:nth-child(2n+1) {
        background-color: #d3dce6;
    }
</style>
