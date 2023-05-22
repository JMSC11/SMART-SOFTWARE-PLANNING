
 const btnEliminar = document.querySelectorAll(".btnEliminar");
  btnEliminar.forEach(btn => {
    btn.addEventListener("click", e => {
      const confirmacion = confirm("¿Deseas eliminar el registro?");
      if (!confirmacion) {
        e.preventDefault();
      }
    });
  });



var $ = jQuery.noConflict();

function abrir_modal_tabla_pf_ldc(url){
    $('#edicion_tabla_pf_ldc').load(url, function(){
        $(this).modal('show');
    });
}

function abrir_modal_multiplicador(url){
    $('#edicion_multiplicador').load(url, function(){
        $(this).modal('show');
    });
}

function abrir_modal_preguntas(url){
    $('#edicion_preguntas').load(url, function(){
        $(this).modal('show');
    });
}


function abrir_modal_edicion(url){
    $('#edicion_proyecto').load(url, function(){
        $(this).modal('show');
    });
}

function abrir_modal_edicion_funcional(url){
    $('#edicion_funcional').load(url, function(){
        $(this).modal('show');
    });
}

function abrir_modal_edicion_no_funcional(url){
    $('#edicion_no_funcional').load(url, function(){
        $(this).modal('show');
    });
}

function abrir_modal_edicion_aspectos(url){
    $('#edicion_aspectos').load(url, function(){
        $(this).modal('show');
    });
}

function drag(event) {
  event.dataTransfer.setData("text", event.target.innerText);
}

function drop1(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  document.getElementById("input1").value = data;
}

function drop2(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  document.getElementById("input2").value = data;
}
function drop3(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  document.getElementById("input3").value = data;
}
function drop4(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  document.getElementById("input4").value = data;
}
function drop5(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  document.getElementById("input5").value = data;
}
function drop6(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  document.getElementById("input6").value = data;
}
function drop7(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  document.getElementById("input7").value = data;
}
function drop8(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  document.getElementById("input8").value = data;
}
function drop9(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  document.getElementById("input9").value = data;
}
function drop10(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  document.getElementById("input10").value = data;
}
function drop11(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  document.getElementById("input11").value = data;
}
function drop12(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  document.getElementById("input12").value = data;
}
function drop13(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  document.getElementById("input13").value = data;
}
function drop14(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  document.getElementById("input14").value = data;
}
function allowDrop(event) {
  event.preventDefault();
}

