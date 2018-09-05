'use strict';
if (!Object.assign) Object.assign = require('object.assign').getPolyfill();

import Vue from 'vue';
import VueResource from 'vue-resource';
import Root from '../vue/root.vue';

Vue.use(VueResource);
global['vm'] = new Vue({
  el: '#app-container',
  components: {
    Root
  }
});
