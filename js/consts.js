const canvas = document.getElementById("cnvs");

canvas.width = document.documentElement.clientHeight-20;
canvas.height = document.documentElement.clientHeight-20;

const gl = canvas.getContext("webgl");
const uint32Ext = gl.getExtension("OES_element_index_uint");

const vertexShader = "glsl_shaders/VertexShader.glsl";
const fragmentShader = "glsl_shaders/FragmentShader.glsl";

var fieldOfView = Math.PI / 4;
var aspect = 1;
var zNear = 0.1;
var zFar = 10000.0;

var vsSource = "";
var fsSource = "";
var squareRotation = 0.0;
var then = 0;

var rot = 1;

var flag = "cube";

var objUrl = "";
var pngUrl = "";
var ZFar = 0;

if (flag == "sasha") {
    ZFar = -2000.0;
    objUrl = "objects/sasha/sasha.obj";
    pngUrl = "objects/sasha/sasha_0.png";
} else if (flag == "sasha_50k") {
    ZFar = -2000.0;
    objUrl = "objects/sasha/sasha_50000.obj";
    pngUrl = "objects/sasha/sasha_0.png";
} else if (flag == "cube") {
    ZFar = -6.0;
    objUrl = "objects/cube/cube.obj";
    pngUrl = "objects/cube/cube_1.png";
} else {
    alert("Bad flag!");
}
