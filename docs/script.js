document.addEventListener('DOMContentLoaded', () => {
    // Navbar scroll effect
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Fade up animations on scroll (Intersection Observer)
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };
    
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-up').forEach(el => {
        observer.observe(el);
    });

    // Fullscreen toggle for dashboard
    const btnFullscreen = document.getElementById('btn-fullscreen');
    const glassContainer = document.getElementById('dashboard-container');
    
    if (btnFullscreen && glassContainer) {
        btnFullscreen.addEventListener('click', () => {
            const isFullscreen = glassContainer.classList.contains('fullscreen');
            
            if (!isFullscreen) {
                glassContainer.classList.add('fullscreen');
                document.body.classList.add('is-fullscreen');
                btnFullscreen.innerHTML = '<i class="fas fa-compress"></i> Exit Fullscreen';
            } else {
                glassContainer.classList.remove('fullscreen');
                document.body.classList.remove('is-fullscreen');
                btnFullscreen.innerHTML = '<i class="fas fa-expand"></i> Fullscreen';
                
                // Scroll back to dashboard if we lost position
                document.getElementById('dashboard').scrollIntoView({ behavior: 'auto' });
            }
        });
    }
});
