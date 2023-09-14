document.addEventListener("DOMContentLoaded", function () {
    const downloadButton = document.getElementById("downloadButton");
    const videoLinkInput = document.getElementById("videoLink");
    const resolutionInput = document.getElementById("resolution");
    const mp3Checkbox = document.getElementById("mp3Checkbox");
    const downloadStatus = document.getElementById("downloadStatus");

    downloadButton.addEventListener("click", function () {
        const videoLink = videoLinkInput.value;
        const resolution = resolutionInput.value;
        const isMp3 = mp3Checkbox.checked;

        if (videoLink) {
            downloadStatus.innerText = "Downloading...";
            downloadStatus.style.color = "black";

            fetch("/download", {
                method: "POST",
                body: JSON.stringify({ link: videoLink, resolution: resolution, is_mp3: isMp3 }),
                headers: {
                    "Content-Type": "application/json",
                },
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.success) {
                        downloadStatus.innerText = isMp3 ? "Audio downloaded successfully!" : "Video downloaded successfully!";
                        downloadStatus.style.color = "green";
                    } else {
                        downloadStatus.innerText = data.error;
                        downloadStatus.style.color = "red";
                    }
                })
                .catch((error) => {
                    downloadStatus.innerText = "An error occurred while downloading.";
                    downloadStatus.style.color = "red";
                });
        } else {
            downloadStatus.innerText = "Please enter a valid YouTube video URL.";
            downloadStatus.style.color = "red";
        }
    });
});
