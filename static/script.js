// "Смотреть далее" баскычы үчүн функция
function toggleReviews() {
    const extraReviews = document.getElementById('extra-reviews');
    const button = document.querySelector('.btn-read-more');
    
    if (extraReviews) {
        if (extraReviews.classList.contains('all-reviews-hidden')) {
            // Ачуу
            extraReviews.classList.remove('all-reviews-hidden');
            extraReviews.classList.add('all-reviews-visible');
            button.textContent = 'Скрыть ↓';
        } else {
            // Жабуу
            extraReviews.classList.remove('all-reviews-visible');
            extraReviews.classList.add('all-reviews-hidden');
            button.textContent = 'Смотреть далее →';
            
            // Бетти жогору түшүрүү (комментарийлер башына)
            document.querySelector('.reviews-section').scrollIntoView({ 
                behavior: 'smooth' 
            });
        }
    }
}

// Модалдык терезени ачуу үчүн функция
document.addEventListener('DOMContentLoaded', function() {
    const modalOverlay = document.querySelector('.modal-overlay');
    const openButtons = document.querySelectorAll('.btn-open-modal');
    const closeButton = document.querySelector('.close-modal');
    
    // Модалды ачуу
    openButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            if (modalOverlay) {
                modalOverlay.style.display = 'flex';
                document.body.style.overflow = 'hidden';
            }
        });
    });
    
    // Модалды жабуу
    if (closeButton) {
        closeButton.addEventListener('click', function() {
            if (modalOverlay) {
                modalOverlay.style.display = 'none';
                document.body.style.overflow = 'auto';
            }
        });
    }
    
    // Терезеден тышкары басса жабуу
    if (modalOverlay) {
        modalOverlay.addEventListener('click', function(e) {
            if (e.target === modalOverlay) {
                modalOverlay.style.display = 'none';
                document.body.style.overflow = 'auto';
            }
        });
    }
});
