import os 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django 
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()

for topic in topics:
    print(topic.id)
    print(topic)
    print(topic.date_added)



entries = t.set_entry.all()

for e in entries:
    print(e)