import { customScaledProjection } from './scripts/d3-funcs.js';

const width = 600;
const height = 600;

const mapSVG = d3.select('#map')
  .attr('width', width)
  .attr('height', height);
const chartSVG = d3.select('#chart');

mapSVG.append('g').attr('id', 'path-group');
mapSVG.append('g').attr('id', 'circle-group');

Promise.all([
  d3.json('./assets/data/map/lb_2009_administrative_districts.geojson'),
  d3.json('./assets/data/map/locations.json')
]).then(function([mapJSON, locJSON]) {
    const projection = customScaledProjection(1.1, 1, d3.geoMercatorRaw)
      .fitSize([width, height], mapJSON);
    const path = d3.geoPath(projection);

    mapSVG.select('#path-group').selectAll('path')
      .data(mapJSON.features)
      .enter()
      .append('path')
      .attr('d', path)
      .on('mouseover', function() { d3.select(this).raise().classed('hover', true); })
      .on('mouseout', function() { d3.select(this).lower().classed('hover', false); });
    
    mapSVG.select('#circle-group').selectAll('circle')
      .data(d3.values(locJSON), function(o) { return o.name; })
      .enter()
      .append('circle')
      .attr('cx', function(o) { return projection(o.location)[0]; })
      .attr('cy', function(o) { return projection(o.location)[1]; });
});
