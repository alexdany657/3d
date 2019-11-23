const canvas = document.getElementById("cnvs");
const gl = canvas.getContext("webgl");

const vertexShader = "glsl_shaders/VertexShader.glsl";
const fragmentShader = "glsl_shaders/FragmentShader.glsl";

var vsSource = "";
var fsSource = "";
var squareRotation = 0.0;
var then = 0;

var rot = 1;

var flag = "sasha_20k";

var objUrl = "";
var pngUrl = "";
var ZFar = 0;

if (flag == "sasha_20k") {
    ZFar = -2000.0;
    objUrl = "objects/sasha/sasha_20000.obj";
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
