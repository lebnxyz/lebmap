import { normalize } from './utils.js';

const LOCATION_STORAGE = {};
let MAX_LOCATION = -1;


export function countLocation(loc, query) {
    if (!(loc in LOCATION_STORAGE)) {
        LOCATION_STORAGE[loc] = query('SELECT COUNT(*) as n FROM $0 WHERE location = $1', loc)[0]['n'];
    }
    return LOCATION_STORAGE[loc];
}


export function countLocationNormalized(loc, query, lower, upper) {
    if (MAX_LOCATION < 0) {
        MAX_LOCATION = query('SELECT COUNT(location) as n FROM $0 GROUP BY location ORDER BY n DESC LIMIT 1')[0]['n'];
    }
    return Math.ceil(normalize(countLocation(loc, query), 1, MAX_LOCATION, lower, upper));
}
