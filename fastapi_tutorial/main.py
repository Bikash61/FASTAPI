from fastapi import FastAPI

#Instance of FastAPI 

app = FastAPI()

@app.get('/')
def index():
    return {
        'data':{
            'name': 'Bikash',
            'class': 12
        }
    }


@app.get('/about')
def about():
    return {
        'date':{
            'About_us': "We are a person working on python,C++ and Javascript",
            'About_me': "I am a python developer"
        }
    }