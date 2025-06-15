document.addEventListener('DOMContentLoaded', () => {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function sendPost(url, productId, callback) {
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: new URLSearchParams({ product_id: productId })
        })
            .then(resp => resp.json())
            .then(callback)
            .catch(err => console.error('Request failed', err));
    }

    document.querySelectorAll('.add-to-cart').forEach(btn => {
        btn.addEventListener('click', e => {
            e.preventDefault();
            const id = btn.dataset.id;
            sendPost('/products/add-to-cart/', id, data => {
                if (data.success) {
                    alert('Added to cart');
                }
            });
        });
    });

    document.querySelectorAll('.add-to-wishlist').forEach(btn => {
        btn.addEventListener('click', e => {
            e.preventDefault();
            const id = btn.dataset.id;
            sendPost('/products/add-to-wishlist/', id, data => {
                if (data.success) {
                    alert('Added to wishlist');
                }
            });
        });
    });
});
