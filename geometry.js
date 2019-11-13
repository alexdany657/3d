function createGeometry(gl) {
    const positionBuff = gl.createBuffer();

    gl.bindBuffer(gl.ARRAY_BUFFER, positionBuff);

    const pos = [
        -1.0,  1.0,
         1.0,  1.0,
        -1.0, -1.0,
         1.0, -1.0,
    ];

    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(pos), gl.STATIC_DRAW);
    return {position: positionBuff,};
}
