import { nest, values } from 'd3';
import Vue from 'vue';

import App from './app.vue';

import respondents from './data/respondents.json';
import locations from './data/map/locations.json';
import { Query } from './scripts/utils.js';

const r = new Query(respondents);
window.rq = r;

new Vue({
  data() {
    return {
      locations,
      respondents,
      locationsByDistrict: nest().key(d => d.district).map(values(locations)),
      respondentQuery: r
    }
  },
  el: '#app',
  render: h => h(App),
  components: { App }
});
