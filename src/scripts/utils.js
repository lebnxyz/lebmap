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


export function normalize(value, min, max, lower, upper) {
    return (value - min) / (max - min) * (upper - lower) + lower;
}


export function toID(prefix, s, use_hash = false) {
    return `${use_hash ? '#' : ''}${prefix}-${s.replace(/\s/, '-').toLowerCase()}`;
}
