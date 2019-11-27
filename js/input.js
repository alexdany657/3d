function onMouseDown(event){
    controller.isMouseDown = 1;
    controller.lastX = event.x;
    controller.lastY = event.y;
}

function onMouseUp(event){
    controller.isMouseDown = 0;
    controller.lastX = event.x;
    controller.lastY = event.y;
}

function onMouseMove(event){
    if (window.controller.lastX == -1){
        window.controller.lastX = event.x;
    }
    if (window.controller.lastY == -1){
        window.controller.lastY = event.y;
    }
    if (!window.controller.isMouseDown){
        return;
    }
    var dx = event.x - window.controller.lastX;
    var dy = event.y - window.controller.lastY;
    window.controller.rotY += window.controller.sensivity * dx;
    window.controller.rotX += window.controller.sensivity * dy;
    window.controller.lastX = event.x;
    window.controller.lastY = event.y;
}

function onMouseEnter(event){
    window.controller.isOver = 1;
}

function onMouseLeave(event){
    window.controller.isOver = 0;
    onMouseUp(event);
}

/*function scrollHandler(event){
    var cScroll = window.pageYOffset;
    //console.log(cScroll - window.controller.defaultScroll);
    window.controller.zDist -= cScroll - window.controller.defaultScroll;
    window.scrollTo(0, window.controller.defaultScroll);
}*/

function wheelHandler(event){
    window.controller.zDist -= event.deltaY;
}

canvas.onmousedown = onMouseDown;
canvas.onmouseup = onMouseUp;
canvas.onmousemove = onMouseMove;
canvas.onmouseleave = onMouseLeave;
canvas.onmouseenter = onMouseEnter;
canvas.addEventListener("wheel", wheelHandler);
