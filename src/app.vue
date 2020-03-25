<template>
  <div id="container">
    <div id="map" class="column">
      <svg v-if="regionPaths.length" width="100%" height="100%">
        <g>
          <dummy-region v-for="p in regionPaths" :key="p.o.ID_2"
            :d="path(p.o)"
          ></dummy-region>
        </g>
        <g>
          <region v-for="(p, index) in regionPaths" :key="p.district + index"
            :district="p.district"
            :d="path(p.o)"
            :projection="projection"
            :highlighted-places="highlightedPlaces"
            :n-selected="nSelected"
            @select="select"
            @unselect="unselect"
          ></region>
        </g>
      </svg>
    </div>
    <tabs id="info" class="info-tabs column">
      <tab title="Questions">
        <question-list :questionMap="$root.questionMap" @show-respondents="showRespondents"></question-list>
      </tab>
      <tab title="Insights" :disabled="true">
        <!--  -->
      </tab>
      <tab title="Answers">
        <list :selection="selectionValues" iterKey="name" v-slot="{item: place}"
          :bold="true"
        >
          {{place.name}}, <span class="faint">{{place.district}}</span>
          <span v-if="place.responses > 1">{{place.responses}}</span>
        </list>
      </tab>
    </tabs>
  </div>
</template>

<script>
import DummyRegion from './components/dummy-region.vue';
import Region from './components/region.vue';
import List from './components/list.vue';
import QuestionList from './components/question-list.vue'

import { geoMercator, geoPath, geoMercatorRaw } from 'd3';
import * as utils from './scripts/utils.js';

import mapJSON from './data/map/lb_2009_administrative_districts.json';

export default {
  name: 'App',
  components: {
    DummyRegion,
    Region,
    List,
    QuestionList
  },
  data() {
    const regionPaths = [];
    mapJSON.features.forEach(
      o => regionPaths.push({
        district: o.properties.DISTRICT,
        o: o
      })
    );
    return {
      regionPaths,
      window: {
        width: null,
        height: null
      },
      selection: {},
      nSelected: 0,
      highlightedPlaces: new Set()
    }
  },
  computed: {
    width() {
      return this.window.width / 2.5;
    },
    height() {
      return this.window.height * .95;
    },
    projection() {
      return utils.customScaledProjection(1.1, 1, geoMercatorRaw)
        .fitSize([this.width, this.height], mapJSON);
    },
    path() {
      return geoPath(this.projection);
    },
    selectionValues() {
      return Object.values(this.selection);
    }
  },
  created() {
    window.addEventListener('resize', this.resize);
    this.resize();
  },
  destroyed() {
    window.removeEventListener('resize', this.resize);
  },
  methods: {
    resize() {
      this.window.width = window.innerWidth;
      this.window.height = window.innerHeight;
    },
    select(pins) {
      pins.map(pin => {
        pin.selected = true;
        this.$set(this.selection, pin.place.name, pin.place);
        this.nSelected++;
      });
    },
    unselect(pins) {
      // better for performance than this.$delete (much faster, especially on later re-selects)
      pins.map(pin => {
        pin.selected = false;
        this.selection[pin.place.name] = undefined;
        this.nSelected--;
      });
    },
    showRespondents(respondents) {
      const s = new Set();
      respondents.map(uid => s.add(this.$root.respondents[uid].location));
      this.highlightedPlaces = s;
    }
  }
};
</script>

<style>
#container {
  display: flex;
  height: 100%;
  flex: none;
}

.faint {
  color: darkgray;
}

.column {
  display: flex;
  flex-direction: column;
  flex: 1;
  overflow: auto;
}

.vue-tab {
  color: white;
  cursor: pointer;
  font-family: sans-serif;
  display: inline-block;
  padding: 1em;
  background-color: #000;
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  transition: background-color 300ms;
}

.vue-tab:hover {
  background-color: #333;
}

.vue-tab[aria-selected="true"] {
  background-color: #fff;
  color: black;
}

.vue-tab[aria-disabled="true"] {
  cursor: not-allowed;
  color: #555;
  background-color: #000;
}
</style>
