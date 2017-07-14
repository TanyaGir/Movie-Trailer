'''imports the webrowser file to make it
   available to use within the current file'''
import webbrowser


# data structure called Movie is created
class Movie():

        ''' creates the __init__ function which initializes the variables
            of the data structure'''
        def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube):
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube

        ''' creates a function called show_trailer that opens the trailer
            of the movie in a new browser'''
        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
