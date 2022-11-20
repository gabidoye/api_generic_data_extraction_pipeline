from flatten_json import flatten_json
import pandas as pd

json_obj = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
          'email': {
              'admission': 'admission@abc.com',
              'general': 'info@abc.com'
          },
          'tel': '123456789',
      }
    }
}

def flaten(data):
       

    if isinstance(data, dict):

        df = pd.DataFrame([flatten_json(data)])
        df.to_csv('new.csv', sep='\t')

    elif isinstance(data, list):
        df = pd.DataFrame([flatten_json(x) for x in data])
        df.to_csv('new.csv', sep='\t')

    return df

flaten(json_obj)