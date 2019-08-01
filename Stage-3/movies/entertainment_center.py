import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", 
						"https://amandawinter.files.wordpress.com/2010/10/600full-toy-story-poster.jpg", 
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet", 
					 "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg", 
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

hansel_and_gretel = media.Movie("Joao e Maria", "Hansel & Gretel are bounty hunters who track and kill witches all over the world.",
					"http://www.impawards.com/2013/posters/hansel_and_gretel_witch_hunters_ver6.jpg",
					"https://www.youtube.com/watch?v=9246msCh7x4")

lord_of_rings = media.Movie("Lord of Rings", "A ring that needs to be destroyed",
							"http://www.movieartarena.com/imgs/lotr1final.jpg",
							"https://www.youtube.com/watch?v=Pki6jbSbXIY")

harry_potter = media.Movie("Harry Potter", "An orphan who discovers he is a wizard",
							"https://s-media-cache-ak0.pinimg.com/originals/1e/c1/b0/1ec1b00ab251d99ad708a361058b52d8.jpg",
							"https://www.youtube.com/watch?v=eKSB0gXl9dw")

ice_age = media.Movie("Ice Age", "A Comedy about three good friends",
					  "http://vignette4.wikia.nocookie.net/iceage/images/9/94/Ice_Age_Original_Poster.jpg/revision/latest?cb=20100512224000",
					  "https://www.youtube.com/watch?v=cMfeWyVBidk")

movies = [toy_story, avatar, hansel_and_gretel, lord_of_rings, harry_potter, ice_age]

"""
Behavior: Calls a fresh_tomatoes function
Input: Receive a list with the movies variables names
Output: Open a Web Browser with the fresh tomatoes interface
"""
fresh_tomatoes.open_movies_page(movies)