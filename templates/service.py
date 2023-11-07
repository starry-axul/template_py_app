from templates.repository import TemplateRepository
from .responses import BadRequestExcep

class TemplateService:
    def __init__(self):
        self.repository = TemplateRepository()
    
    def get_templates(self, cluster, type, version):
        return self.repository.get_templates(cluster, type, version)

    def get_template(self, id):
        return self.repository.get_template(id)

    def create_template(self, cluster, type, version, body, placeholders):
        pholders = ','.join(placeholders)

        template = self.repository.get_templates(cluster, type, version)

        if template.exists():
            raise BadRequestExcep(f"there is a templates with the values: cluster={cluster}, type={type}, version={version}")


        return self.repository.create_template(cluster, type, version, body, pholders)