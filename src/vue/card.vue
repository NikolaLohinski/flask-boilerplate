<template>
  <div class="card">
    <div>{{ name }}</div>
  </div>
</template>
<script>
  export default {
    props: {
      name: String,
      info: String
    }
  };
</script>
<style lang="sass" type="text/scss" rel="stylesheet/scss" scoped>
  .card {
  }
</style>
