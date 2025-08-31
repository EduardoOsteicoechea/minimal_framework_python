const PageArticle001_ArticleTitle001 = document.getElementById("PageArticle001_ArticleTitle001");
const ArticleTitle001_article_title_heading = document.getElementById("ArticleTitle001_article_title_heading");
const PageArticle001_ArticleBody001 = document.getElementById("PageArticle001_ArticleBody001");
const ArticleTitle001_reload_article_button = document.getElementById("ArticleTitle001_reload_article_button");
const webUrl = "static/json/una_autentica_relacion_cristo.json";

ArticleTitle001_reload_article_button.addEventListener('click',()=>{
    PageArticle001_ArticleBody001.innerHTML = "Reloading"
    setTimeout(()=>{
        reloadArticle(webUrl)
    },100)
})

setTimeout(()=>{
    reloadArticle(webUrl)
},100)

function reloadArticle(url){
    console.log(`loading from ${url}`)
    fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        ArticleTitle001_article_title_heading.innerHTML = data.title;
        
        let htmlContent = ""; 
        data.ideas.forEach(idea => {
            htmlContent += `<h2>${idea.heading}</h2>`;
            idea.subideas.forEach(subidea => {
                htmlContent += `<p>${subidea.content}</p>`;
            });
        });
        PageArticle001_ArticleBody001.innerHTML = htmlContent;
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        PageArticle001_ArticleBody001.innerHTML = `<p>Error loading content.</p>`; 
    });
}
