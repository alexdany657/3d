async function setVsSource(url) {
    vsSource = await (await load(url)).text();
}

async function setFsSource(url) {
    fsSource = await (await load(url)).text();
}

async function load(url) {
    resp = await fetch(url);
    return resp;
}

async function loadMesh() {
    //objSource = await (await load(objUrl)).text();
    //mtlSource = await (await load(mtlUrl)).text();
    // bmpSource = await (await load(bmpUrl)).text();

    mesh = await (await fetch(objUrl, {method: "post"})).json()
    window.vCount = mesh.f.length;
    console.log(vCount);
    //console.log(mesh);

    //console.log(mesh.fn.length);

    window.texture = loadTexture(gl, pngUrl);

    window.buff = createGeometry(gl, mesh);

    //parseOBJ();
}
