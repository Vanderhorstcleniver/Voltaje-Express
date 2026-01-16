// Elementos del DOM para el menú
const mobileMenu = document.querySelector('.mobile-menu');
const navUl = document.querySelector('nav ul');
const navLinks = document.querySelectorAll('nav a');
const header = document.querySelector('header');

// Menú móvil - toggle
mobileMenu.addEventListener('click', () => {
    navUl.classList.toggle('active');
    mobileMenu.textContent = navUl.classList.contains('active') ? '✕' : '☰';
});

// Cerrar menú móvil al hacer clic en un enlace
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (window.innerWidth <= 768) {
            navUl.classList.remove('active');
            mobileMenu.textContent = '☰';
        }
    });
});

// Scroll suave para enlaces internos
navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
        // Solo aplicar a enlaces que sean hashes (enlaces internos)
        if (this.getAttribute('href').startsWith('#')) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                const headerHeight = header.offsetHeight;
                const targetPosition = targetSection.offsetTop - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        }
    });
});

// Cambiar estilo del header al hacer scroll
function handleScroll() {
    if (window.scrollY > 100) {
        header.style.backgroundColor = 'rgba(13, 13, 13, 0.95)';
        header.style.backdropFilter = 'blur(10px)';
    } else {
        header.style.backgroundColor = '';
        header.style.backdropFilter = '';
    }
}

// Resaltar enlace activo según la sección visible
function highlightActiveLink() {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('nav a[href^="#"]');

    let currentSection = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        const headerHeight = header.offsetHeight;

        if (window.scrollY >= (sectionTop - headerHeight - 100)) {
            currentSection = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${currentSection}`) {
            link.classList.add('active');
        }
    });
}

// Cerrar menú al hacer clic fuera de él
document.addEventListener('click', (e) => {
    if (window.innerWidth <= 768) {
        const isClickInsideNav = navUl.contains(e.target) || mobileMenu.contains(e.target);

        if (!isClickInsideNav && navUl.classList.contains('active')) {
            navUl.classList.remove('active');
            mobileMenu.textContent = '☰';
        }
    }
});

// Manejar redimensionamiento de ventana
window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
        navUl.classList.remove('active');
        mobileMenu.textContent = '☰';
    }
});

// Agregar estilos CSS para el enlace activo
const style = document.createElement('style');
style.textContent = `
    nav a.active {
        color: var(--electric-yellow) !important;
    }
    
    nav a.active::after {
        width: 100% !important;
    }
    
    header {
        transition: all 0.3s ease;
    }
`;
document.head.appendChild(style);

// Event listeners
window.addEventListener('scroll', () => {
    handleScroll();
    highlightActiveLink();
});

// Inicialización al cargar la página
window.addEventListener('DOMContentLoaded', () => {
    handleScroll();
    highlightActiveLink();
});