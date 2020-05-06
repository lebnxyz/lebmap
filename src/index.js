import { nest, values } from 'd3';
import Vue from 'vue';

import 'typeface-montserrat';
import { Query } from './scripts/utils.js';
import * as Tabs from 'vue-slim-tabs';
import Fitty from './vue-fitty.vue';

import App from './app.vue';
import respondents from './data/respondents.json';
import locations from './data/map/locations.json';
import questions from './data/questions.json';
import questionValues from './data/question_answers.json';


Vue.use((vue, settings) => vue.component('fitty', Fitty));
Vue.use(Tabs);

new Vue({
  render: h => h(App),
  el: '#app',
  components: {
    App
  },
  created() {
    // create non-reactive data
    this.questions = questions;
    this.locations = locations;
    this.respondents = respondents;
    this.questionValues = questionValues;
    this.locationsByDistrict = nest().key(d => d.district).map(values(locations));
    this.respondentQuery = new Query(respondents);
  }
});
