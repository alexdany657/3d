async function main1() {
    await setVsSource(vertexShader);
    await setFsSource(fragmentShader);
    await loadMesh();
    start(vsSource, fsSource);
}

function start(vsSource, fsSource) {

    gl.clearColor(0.0, 0.0, 0.0, 1.0);

    gl.clear(gl.COLOR_BUFFER_BIT);

    const shaderProgram = initShader(gl, vsSource, fsSource);

    window.programInfo = {
        program: shaderProgram,
        attribLocations: {
            vertexPosition: gl.getAttribLocation(shaderProgram, 'aVertexPosition'),
            vertexColor: gl.getAttribLocation(shaderProgram, 'aVertexColor'),
        },
        uniformLocations: {
            projectionMatrix: gl.getUniformLocation(shaderProgram, 'uProjectionMatrix'),
            modelViewMatrix: gl.getUniformLocation(shaderProgram, 'uModelViewMatrix'),
        },
    };

    window.buff = createGeometry(gl);

    requestAnimationFrame(render);
}

main1();
