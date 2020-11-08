from flask import Flask

app=Flask(__name__)
@app.route('/')
def home():
    return 'Hello Gbenga ! My first website'
    
@app.route('/about')
def about():
    return 'The about page'
    
@app.route('/blog')
def blog():
    return 'This is the blog'
    
if __name__=='__main__':
    app.run()