var DOMParser = require('xmldom').DOMParser;
var fs=require('fs')

function processXml(xmlfile) {
  fs.readFile(xmlfile, 'utf8', (err, data) => {
    if (err) throw err
    console.log(data)
    //var parseString = xml2js.parseString;
    var doc=new DOMParser().parseFromString(data)
    //console.log(doc)
    console.log(doc.childNodes.length)
    for (var i=0;i<doc.childNodes.length;i++){
      console.log(doc.childNodes[i].nodeName,doc.childNodes[i].nodeType,doc.childNodes[i].nodeValue)
    }
    var author=doc.getElementsByTagName('author')[0]
    dumpNodeInfo(author,3)
  })
}
function dumpNodeInfo(node,level=1,heading=""){
  if (level<1) return
  console.log(heading,node.nodeName,node.nodeType,node.nodeValue)
  if (level>1 && node.childNodes){
    for (var i=0;i<node.childNodes.length;i++){
      dumpNodeInfo(node.childNodes[i],level-1,heading+" ")
    }
  }
}
processXml(process.argv[2])
