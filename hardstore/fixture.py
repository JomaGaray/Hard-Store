import json
from market.models import Category

with open('mock-data.json', 'r') as fp:
    data = json.load(fp)

for c in data['category']:
  
    print('Nombre de categoria: ' + c['name'])

    e = Category(id=c['id'],name=c['name'])

    e.save()

    print('Categoria guardada...')
    
for p in data['product']:
  
    print('Nombre del producto: ' + p['name'])

    e = Category(id=p['id'],name=p['name'])

    e.save()

    print('Categoria guardada...')
    