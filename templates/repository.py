from templates.models import Template


class TemplateRepository:
    def get_templates(self, cluster, type, version):
        filter = {}
        if cluster is not None:
            filter['cluster'] = cluster

        if type is not None:
            filter['type'] = type

        if version is not None:
            filter['version'] = version

        return Template.objects.all().filter(**filter)

    def get_template(self, id):
        return Template.objects.get(id=id)

    def check_unique_values(self, cluster, type, version):
        pass

    def create_template(self, cluster, type, version, body, placeholders):
        tmp = Template.objects.create(
            cluster=cluster,
            type=type,
            version=version,
            body=body,
            placeholders=placeholders,
        )
        return tmp
