const locationStorage = {};

export function countLocation(loc, query) {
    if (!(loc in locationStorage)) {
        locationStorage[loc] = query('SELECT COUNT(*) FROM $0 WHERE location = $1', loc)[0]['COUNT(*)'];
    }
    return locationStorage[loc];
}
