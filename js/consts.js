const canvas = document.getElementById("cnvs");
const gl = canvas.getContext("webgl");

const vertexShader = "glsl_shaders/VertexShader.glsl";
const fragmentShader = "glsl_shaders/FragmentShader.glsl";

var vsSource = "";
var fsSource = "";
var squareRotation = 0.0;
var then = 0;

var ZFar = -2000.0;
//var ZFar = -6.0;

const objUrl = "objects/sasha/sasha_20000.obj";
//const objUrl = "objects/cube/cube.obj";
const mtlUrl = "objects/sasha/sasha.mtl";
const bmpUrl = "objects/sasha/sasha.bmp";
const pngUrl = "objects/sasha/sasha_0.png";
//const pngUrl = "objects/cube/cube_0.png";
