
function returnHome() {
    window.location.href = "/"
}

function capture() {
    windows.location.href = "/capture"
}

function runCam() {
    Webcam.set({
        width: 320,
        height: 240,
        image_format: 'jpeg',
        jpeg_quality: 90
    });
    Webcam.attach('#my_camera');
}