const canvas = document.getElementById("cnvs");
const gl = canvas.getContext("webgl");

const vertexShader = "glsl_shaders/VertexShader.glsl";
const fragmentShader = "glsl_shaders/FragmentShader.glsl";

var vsSource = "";
var fsSource = "";
var squareRotation = 0.0;
var then = 0;

var rot = 1;

var sasha = true;

var objUrl = "";
var pngUrl = "";
var ZFar = 0;

if (sasha) {
    var ZFar = -2000.0;
    var objUrl = "objects/sasha/sasha_20000.obj";
    var pngUrl = "objects/sasha/sasha_0.png";
} else {
    var ZFar = -6.0;
    var objUrl = "objects/cube/cube.obj";
    var pngUrl = "objects/cube/cube_1.png";
}
