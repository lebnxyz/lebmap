import Vue from 'vue';
import App from './app.vue';

import { data as respondents } from './data/respondents.json';
import { makeQueryFunc } from './scripts/utils.js';

const e = respondents;

new Vue({
  data() {
    return {
      respondents: e,
      respondentQuery: makeQueryFunc(e),
    }
  },
  el: '#app',
  render: h => h(App),
  components: { App }
});
