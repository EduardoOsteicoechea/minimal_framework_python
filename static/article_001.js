const article_body = document.getElementById("PageArticle001_ArticleBody001");

fetch("https://eduardoos.com/static/json/en_la_disciplina_e_instruccion_del_senor.json")
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        article_body.innerHTML = `<h1>${data.title}</h1>`;
        
        // Or to display all the content
        let htmlContent = `<h1>${data.title}</h1>`; 
        data.ideas.forEach(idea => {
            htmlContent += `<h2>${idea.heading}</h2>`;
            idea.subideas.forEach(subidea => {
                htmlContent += `<p>${subidea.content}</p>`;
            });
        });
        article_body.innerHTML = htmlContent;

    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        article_body.innerHTML = `<p>Error loading content.</p>`; 
    });