# components/subcomponents/image_bounded.py

from components.htmlTags import HTMLContaining, HTMLSimple
from components.base import ComponentBase
import json
import os

from components.subcomponents.passage_list_001 import PassageList001


class ArticleBody001(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__,
            ["article_body_001"]
        )
        file_path = os.path.join(
            os.path.dirname(__file__),
            "..\\..\\database\\articles\\en_la_disciplina_e_instruccion_del_senor.json"
            # "../../database/articles/en_la_disciplina_e_instruccion_del_senor.json"
        )
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                articleContent = json.load(file)
                article_instance = Article(**articleContent)
                for idea in article_instance.ideas:
                    self.addComponent(
                        self,ComponentBase(HTMLContaining.H2, "article_body_heading","article_body_heading",{},
                        idea.heading, 
                    ))
                    for subidea in idea.subideas:
                        if subidea.type == "regular" or subidea.type == None:                      
                            self.addComponent(
                                self,ComponentBase(HTMLContaining.P, "article_body_001_subidea","article_body_001",{},
                                subidea.content,
                            ))
                        elif subidea.type == "passage_list":                      
                            self.addComponent(self,PassageList001(subidea.content))
                        else:                      
                            self.addComponent(
                                self,ComponentBase(HTMLContaining.P, "article_body_001_biblical_passage","article_body_001_biblical_passage",{},
                                subidea.content,
                            ))
        except FileNotFoundError:
            print(f"Error: The file at {file_path} was not found.")
        except json.JSONDecodeError:
            print("Error: The file is not a valid JSON format.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        
class Subidea:
    def __init__(self, content, subidea_type = ""):
        self.content = content
        if subidea_type is None or subidea_type == "":
            self.type = "regular"
        else:
            self.type = subidea_type

class Idea:
    def __init__(self, heading, subideas):
        self.heading = heading
        self.subideas = [Subidea(**s) for s in subideas]

class Article:
    def __init__(self, title, ideas):
        self.title = title
        self.ideas = [Idea(**i) for i in ideas]