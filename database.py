from google.appengine.ext import ndb

class Post(ndb.Model):
    post_title = ndb.StringProperty(required = True)
    post_content = ndb.TextProperty(required = True)
    post_author = ndb.StringProperty(required = True)
    post_created = ndb.DateTimeProperty(auto_now_add = True)
    post_last_updated = ndb.DateTimeProperty(auto_now = True)