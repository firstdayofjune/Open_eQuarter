String.format = function() {
    // The string containing the format items (e.g. "{0}")
    // will and always has to be the first argument.
    var theString = arguments[0];

    // start with the second argument (i = 1)
    for (var i = 1; i < arguments.length; i++) {
        // "gm" = RegEx options for Global search (more than one instance)
        // and for Multiline search
        var regEx = new RegExp("\\{" + (i - 1) + "\\}", "gm");
        theString = theString.replace(regEx, arguments[i]);
    }

    return theString;
}

/**
 * Finds a layers given a 'name' attribute.
 * @param {type} name
 * @returns {unresolved}
 */
function findByName(name) {
    var layers = map.getLayers();
    var length = layers.getLength();
    for (var i = 0; i < length; i++) {
        if (name === layers.item(i).get('name')) {
            return layers.item(i);
        }
    }
    return null;
}


function layerFromGeoJSON(url, name) {
  var json_layer,
      start,
      end;

  json_layer = new ol.layer.Vector({
      source: new ol.source.Vector({
          url: url,
          format: new ol.format.GeoJSON()
      }),
      style: function(feature, resolution) {
          STYLE.getText().setText(resolution < 5000 ? feature.get('name') : '');
          return STYLE_CACHE;
      }
  });

  if (name === undefined) {
    start = url.lastIndexOf('/') + 1;
    end = url.lastIndexOf('.') - start;
    name = url.substr(start, end);
  }
  json_layer.set('name', name);

  return json_layer;
}
