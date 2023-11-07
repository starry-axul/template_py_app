from templates.repository import TemplateRepository

class TemplateService:
    def __init__(self):
        self.repository = TemplateRepository()
    
    def get_templates(self, cluster=""):
        return self.repository.get_templates(cluster)

    def get_template(self, id):
        return self.repository.get_template(id)

    def create_template(self, cluster, type, version, body, placeholders):
        pholders = ','.join(placeholders)


        return self.repository.create_template(cluster, type, version, body, pholders)