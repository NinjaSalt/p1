# obtain user login information
def get_login():
    if auth.user:
        return auth.user.first_name + " " + auth.user.last_name
    else:
        return "Unknown User"

# obtain user id
def get_id():
    if auth.user:
        return auth.user.id
    else:
        return 0

# obtain user e-mail
def get_email():
    if auth.user:
        return auth.user.email
    else:
        return "Unknown User"


#define message layout
db.define_table('inbox_message',
    Field('author', default = get_email()),
    Field('title',unique = True),
    Field('description','text'),
    Field('receiver_username', requires=IS_IN_DB(db, 'auth_user.username', '%(username)s', zero='User')))

    # The following three fields could be useful later for accepting a person's Friend Code request an
    #Field('accepted','boolean'),
    #Field('complete','boolean'),
    #Field('rejected', 'boolean'),
