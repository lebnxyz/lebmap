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
    
    console.log('L', locJSON);
    
    mapSVG.selectAll('circle')
      .data(locJSON, function(o) { console.log(o); return o.name; })
      .enter()
      .append('circle')
      .attr('cx', function(o) { console.log('cx', o); return customScaledProjection(o.location)[0]; })
      .attr('cy', function(o) { console.log('cy', o); return customScaledProjection(o.location)[1]; })
      .attr('r', '8px')
      .attr('fill', 'green');
});

