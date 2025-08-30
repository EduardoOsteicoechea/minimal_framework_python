const article_body = document.getElementById("PageArticle001_ArticleBody001");

fetch("https://eduardoos.com/static/json/en_la_disciplina_e_instruccion_del_senor.json")
    .then(response => {
        // Check if the response was successful
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Parse the JSON data from the response
        return response.json();
    })
    .then(data => {
        // Use the parsed JSON data to update the element's innerHTML
        // You'll need to decide how to format this data for display.
        // For example, displaying the title:
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
        // Handle any errors that occurred during the fetch
        console.error('There was a problem with the fetch operation:', error);
        article_body.innerHTML = `<p>Error loading content.</p>`; 
    });