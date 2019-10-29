<template>
  <svg v-if="regionPaths.length" :width="width" :height="height">
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
      ></region>
    </g>
  </svg>
</template>

<script>
import DummyRegion from './components/dummy-region.vue';
import Region from './components/region.vue';

import { geoMercator, geoPath, geoMercatorRaw } from 'd3';
import * as utils from './scripts/utils.js';

import mapJSON from './data/map/lb_2009_administrative_districts.json';

export default {
  name: 'App',
  components: {
    DummyRegion,
    Region
  },
  props: {
    defaultWidth: {
      type: Number,
      default: window.innerWidth / 2
    },
    defaultHeight: {
      type: Number,
      default: window.innerHeight
    }
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
        width: this.defaultWidth,
        height: this.defaultHeight
      }
    }
  },
  computed: {
    width() {
      return this.window.width / 2;
    },
    height() {
      return this.window.height;
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
    }
  }
};
</script>

<style scoped>
</style>
