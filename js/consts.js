const canvas = document.getElementById("cnvs");
const gl = canvas.getContext("webgl");

const vertexShader = "glsl_shaders/VertexShader.glsl";
const fragmentShader = "glsl_shaders/FragmentShader.glsl";

var vsSource = "";
var fsSource = "";
var squareRotation = 0.0;
var then = 0;

const objUrl = "objects/sasha/sasha.obj";
const mtlUrl = "objects/sasha/sasha.mtl";
const bmpUrl = "objects/sasha/sasha.bmp";
const pngUrl = "objects/sasha/sasha_0.png";
