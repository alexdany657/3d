const canvas = document.getElementById("cnvs");
const gl = canvas.getContext("webgl");

var vsSource = "";
var fsSource = "";
var squareRotation = 0.0;
var then = 0;

const objUrl = "sasha.obj";
const mtlUrl = "sasha.mtl";
const bmpUrl = "sasha.bmp";
