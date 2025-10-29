function showProfile() {
    const profile = document.getElementById('profiles');
    const overlay = document.getElementById('profileOverlay');
    
    if (profile && overlay) {
        profile.classList.add('show');
        overlay.classList.add('show');
        document.body.style.overflow = 'hidden';
    } else {
        console.error('Profile elements not found');
    }
}

function hideProfile() {
    const profile = document.getElementById('profiles');
    const overlay = document.getElementById('profileOverlay');
    
    if (profile && overlay) {
        profile.classList.remove('show');
        overlay.classList.remove('show');
        document.body.style.overflow = 'auto';
    }
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    // Escape key to close
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            hideProfile();
        }
    });
    
    // Click outside to close
    document.addEventListener('click', function(event) {
        const overlay = document.getElementById('profileOverlay');
        if (event.target === overlay) {
            hideProfile();
        }
    });
});