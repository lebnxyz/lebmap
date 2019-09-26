export function customScaledProjection(xMult = 1.1, yMult = 1, rawProjection = d3.geoMercatorRaw) {
    return d3.geoProjection(function(...args) {
        const [x, y] = rawProjection(...args);
        return [x * xMult, y * yMult];
    });
}