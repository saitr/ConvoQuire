$(document).ready(function() {
    $('.like-button').click(function() {
        const button = $(this);
        const postId = button.data('post-id');
        const likeUrl = button.data('like-url');

        $.ajax({
            type: 'POST',
            url: likeUrl,
            data: {
                'post_id': postId,
            },
            success: function(data) {
                // Update the like count for this specific post
                button.closest('.list-group-item').find('.like-count').html(data.like_count);
            },
            error: function() {
                console.log('Error occurred during the like operation.');
            }
        });
    });
});


