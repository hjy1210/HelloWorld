var parseString = require('xml2js').parseString;
var xml = "<root>Hello xml2js!</root>"
parseString(xml, function (err, result) {
    console.dir(result);
});

var fs=require('fs')
var xml2js=require('xml2js')
/*var obj = {name: "Super", Surname: "Man", age: 23};
var builder=new xml2js.Builder()
var xml=builder.buildObject(obj)
console.log(xml)*/

function json2xml(jsonfile, xmlfile){
  fs.readFile(jsonfile,'utf8',(err,data)=>{
    if (err) throw err
    var obj=JSON.parse(data)
    var builder=new xml2js.Builder()
    var xml=builder.buildObject(obj)
    fs.writeFile(xmlfile,xml,(err)=>{
      if (err) throw err
      console.log("done")
    })
  })
}

json2xml("d:\\work\\data\\sat2_chi_2016_01.json","d:\\work\\data\\sat2_chi_2016_01.xml")
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
json2xml("d:\\work\\data\\telc_sample_2\\telc_sample_2.json","d:\\work\\data\\telc_sample_2\\telc_sample_2.xml")
