document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            if (typeof bootstrap !== 'undefined') {
                var bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }
        });
    }, 5000);

    var logoutLinks = document.querySelectorAll('a[href*="logout"]');
    logoutLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            if (!confirm('Вы уверены, что хотите выйти?')) {
                e.preventDefault();
            }
        });
    });
});
// Плавное появление элементов
document.addEventListener('DOMContentLoaded', function() {
    // Анимация появления карточек
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            card.style.transition = 'opacity 0.5s, transform 0.5s';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
    
    // Анимация кнопок
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(btn => {
        btn.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
        });
        btn.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
});