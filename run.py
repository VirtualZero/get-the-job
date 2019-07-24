from get_the_job import app

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
        threaded=True
    )
