import media
import fresh_tomatoes


#create list of movies to display in the HTML file
finding_dory = media.Movie("Finding Dory",
                        "The story about a fish with short term memory loss who sets out to find her parents",
                        "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
                        "https://www.youtube.com/watch?v=MKJA-VLpiCo")


beauty_and_the_beast = media.Movie("Beauty and the Beast",
                     "Story of a girl who falls in love with a beast",
                     "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                     "https://www.youtube.com/watch?v=e3Nl_TCQXuw")



finding_nemo = media.Movie("Finding Nemo",
                           "The story about how a lost fish finds his way back home",
                           "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")


zootopia = media.Movie("Zootopia",
                                "A story abou a bunny who sets out change what everyone thinks of her",
                                "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                                "https://www.youtube.com/watch?v=jWM0ct-OLsM")


ratatouille = media.Movie("Ratatouille",
                          "The story about a rat",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

kung_fu_panda = media.Movie ("Kung Fu Panda",
                 "The story about a Panda",
                 "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
                 "https://www.youtube.com/watch?v=PXi3Mv6KMzY")



#create a list of the instances created above
movies = [finding_dory, beauty_and_the_beast, finding_nemo, zootopia, ratatouille, kung_fu_panda]


#open_movies_page is a function in fresh_tomatoes.py that takes in one argument which is the list of movies
fresh_tomatoes.open_movies_page(movies)




