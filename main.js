function update() {
    1;
}

async function main() {

    const canvas = document.getElementById("cnvs");

    const gl = canvas.getContext("webgl");

    gl.clearColor(0.0, 0.0, 0.0, 1.0);

    gl.clear(gl.COLOR_BUFFER_BIT);

    await setVsSource("VertexShader.glsl");
    await setFsSource("FragmentShader.glsl");

    console.log(vsSource);
    console.log(fsSource);

    const shaderProgram = initShader(gl, vsSource, fsSource);

    const programInfo = {
        program: shaderProgram,
        attribLocations: {
            vertexPosition: gl.getAttribLocation(shaderProgram, 'aVertexPosition'),
        },
        uniformLocations: {
            projectionMatrix: gl.getUniformLocation(shaderProgram, 'uProjectionMatrix'),
            modelViewMatrix: gl.getUniformLocation(shaderProgram, 'uModelViewMatrix'),
        },
    };

    console.log(shaderProgram);
}

main();
