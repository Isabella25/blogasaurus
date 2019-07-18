import webapp2
import jinja2
import os



the_jinja_enviroment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# Remember, you can get this by searching for jinja2 google app engine

class HomePage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_enviroment.get_template("blog.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('Hey yall welcome to my ted talk')
        self.response.write(template.render())


class DogPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('This is my puppy Charlie')

class FriendsPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("These are my friends!")

# Route mapping
app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', HomePage),
    ('/dog', DogPage),
    ('/friends', FriendsPage) #maps '/predict' to the FortuneHandler
], debug=True)
