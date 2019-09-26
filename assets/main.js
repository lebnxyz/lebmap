import { customScaledProjection } from './scripts/d3-funcs.js';

const width = 600;
const height = 600;

const mapSVG = d3.select('#map')
  .attr('width', width)
  .attr('height', height);
const chartSVG = d3.select('#chart');

Promise.all([
  d3.json('../data/map/lb_2009_administrative_districts.geojson'),
  d3.json('../data/map/locations.json')
]).then(function([mapJSON, locJSON]) {
    const projection = customScaledProjection(1.1)
      .fitSize([width, height], mapJSON);
    const path = d3.geoPath(projection);

    mapSVG.append('path')
      .attr('d', path(mapJSON));
});

