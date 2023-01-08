var vid = document.querySelectorAll('video')

vid.forEach(play => play.addEventListener('dblclick', () =>{
    play.classList.toggle('active');

    if(play.paused){
        play.play();
    }
    else{
        play.pause();
    }
}));
