import * as d3 from 'd3';
import alasql from 'alasql';


export function customScaledProjection(xMult, yMult, rawProjection) {
  return d3.geoProjection(function(...args) {
    const [x, y] = rawProjection(...args);
    return [x * xMult, y * yMult];
  });
}


export class Query extends Function {
  constructor(queryObj) {
    super('...args', 'return this.$self.$call(...args)');
    this.$self = this.bind(this);
    this.$self.queryObj = queryObj;
    return this.$self;
  }

  $call(query, ...params) {
    return alasql(query, [this.queryObj, ...params]);
  }

  count(query, ...params) {
    return this.$call('SELECT COUNT(*) FROM $0 ' + query, ...params)[0]['COUNT(*)'];
  }
}


function unflatten(results, optionLength) {
  const o = Object.fromEntries(results.map(o => [o.result, o.count]));
  return Array.from(
    {length: optionLength},
    (_, i) => o[i]
  );
}

/**
 * Addresses https://stackoverflow.com/questions/61633745/using-group-by-with-alasqls-search
 * The column that results will be grouped by must be named `result`
 * @param {string} query Search query that returns a groupable result
 * @param {Query|Array} queryObj Either a Query instance (will be called) or a queryable array
 * @param {Object} transform Function to transform resulting array; the value 'unflatten'
 *   calls a predefined function
 * @param {Function} post A function to call on the result of the query obj (ugh) before transform/return
 * @return {Object|R} Grouped array of [{result: Number, count: Number}], or return value of transform
 */
export function searchAndGroupBy(query, queryObj, transform, post) {
  let res;
  if (queryObj instanceof Query) {
    res = queryObj(query);
  } else {
    res = alasql(query, queryObj);
  }
  if (post !== undefined) {
    res = post(res);
  }
  res = alasql('SELECT result, COUNT(*) AS [count] FROM $0 GROUP BY result', [res]);
  if (transform === undefined) {
    return res;
  }
  const ret = {}
  if (transform.unflatten !== undefined) {
    ret.unflatten = unflatten(res, transform.unflatten);
  }
  if (transform.raw !== undefined) {
    ret.raw = res;
  }
  if (transform.call !== undefined) {
    ret.call = transform.call(res);
  }
  return ret;
}


export function normalize(value, min, max, lower, upper) {
  return (value - min) / (max - min) * (upper - lower) + lower;
}


export function toID(prefix, s, use_hash = false) {
  return `${use_hash ? '#' : ''}${prefix}-${s.replace(/\s/, '-').toLowerCase()}`;
}

export function d(...objs) {
  objs.map(o => JSON.stringify(o))
    .map(o => JSON.parse(o))
    .forEach(o => console.log(o));
}
