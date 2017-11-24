var mjAPI = require("mathjax-node");
mjAPI.config({
  MathJax: {
    extensions: 'mhchem.js',
    "TeX": { 
      mhchem: { legacy: false}
    }
  }
});

var yourMath = '\\ce{H2SO4} \\pu{1.0e-20}';

mjAPI.typeset({
  math: yourMath,
  format: "TeX", // "inline-TeX", "MathML"
  mml:true, //  svg:true,
}, function (data) {
  console.log(data.mml)
});
