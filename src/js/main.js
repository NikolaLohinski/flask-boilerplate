'use strict';
if (!Object.assign) Object.assign = require('object.assign').getPolyfill();

import Vue from 'vue';
import VueTouch from 'vue-touch';
import VueResource from 'vue-resource';

import Vm from './vm';

Vue.use(VueResource);
Vue.use(VueTouch, { name: 'v-touch' });

global['URL_API'] = window.location.href + 'api/v0/';
global['vm'] = new Vue(Vm);

window.applicationCache.addEventListener('updateready', () => {
  window.location.reload();
});
if (window.applicationCache.status === window.applicationCache.UPDATEREADY) {
  window.location.reload();
}
