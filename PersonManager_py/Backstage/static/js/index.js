setInterval(function () {
  $('.time').html(getTime())
},1000)
function getTime() {
var date_obj=new Date();
var year=date_obj.getFullYear();
var month=date_obj.getMonth();
var day=date_obj.getDate();
var hour=date_obj.getHours();
var minute=date_obj.getMinutes();
var seconds=date_obj.getSeconds();
return year+"年"+month+"月"+day+"日"+hour+"时"+minute+"分"+seconds+"秒"
 }