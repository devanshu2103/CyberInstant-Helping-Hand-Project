from django.core.management.base import BaseCommand
from charity.models import Cause, Event, News

class Command(BaseCommand):
    help = 'Seed initial data for Causes, Events, and News'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Cause.objects.all().delete()
        Event.objects.all().delete()
        News.objects.all().delete()

        # Create sample Causes
        Cause.objects.create(
            title='Clean Water Initiative',
            description='Providing clean water to communities in need.',
            is_active=True,
            icon='fas fa-tint'
        )
        Cause.objects.create(
            title='Education for All',
            description='Supporting education for underprivileged children.',
            is_active=True,
            icon='fas fa-book'
        )
        Cause.objects.create(
            title='Healthcare Access',
            description='Improving healthcare facilities in rural areas.',
            is_active=True,
            icon='fas fa-heartbeat'
        )

        # Create sample Events
        Event.objects.create(
            title='Charity Run 2024',
            description='Annual charity run to raise funds for education.',
            date='2024-09-15',
            location='Central Park',
        )
        Event.objects.create(
            title='Health Camp',
            description='Free health checkup camp for local communities.',
            date='2024-10-10',
            location='Community Center',
        )

        # Create sample News
        News.objects.create(
            title='Successful Fundraiser',
            content='We successfully raised funds for the clean water project.',
            author='Admin',
            date='2024-05-01',
        )
        News.objects.create(
            title='New School Built',
            content='A new school has been built in the rural area.',
            author='Admin',
            date='2024-06-15',
        )

        self.stdout.write(self.style.SUCCESS('Sample data seeded successfully.'))
