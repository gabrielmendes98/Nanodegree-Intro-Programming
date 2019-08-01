import webbrowser

class Movie():
	""" This class provides a way to store movie related information"""

	"""
	Behavior: This function creates a space in memory to save the movies information
	Input: It receives the movie variable name, its title, storyline, poster image and youtube trailer
	"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_storyline
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	"""
	Behavior: It takes a 'webbrowser function and transform in a 'media' function
	Input: It receives the movie variable name
	Output: Plays the respective movie trailer using a webbrowser function
	"""
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)