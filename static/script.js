const video = document.getElementById('video');
const photoInput = document.getElementById('photoInput');

function startCamera() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: { facingMode: "user", width: 320, height: 240 } })
            .then(stream => {
                video.srcObject = stream;
                video.play();
            })
            .catch(err => {
                alert('Tidak dapat mengakses kamera: ' + err);
            });
    } else {
        alert('Browser tidak mendukung akses kamera.');
    }
}

function capturePhotoBeforeSubmit() {
    const canvas = document.createElement('canvas');
    canvas.width = 320;
    canvas.height = 240;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const dataURL = canvas.toDataURL('image/png');
    photoInput.value = dataURL;
    return true;
}

window.onload = startCamera;
