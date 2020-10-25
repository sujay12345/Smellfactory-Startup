document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.likelink').forEach(link => {
        link.onclick = function() {
            const postid = this.dataset.postid
            const like = document.querySelector(`#span${postid}`);
            fetch(`/like/${postid}`);

            if (this.innerHTML === 'Upvote') {
                this.innerHTML = 'Remove Upvote';
                like.innerHTML = parseInt(like.innerHTML) + 1;
            } else {
                this.innerHTML = 'Upvote';
                like.innerHTML = parseInt(like.innerHTML) - 1;
            }
        };
    });

    document.querySelector('#submit').disabled = true;

    // Enable button only if there is text in the input field
    document.querySelector('#task').onkeyup = () => {
        if (document.querySelector('#task').value.length > 0)
            document.querySelector('#submit').disabled = false;
        else
            document.querySelector('#submit').disabled = true;
    };


});


