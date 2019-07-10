import os

from flaskr  import create_app

def main():
    app = create_app()
    app.run(host='0.0.0.0', port='5002')

if __name__ =='__main__':
    main()
