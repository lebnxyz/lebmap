import * as d3 from 'd3';
import alasql from 'alasql';


export function customScaledProjection(xMult, yMult, rawProjection) {
    return d3.geoProjection(function(...args) {
        const [x, y] = rawProjection(...args);
        return [x * xMult, y * yMult];
    });
}


export function makeQueryFunc(obj) {
    return (query, ...params) => alasql(query, [obj, ...params]);
}


export function normalize(value, min, max, lower, upper) {
    return (value - min) / (max - min) * (upper - lower) + lower;
}
