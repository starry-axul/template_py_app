from templates.repository import TemplateRepository

class TemplateService:
    def __init__(self):
        self.repository = TemplateRepository()
    
    def get_templates(self):
        return self.repository.get_templates()

    def create_template(self, title, body, placeholders):
        pholders = ','.join(placeholders)
        return self.repository.create_template(title, body, pholders)