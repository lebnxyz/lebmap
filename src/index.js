import { nest, values } from 'd3';
import Vue from 'vue';

import 'typeface-montserrat';
import Fitty from './vue-fitty.vue';

import App from './app.vue';
import respondents from './data/respondents.json';
import locations from './data/map/locations.json';
import { Query } from './scripts/utils.js';


Vue.use((vue, settings) => vue.component('fitty', Fitty));

new Vue({
  data() {
    return {
      locations,
      respondents,
      locationsByDistrict: nest().key(d => d.district).map(values(locations)),
      respondentQuery: new Query(respondents)
    }
  },
  el: '#app',
  render: h => h(App),
  components: { App }
});
