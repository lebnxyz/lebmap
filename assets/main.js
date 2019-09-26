const width = 600;
const height = 600;

const map = d3.select('#map')
  .attr('width', width)
  .attr('height', height);
const chart = d3.select('#chart');

d3.json('../data/map/lb_2009_administrative_districts.geojson').then(function(lb) {
    const projection = d3.geoMercator()
      .fitSize([width, height], lb);
    const path = d3.geoPath(projection);

    map.append('path')
      .attr('d', path(lb));
});

