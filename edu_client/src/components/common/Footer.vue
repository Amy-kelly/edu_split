<template>
 <div class="footer">
        <ul>
            <li v-for="footer in footers" v-if="footer.position === 2">
                <span v-if="footer.is_site"><a :href="footer.link">{{footer.title}}</a></span>
                <span v-else><router-link :to="footer.link">{{footer.title}}</router-link></span>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Footer",
        props:["footers"]


    }
</script>

<style scoped>
 .footer {
        width: 100%;
        height: 128px;
        background: rgba(39, 46, 42, 0.7);
        color: #fff;
    }

    .footer ul {
        margin: 0 auto 16px;
        padding-top: 38px;
        width: 810px;
    }

    .footer ul li span{
        float: left;
        width: 112px;
        margin: 0 10px;
        text-align: center;
        font-size: 14px;
        color: white;
    }

    .footer ul::after {
        content: "";
        display: block;
        clear: both;
    }

    .footer p {
        text-align: center;
        font-size: 12px;
    }
</style>
