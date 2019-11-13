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
