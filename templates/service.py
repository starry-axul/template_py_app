from templates.repository import TemplateRepository

class TemplateService:
    def __init__(self):
        self.repository = TemplateRepository()
    
    def get_templates(self):
        return self.repository.get_templates()

    def get_template(self, id):
        return self.repository.get_template(id)

    def create_template(self, title, type, version, body, placeholders):
        pholders = ','.join(placeholders)
        return self.repository.create_template(title, type, version, body, pholders)