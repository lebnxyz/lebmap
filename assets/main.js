import { customScaledProjection, makeQueryFunc, normalize } from './scripts/utils.js';
import { countLocationNormalized } from './scripts/oneOffHelpers.js'
import mapJSON from './data/map/lb_2009_administrative_districts.geojson';
import { url as locJSON } from './data/map/locations.json';
import { data as respondentsJSON } from './data/respondents.json';
import * as d3 from 'd3';

const SVG_WIDTH = 600;
const SVG_HEIGHT = 600;

const MIN_RAD = 4;
const MAX_RAD = 10;

const respondents = makeQueryFunc(respondentsJSON);

const mapSVG = d3.select('body').append('svg')
  .attr('id', 'map')
  .attr('width', SVG_WIDTH)
  .attr('height', SVG_HEIGHT);
const chartSVG = d3.select('body').append('svg')
  .attr('id', 'chart');

mapSVG.append('g').attr('id', 'path-group');
mapSVG.append('g').attr('id', 'circle-group');

Promise.all([
    d3.json(mapJSON),
    d3.json(locJSON)
]).then(function([mapJSON, locJSON]) {
    const projection = customScaledProjection(1.1, 1, d3.geoMercatorRaw)
        .fitSize([SVG_WIDTH, SVG_HEIGHT], mapJSON);
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
        .attr('cx', place => projection(place.location)[0])
        .attr('cy', place => projection(place.location)[1])
        .attr('r', place => countLocationNormalized(place.name, respondents, MIN_RAD, MAX_RAD));
});
