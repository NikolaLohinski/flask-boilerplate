'use strict';
if (!Object.assign) Object.assign = require('object.assign').getPolyfill();

import Vue from 'vue';
import VueResource from 'vue-resource';
import Root from '../vue/root.vue';
import VuePromiseBtn from 'vue-promise-btn';
import VModal from 'vue-js-modal';
import 'vue-promise-btn/dist/vue-promise-btn.css';
import 'bootstrap-css-only';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faCheckCircle, faTimesCircle } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(faCheckCircle, faTimesCircle);
Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.config.productionTip = false;

Vue.use(VModal);
Vue.use(VuePromiseBtn);
Vue.use(VueResource);

global['vm'] = new Vue({
  el: '#app-container',
  components: {
    Root
  }
});
