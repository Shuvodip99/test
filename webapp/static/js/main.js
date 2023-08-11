```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    const postForm = document.querySelector('#post-form');
    const postInput = document.querySelector('#post-input');
    const postContainer = document.querySelector('#post-container');

    postForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const postText = postInput.value.trim();
        if (postText) {
            createPost(postText);
            postInput.value = '';
        }
    });

    function createPost(text) {
        const postElement = document.createElement('div');
        postElement.classList.add('post');
        postElement.textContent = text;
        postContainer.prepend(postElement);
    }
});
```