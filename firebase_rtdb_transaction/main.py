import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def increment_count(val):
    """ Increments the value by 1. """
    return val + 1


def rtdb_transaction(event, context):
    """ Attempts a transaction to update the value of the counter, incrementing it by 1. """

    # Function's runtime environment service account has the predefined Firebase Admin role
    cred = credentials.ApplicationDefault()

    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'MY_FIREBASE_RTDB_URL'
        })
    else:
        firebase_admin.get_app()

    # As an admin, the app has access to read and write all data, regardless of Security Rules
    ref = db.reference('counter')

    ref.transaction(increment_count)
    print('Transaction completed')

    return 'New value: ' + str(ref.get())
