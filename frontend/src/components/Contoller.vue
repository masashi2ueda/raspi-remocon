<template>
    <div>
      <h1>{{title}}</h1>
    </div>
    <div>
        <div v-for="btn in buttons" :key="btn">
            <div class="container">
                <div v-for="devName in Object.keys(btn)" :key="devName">
                    <button class="MyButton" v-on:click="send(btn[devName])">{{devName}}</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import send_sig from "../js/transfer"
export default {
    props:{
        title:String,
        url:String,
        preSigName:String,
        buttons:Object,
    },
    methods:{
        send:function(coreName){
            send_sig(this.url,
                this.preSigName+"_"+coreName
            );
        },
    },
}
</script>

<style>
@import "../css/button.css";
@import "../css/container.css";
</style>
