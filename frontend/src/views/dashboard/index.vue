<template>
  <div class="dashboard-container">
    <div class="dashboard-text">name: {{ name }}</div>
    {{ link }}
    <br>
    <a :href="link">百度</a>
    <br>
    <span v-html="myLink" />
    <br>
    <span v-text="myLink" />
    <br>
    <input type="text" @keyup.enter="addbtn">
    {{ count }}
    <button type="button" @click="addbtn()">add</button>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  data() {
    return {
      count: 0,
      link: 'www.baidu.com',
      myLink: '<a href="www.gamersky.com">游民</a>'
    }
  },

  computed: {
    ...mapGetters([
      'name'
    ])
  },
  methods: {
    addbtn: function() {
      this.count += 1
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
