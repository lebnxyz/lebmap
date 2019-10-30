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
            @select="select"
            @unselect="unselect"
          ></region>
        </g>
      </svg>
    </div>
    <div id="info" class="column">
      <answer-list :selection="selection"></answer-list>
    </div>
  </div>
</template>

<script>
import DummyRegion from './components/dummy-region.vue';
import Region from './components/region.vue';
import AnswerList from './components/answer-list.vue';

import { geoMercator, geoPath, geoMercatorRaw } from 'd3';
import * as utils from './scripts/utils.js';

import mapJSON from './data/map/lb_2009_administrative_districts.json';

export default {
  name: 'App',
  components: {
    DummyRegion,
    Region,
    AnswerList
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
      mapJSON,
      regionPaths,
      window: {
        width: null,
        height: null
      },
      selection: {}
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
      pins.map(pin => this.$set(this.selection, pin.place.name, pin.place));
    },
    unselect(pins) {
      pins.map(pin => this.$delete(this.selection, pin.place.name));
    }
  }
};
</script>

<style scoped>
#container {
  display: flex;
  height: 100%;
  flex: none;
}

.column {
  display: flex;
  flex-direction: column;
  flex: 1;
  overflow: auto;
}
</style>
