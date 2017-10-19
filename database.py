from google.appengine.ext import ndb

class Post(ndb.Model):
    post_title = ndb.StringProperty(required = True)
    post_content = ndb.TextProperty(required = True)
    post_author = ndb.StringProperty(required = True)
    post_created = ndb.DateTimeProperty(auto_now_add = True)
    post_last_updated = ndb.DateTimeProperty(auto_now = True)

     @classmethod
    def addPost(cls, title, content, author):
        p = Post(post_title = title, post_content = content,
                 post_author = author)
        p.put()
        return p.key.id()

    @classmethod
    def editPost(cls, title, content, author, post_id):
        post = Post.get_by_id(int(post_id))
        if post:
            if post.post_author == author:
                post.post_title = title
                post.post_content = content
                post.put()
                return post.key.id()