let progress = document.getElementById('progg');
        let total = document.body.scrollHeight - window.innerHeight;

        window.onscroll = function(){
            let proghght = (window.pageYOffset / total)*100;
            progress.style.height = proghght +"%";
        }