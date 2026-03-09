document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.presentation-container');
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const indicatorsContainer = document.getElementById('indicators');

    let currentSlide = 0;
    const totalSlides = slides.length;

    // Build indicators
    for (let i = 0; i < totalSlides; i++) {
        const dot = document.createElement('div');
        dot.classList.add('indicator');
        if (i === 0) dot.classList.add('active');
        dot.addEventListener('click', () => goToSlide(i));
        indicatorsContainer.appendChild(dot);
    }
    const indicators = document.querySelectorAll('.indicator');

    function updateSlides() {
        container.style.transform = `translateX(-${currentSlide * 100}vw)`;
        slides.forEach((slide, index) => {
            slide.classList.toggle('active', index === currentSlide);
            if (index === currentSlide) slide.scrollTop = 0;
        });
        indicators.forEach((ind, index) => {
            ind.classList.toggle('active', index === currentSlide);
        });
        prevBtn.disabled = currentSlide === 0;
        nextBtn.disabled = currentSlide === totalSlides - 1;
    }

    function goToSlide(index) {
        if (index >= 0 && index < totalSlides) {
            currentSlide = index;
            updateSlides();
        }
    }

    prevBtn.addEventListener('click', () => goToSlide(currentSlide - 1));
    nextBtn.addEventListener('click', () => goToSlide(currentSlide + 1));

    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === ' ') goToSlide(currentSlide + 1);
        else if (e.key === 'ArrowLeft') goToSlide(currentSlide - 1);
    });

    let touchStartX = 0;
    document.addEventListener('touchstart', e => { touchStartX = e.changedTouches[0].screenX; }, false);
    document.addEventListener('touchend', e => {
        const diff = e.changedTouches[0].screenX - touchStartX;
        if (Math.abs(diff) > 50) goToSlide(currentSlide + (diff < 0 ? 1 : -1));
    }, false);

    // ─── Itinerary Map Logic ────────────────────────────────────────────────
    const mapIframe = document.getElementById('map-iframe');
    const mapLabel = document.getElementById('map-label');

    // Fixed overview: Ho Chi Minh City, zoom 13. Always use this as the base.
    const HCMC_OVERVIEW = 'https://maps.google.com/maps?q=Ho+Chi+Minh+City+Vietnam&output=embed&z=13';

    // Google Maps directions URLs for each day (open in new tab — NOT embeddable)
    const dayRouteLinks = {
        'day-1-list': 'https://www.google.com/maps/dir/Tan+Son+Nhat+International+Airport,+HCMC/Le+Corto+Restaurant,+HCMC/Saigon+Central+Post+Office,+HCMC/Miu+Miu+Spa,+HCMC/Banh+Mi+Huynh+Hoa,+HCMC',
        'day-2-list': 'https://www.google.com/maps/dir/Signature+by+M+Village+Hai+Ba+Trung,+HCMC/The+Cafe+Apartment,+HCMC/Ho+Chi+Minh+City+Opera+House,+HCMC/Pizza+4Ps+Le+Thanh+Ton,+HCMC/Miu+Miu+Spa,+HCMC',
        'day-3-list': 'https://www.google.com/maps/dir/Tan+Dinh+Church,+HCMC/Cocotte+Restaurant,+HCMC/Saigon+Zoo+and+Botanical+Gardens,+HCMC/Miu+Miu+Spa+97+Vo+Van+Tan,+HCMC/Sol+Kitchen+Bar,+HCMC',
        'day-4-list': 'https://www.google.com/maps/dir/Signature+by+M+Village+Hai+Ba+Trung,+HCMC/War+Remnants+Museum,+HCMC/Ben+Thanh+Market,+HCMC/Nguyen+Hue+Walking+Street,+HCMC',
        'day-5-list': 'https://www.google.com/maps/dir/Signature+by+M+Village+Hai+Ba+Trung,+HCMC/Banh+Mi+Huynh+Hoa,+HCMC/Tan+Son+Nhat+International+Airport,+HCMC'
    };

    // Inject a "🗺️ 開啟路線" button into each day title
    document.querySelectorAll('.day-section').forEach(section => {
        const dayId = section.id;
        const routeUrl = dayRouteLinks[dayId];
        const titleEl = section.querySelector('.day-title');
        if (titleEl && routeUrl) {
            const btn = document.createElement('a');
            btn.href = routeUrl;
            btn.target = '_blank';
            btn.rel = 'noopener';
            btn.title = '在 Google Maps 中查看當日完整路線';
            btn.style.cssText = `
                display: inline-flex; align-items: center; gap: 0.3rem;
                margin-left: 0.75rem; padding: 0.2rem 0.7rem;
                background: var(--c-primary); color: white;
                border-radius: 100px; font-size: 0.75rem; font-weight: 700;
                text-decoration: none; vertical-align: middle;
                white-space: nowrap;
            `;
            btn.innerHTML = '🗺️ 開啟路線';
            titleEl.appendChild(btn);
        }
    });

    // Individual event card click → show that location pin in iframe (z=13 for context)
    const eventCards = document.querySelectorAll('.event-card[data-map-src]');
    eventCards.forEach(card => {
        card.style.cursor = 'pointer';
        card.addEventListener('click', () => {
            const newSrc = card.getAttribute('data-map-src');
            if (!newSrc || !mapIframe) return;
            eventCards.forEach(c => c.style.boxShadow = '');
            card.style.boxShadow = '0 0 0 3px var(--c-primary)';
            mapIframe.src = newSrc;
            if (mapLabel) {
                const h4 = card.querySelector('h4');
                mapLabel.textContent = h4 ? '📍 ' + h4.textContent.replace(/[\u{1F517}]/gu, '').trim() : '顯示地點';
            }
        });
    });

    // Initialize
    if (mapIframe) mapIframe.src = HCMC_OVERVIEW;
    if (mapLabel) mapLabel.textContent = '點擊左側行程查看地點，或按路線按鈕開啟全日路線';
    updateSlides();
});
