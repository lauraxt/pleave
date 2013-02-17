INSTALL & RUN
=============

You'll need sqlite to be installed locally.

Run these commands:

    virtualenv ~/venvs/pleave
    source ~/venvs/pleave/bin/activate
    pip install -r requirements.txt

    cp config.py.dist config.py
    # edit config.py to your liking!
    export PLEAVE_SETTINGS=config.py

    python start_db.py ## to initialize the sqlite database

    python pleave.py ## To start the flask app
