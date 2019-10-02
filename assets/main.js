import { customScaledProjection } from './scripts/d3-funcs.js';
import { url as mapJSON } from './data/map/lb_2009_administrative_districts.geojson';
import { url as locJSON } from './data/map/locations.json';
import * as d3 from 'd3';

const width = 600;
const height = 600;


const mapSVG = d3.select('body').append('svg')
  .attr('id', 'map')
  .attr('width', width)
  .attr('height', height);
const chartSVG = d3.select('body').append('svg')
  .attr('id', 'chart');

mapSVG.append('g').attr('id', 'path-group');
mapSVG.append('g').attr('id', 'circle-group');

Promise.all([
    d3.json(mapJSON),
    d3.json(locJSON)
]).then(function([mapJSON, locJSON]) {
    const projection = customScaledProjection(1.1, 1, d3.geoMercatorRaw)
        .fitSize([width, height], mapJSON);
    const path = d3.geoPath(projection);

    mapSVG.select('#path-group').selectAll('path')
        .data(mapJSON.features)
        .enter()
        .append('path')
        .attr('d', path)
        .on('click', function() { const o = d3.select(this); o.classed('clicked', !o.classed('clicked')); })
        // class .hover rather pseudo :hover required because Firefox is lame
        .on('mouseover', function() { d3.select(this).raise().classed('hover', true); })
        .on('mouseout', function() { d3.select(this).classed('hover', false); });
    
    mapSVG.select('#circle-group').selectAll('circle')
        .data(d3.values(locJSON), function(o) { return o.name; })
        .enter()
        .append('circle')
        .attr('cx', function(o) { return projection(o.location)[0]; })
        .attr('cy', function(o) { return projection(o.location)[1]; });
});
