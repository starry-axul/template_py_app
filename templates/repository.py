from templates.models import Template

class TemplateRepository:
    def get_templates(self):
        return Template.objects.all()
    
    def get_template(self, id):
        return Template.objects.get(id=id)

    def create_template(self, title,type, version, body, placeholders):
        tmp = Template.objects.create(
            title=title,
            type=type, 
            version=version,
            body=body,
            placeholders=placeholders,
        )
        return tmp
