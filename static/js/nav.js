    'use strict';

    const navBtn = document.querySelector('.nav-btn');
    const openBtn = document.querySelector('.open-btn');
    const closeBtn = document.querySelector('.close-btn');
    const nav = document.querySelector('.nav');

    navBtn.addEventListener('click', function () {
        console.log("clicked")
        console.log(nav.classList)
        nav.classList.toggle('open');
    })

    // document.querySelector('main').addEventListener('click', function (e) {
    //     nav.classList.remove('open');
    // });

    // })