$(function () {
    bind_Ajax_yzm()
    bind_form_password()
})
function bind_Ajax_yzm() {
    $("#yz_Code").click(function () {
        $(this)[0].src+='?';
    })
}
function bind_form_password() {
    $(".tj").click(function () {
        var public_key=$("#public_key").html();
        var jsencrypt = new JSEncrypt();
        jsencrypt.setPublicKey(public_key);
        var password=jsencrypt.encrypt($("#password_look").val());
        $("#password_not_look")[0].value=password
    })
}
