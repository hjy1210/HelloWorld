var fs=require('fs')
var xml2js = require('xml2js')

var xmlStr2jsonStr=require('./xmljsonutil').xmlStr2jsonStr

function xml2json(xmlfile,jsonfile){
  fs.readFile(xmlfile, 'utf8', (err, xml) => {
    if (err) throw err
    xmlStr2jsonStr(xml,(err,json)=>{
      if (err) throw err
      fs.writeFile(jsonfile,json,(err)=>{
        if (err) throw err
        console.log("done")
      })
    })
  })
}
function json2xml(jsonfile, xmlfile) {
  fs.readFile(jsonfile, 'utf8', (err, data) => {
    if (err) throw err
    var obj = JSON.parse(data)
    var builder = new xml2js.Builder()
    var xml = builder.buildObject(obj)
    fs.writeFile(xmlfile, xml, (err) => {
      if (err) throw err
      console.log("done")
    })
  })
}
function xml2json0(xmlfile,jsonfile) {
  fs.readFile(xmlfile, 'utf8', (err, data) => {
    if (err) throw err
    json=xmlStr2jsonStr(data)
    //console.log(data)
    data=substituteContent(data)
    //var parseString = xml2js.parseString;
    parseString(data,(err,doc)=>{
      if (err) throw err
      doc=doc.root
      var json=JSON.stringify(doc,null,2)
      fs.writeFile(jsonfile,json,(err)=>{
        if (err) throw err
      })
    })
  })
}

var msg="Usage: \nnode conversion.js tojson <xmlfile> <jsonfile>\nnode conversion.js toxml <jsonfile> <xmlfile>"
//console.log(process.argv)
if (process.argv.length!=5 || (process.argv[2]!="toxml" && process.argv[2]!="tojson")){
  console.log(msg)
  return
}
if (process.argv[2]==="toxml"){
  json2xml(process.argv[3],process.argv[4])
} else {
  xml2json(process.argv[3],process.argv[4])
}