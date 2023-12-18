from django.core.management.base import BaseCommand, CommandParser
from geonode.base.models import ResourceBase


class Command(BaseCommand):
    help = "This command will count the resoruces available"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('resource_type', type=str)
        
    def handle(self, *args, **options):
        counter = ResourceBase.objects.filter(resource_type=options['resource_type']).count()
        self.stdout.write(self.style.SUCCESS(f"Total resource found: {counter}"))
