import * as d3 from 'd3';
import Vue from 'vue';

import App from './app.vue';

import { data as respondents } from './data/respondents.json';
import { data as locations } from './data/map/locations.json';
import { makeQueryFunc } from './scripts/utils.js';

new Vue({
  data() {
    return {
      locations,
      respondents,
      locationsByDistrict: d3.nest().key(d => d.district).map(d3.values(locations)),
      respondentQuery: makeQueryFunc(respondents)
    }
  },
  el: '#app',
  render: h => h(App),
  components: { App }
});
