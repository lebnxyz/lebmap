import { nest, values } from 'd3';
import Vue from 'vue';

import App from './app.vue';

import respondents from './data/respondents.json';
import locations from './data/map/locations.json';
import { makeQueryFunc } from './scripts/utils.js';

new Vue({
  data() {
    return {
      locations,
      respondents,
      locationsByDistrict: nest().key(d => d.district).map(values(locations)),
      respondentQuery: makeQueryFunc(respondents)
    }
  },
  el: '#app',
  render: h => h(App),
  components: { App }
});
