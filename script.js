/**
 * Astia Wireframe Prototype Script
 * Shared script for navigation and interaction simulation.
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Smooth Scroll for internal anchor links (FAQ categories, etc.)
  const anchorLinks = document.querySelectorAll('a[href^="#"]:not([href="#"])');
  anchorLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href');
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        const headerHeight = document.querySelector('.site-header')?.offsetHeight || 80;
        const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight - 20;
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // 2. Form submission simulation
  const contactForm = document.getElementById('wireframe-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      alert('【ワイヤーフレーム確認用シミュレーション】\n\n送信ボタンが押されました。実際のサイトではここでお問い合わせ完了画面（Thanksページ）へ遷移または送信完了メッセージが表示されます。');
    });
  }

  // 3. Highlight current page in global navigation
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.global-nav a');
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
});
