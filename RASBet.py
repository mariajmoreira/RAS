from app import create_app,db

db.create_all(app=create_app('default'))
app = create_app('default')

if __name__ == '__main__':
    app.run(debug=True)