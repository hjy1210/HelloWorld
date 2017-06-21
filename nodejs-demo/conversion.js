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

/*json2xml("d:\\work\\data\\sat2_chi_2016_01.json","d:\\work\\data\\sat2_chi_2016_01.xml")
json2xml("d:\\work\\data\\sat2_chi_2016_02.json","d:\\work\\data\\sat2_chi_2016_02.xml")
json2xml("d:\\work\\data\\sat2_eng_2016_01.json","d:\\work\\data\\sat2_eng_2016_01.xml")
json2xml("d:\\work\\data\\sat2_eng_2016_02.json","d:\\work\\data\\sat2_eng_2016_02.xml")
json2xml("d:\\work\\data\\sat2_eng_2016_36_37.json","d:\\work\\data\\sat2_eng_2016_36_37.xml")
json2xml("d:\\work\\data\\sat2_eng_2016_21_30.json","d:\\work\\data\\sat2_eng_2016_21_30.xml")
json2xml("d:\\work\\data\\sat2_his_2016_01.json","d:\\work\\data\\sat2_his_2016_01.xml")
json2xml("d:\\work\\data\\sat2_his_2016_02.json","d:\\work\\data\\sat2_his_2016_02.xml")
json2xml("d:\\work\\data\\sat2_his_2016_03.json","d:\\work\\data\\sat2_his_2016_03.xml")
json2xml("d:\\work\\data\\sat2_mathb_2016_01.json","d:\\work\\data\\sat2_mathb_2016_01.xml")
json2xml("d:\\work\\data\\sat2_mathb_2016_02.json","d:\\work\\data\\sat2_mathb_2016_02.xml")
json2xml("d:\\work\\data\\sat2_mathb_2016_A.json","d:\\work\\data\\sat2_mathb_2016_A.xml")
json2xml("d:\\work\\data\\sat2_mathb_2016_B.json","d:\\work\\data\\sat2_mathb_2016_B.xml")
json2xml("d:\\work\\data\\sat2_geo_2016_02\\sat2_geo_2016_02.json","d:\\work\\data\\sat2_geo_2016_02\\sat2_geo_2016_02.xml")
json2xml("d:\\work\\data\\sat2_geo_2016_04\\sat2_geo_2016_04.json","d:\\work\\data\\sat2_geo_2016_04\\sat2_geo_2016_04.xml")
json2xml("d:\\work\\data\\telc_sample_1\\telc_sample_1.json","d:\\work\\data\\telc_sample_1\\telc_sample_1.xml")
json2xml("d:\\work\\data\\telc_sample_2\\telc_sample_2.json","d:\\work\\data\\telc_sample_2\\telc_sample_2.xml")*/

//json2xml(process.argv[2],process.argv[3])
xml2json(process.argv[2],process.argv[3])

//node conversion.js sat2_chm_2016_02.xml sat2_chm_2016_02.json