import { scaleOrdinal } from 'd3-scale';
import { schemePaired } from 'd3-scale-chromatic';

const autoColorScale = scaleOrdinal(schemePaired);

function autoColorObjects(objects, colorByAccessor, colorField) {
  if (!colorByAccessor || typeof colorField !== 'string') return;

  objects.filter(obj => !obj[colorField]).forEach(obj => {
    obj[colorField] = autoColorScale(colorByAccessor(obj));
  });
}

export { autoColorObjects };
