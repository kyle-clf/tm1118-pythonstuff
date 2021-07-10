from .models import VenueEvent
import json
import pandas as pd

#Reset table
VenueEvent.objects.all().delete()

print('Reading data from Excel')
df = pd.read_excel('Venue-Event.xlsx', skiprows=1)

for i in range(df.shape[0]):
    data = df.iloc[i]
    p = VenueEvent(venue=data['Venue'], date=data['Date'], timeStart=data['Time start'], timeEnd=data['Time end'], event=data['Event'], instructor=data['Instructor'])
    p.save()

print('Finishing reading data from Excel')
