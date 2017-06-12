var express = require('express');
var router = express.Router();
var path=require('path')

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

/* try erercise dump error */
router.get('/comments/:message', function(req,res,next){
  if (req.params.message==="1"){
    res.sendFile(path.join(__dirname, '../public/images/Mia20161013.jpg'));
  } else {
    var error=new Error("not found!!!")
    console.log(error.stack)
    error.status=404
    next(error)
  }
})

router.get('/image/:message', function(req,res,next){
  var url='/comments/'+req.params.message
  //console.log(url)
  res.render('image',{message:req.params.message,url:url})
})

module.exports = router;
