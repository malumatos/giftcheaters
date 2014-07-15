import webapp2
import os

from google.appengine.ext.webapp import template

class BaseHandler(webapp2.RequestHandler):
  def render_template(self, filename, template_args=None):
        path = os.path.join(os.path.dirname(__file__), 'views', filename)
        self.response.write(template.render(path, template_args))


class Index(BaseHandler):
	def get(self):
		# self.response.headers['Content-Type'] = 'text/plain'	
		# self.response.out.write('Hello, WebApp World!')
		self.render_template('index.html', {})

class Dashboard(BaseHandler):
	# @require_login
	def get(self):
		self.render_template('dashboard.html', {})
	
class Facebook_signin(BaseHandler):
	def get(self):
		self.render_template('facebook_signin.html', {})
	
app = webapp2.WSGIApplication([
	#nav
    ('/', Index),
    ('/dashboard', Dashboard),
	('/facebook_signin', Facebook_signin),
	], debug=True)
	