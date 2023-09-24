from templates.models import Template

class TemplateRepository:
    def get_templates(self):
        return Template.objects.all()
    
    def get_template(self, id):
        return Template.objects.get(id=id)

    def create_template(self, title, body, placeholders):
        tmp = Template.objects.create(
            title=title,
            body=body,
            placeholders=placeholders,
        )
        return tmp
