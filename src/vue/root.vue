<template>
  <div class="root">
    <div class="selection">
      <card v-for="s in sample" :key="s._id" :name="s.name" :info="s.info">
      </card>
    </div>
    <div class="drop"></div>
  </div>
</template>
<script>
  import Card from './card.vue';
  export default {
    data () {
      return {
        number: 3,
        sample: []
      };
    },
    methods: {
      treatSample (result) {
        if (result.body.success) {
          this.sample = result.body.result.inventions;
        }
      }
    },
    components: {
      Card
    },
    mounted () {
      const form = new FormData();
      form.append('number', 3);
      this.$http.post(global.URL_API + 'inventions/sample', form).then(this.treatSample);
    }
  };
</script>
<style lang="sass" type="text/scss" rel="stylesheet/scss" scoped>
  @import '../scss/general';
  .root {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: $background-color;
    color: $font-color;
    font-family: $font;
  }
</style>
