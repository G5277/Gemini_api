function captionImage() {
    var imageInput = document.getElementById('imageInput');
    var captionDiv = document.getElementById('caption');

    if (imageInput.files.length > 0) {
        var file = imageInput.files[0];
        var reader = new FileReader();

        reader.onload = function(e) {
            var img = new Image();
            img.src = e.target.result;

            img.onload = function() {
                var formData = new FormData();
                formData.append('image', file);

                $.ajax({
                    type: 'POST',
                    url: '/caption',
                    data: formData,
                    processData: false,
                    contentType: true,
                    success: function(response) {
                        captionDiv.textContent = response.caption;
                    },
                    error: function(error) {
                        console.error('Error: hello', error);
                    }
                });
            };
        };

        reader.readAsDataURL(file);
    }
}
