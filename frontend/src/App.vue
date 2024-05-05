<template>
  <div>
      <label><input type="radio" v-model="nowRoom" value="living">リビング</label>
      <label><input type="radio" v-model="nowRoom" value="bed">寝室</label>
  </div>
  <hr>
  <div v-show="this.nowRoom=='living'">
    <Contoller
    title="リビングテレビ"
    :url="this.livingURL"
    preSigName="living_tv"
    :buttons='
      [
      {"入力切替":"srcchange", "電源":"power"},
      {"地デジ":"grounddigital", "bs":"bs", "cs":"cs"},
      {"1":"1", "2":"2", "3":"3"},
      {"4":"4", "5":"5", "6":"6"},
      {"7":"7", "8":"8", "9":"9"},
      {"10":"10", "11":"11", "12":"12"},
      {"ch↑":"chup", "消音":"silent", "vol↑":"volumeup"},
      {"ch↓":"chdown", "サブ":"submenue", "vol↓":"volumedown"},
      {"録画":"record", "↑↑":"upup", "番組表":"listings"},
      {"↑":"up"},
      {"←":"left", "決定":"decision", "→":"right"},
      {"↓":"down"},
      {"戻る":"back", "↓↓":"downdown", "終了":"finish"},
      {"<<":"recleftleft", "▶︎":"recplay", ">>":"recrightright"},
      {"|<<":"recmostleft", "■":"recstop", "||":"recpause",">>|":"recmostright"},
      ]'
      />
    <hr>
    <Contoller
    title="リビング電気"
    :url="this.livingURL"
    preSigName="living_light"
    :buttons='
      [
      {"蛍光灯":"keikoutou", "図書館":"toshokan"},
      {"食卓":"shokutaku", "電球":"denkyu"},
      {"リラ":"rirakkusu", "ひろ":"hirobiro"},
      {"全灯":"zentou"},
      {"保安":"hoankyu", "消灯":"shoutou"},
      ]'
      />
      <hr>
  </div>
  <div v-show="this.nowRoom=='bed'">
    <Contoller
    title="寝室電気"
    :url="this.bedURL"
    preSigName="bed_light"
    :buttons='
      [
      {"電源":"dengen"},
      {"全灯":"zentou", "常夜灯":"zyouyatou"},
      {"くつろぎ":"kutsurogi"},
      ]'
    />
    <hr>
    <Contoller
    title="寝室エアコン"
    :url="this.bedURL"
    preSigName="bed_aircon"
    :buttons='
      [
      {"暖房":"danbou"},
      {"冷房28度":"reibou28"},
      {"切タイマ":"kirutaima", "取消":"torikeshi"},
      {"停止":"teishi"},
      ]'
      />
      <hr>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Contoller from "./components/Contoller.vue"
export default {
  name: 'App',
  data(){
    return{
      livingURL:"http://livingpi:5001",
      bedURL:"http://bedpi:5001",
      nowRoom:"living",
    }
  },
  components: {
    Contoller,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

input.geomsize {
   width: 2em;
   height: 2em;
}
</style>
