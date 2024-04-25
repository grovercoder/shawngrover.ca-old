// Simple object to organize the Hero Rotator logic
const HeroRotator = {
    currentIndex: 0,
    rotateInterval: 15000,      // 15 seconds
    heroContents: [],
    intervalTimer: null,

    // clear the active and fadeIn classes from all hero content items
    clear: () => {
        HeroRotator.heroContents.forEach(item => {
            item.classList.remove('active', 'fadeIn')
        })
    },

    // clear the fadeIn only from all hero content items
    // (fadeIn should only last for 1 second)
    clearFade: () => {
        HeroRotator.heroContents.forEach(item => {
            item.classList.remove('fadeIn')
        })
    },

    // show the specified hero content item
    show: (target) => {
        // sanity checks
        if (isNaN(target)) { target = 0 }
        if (target < 0 ) { target = HeroRotator.heroContents.length -1 }
        if (target >= HeroRotator.heroContents.length) { target = 0 }

        // get node reference
        const content = HeroRotator.heroContents[target]
        if (content) {
            // display the node
            HeroRotator.currentIndex = target
            HeroRotator.clear()
            content.classList.add('active', 'fadeIn')
            setTimeout(HeroRotator.clearFade, 1000)
        }
    },

    // show the next hero content node
    next: () => {
        HeroRotator.show(HeroRotator.currentIndex + 1)
    },

    // show the previous item, restarting the timer so the full interval period is used
    previous: () => {
        // set the desired index back 2 because next() adds one automatically
        HeroRotator.currentIndex = HeroRotator.currentIndex - 2
        // show the item
        HeroRotator.next()

        // reset the interval
        clearInterval(HeroRotator.intervalTimer)
        HeroRotator.intervalTimer = setInterval(HeroRotator.next, HeroRotator.rotateInterval)
    },

    // start the rotation process
    begin: () => {
        // find the hero content items that are available right now
        HeroRotator.heroContents = document.querySelectorAll('.hero-content')
        // reset the index to start at the beginning of the list
        HeroRotator.currentIndex = -1;     // the rotate method adds one automatically

        // show the first item
        HeroRotator.next()

        // start the interval timer
        HeroRotator.intervalTimer = setInterval(HeroRotator.next, HeroRotator.rotateInterval);
    }
}

// Simple object to organize the navigation logic
const NavController = {
    icon: null,
    overlay: null,

    init: () => {
        NavController.icon = document.querySelector('.burger')
        NavController.overlay = document.querySelector('.overlay-content')

        // Add event handlers
        NavController.icon?.addEventListener('click', NavController.toggleNav)
        NavController.overlay?.addEventListener('click', NavController.hideNav)
    },

    toggleNav: () => {
        NavController.icon?.classList.toggle('active')
        NavController.overlay?.classList.toggle('active')
    },

    hideNav: () => {
        NavController.icon?.classList.remove('active')
        NavController.overlay?.classList.remove('active')
    }
}

// ------------------------------------------------
// Initialize the page when everything is loaded
// ------------------------------------------------
document.addEventListener("DOMContentLoaded", function() {
    // start the hero banner rotation
    HeroRotator.begin()

    // Initialize the navigation controller
    NavController.init()    
});
