import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
import django

django.setup()

# FAKE POP SCRIPT
import random
from first_app.models import AccessRecord, Webpage, Topic,User
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Market', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        # Create user with the generated attributes

        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]
        user.save()
        # get the topic for entry
        top = add_topic()

        # create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create access record for that page
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]




if __name__ == '__main__':
    print("Populating Scripts")
    populate(20)
    print("Database has been populated")
