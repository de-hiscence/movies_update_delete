
import mysql.connector
db = mysql.connector.connect(user = "root",
                                password = "M1krokosmos!2223",
                                host = "localhost",
                                database = "movies",
                                raise_on_warnings = True
    )
    # function for cursor
cursor = db.cursor()
def show_films(cursor, title):

        # method to execute an inner join on all tables,
        # iterate over the dataset and output the results to the terminal window
        # inner join query
        
        cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name'\
            FROM film INNER JOIN genre ON \
            film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id")
            
        # get the results from the cursor object
        films = (cursor.fetchall())
        print("\n -- {} -- ".format(title))   
        # iterate over the film data set and display results
        for film in films:
            print("\nFilm Name: {} \n Director: {}\n Genre Name ID: {} \n Studio Name: {} \n".format(film[0], film[1], film[2], film[3]))
        
show_films(cursor, "DISPLAYING FILMS")
# INSERT
cursor.execute("""INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director,studio_id, genre_id) \
    VALUES ("Avatar: The Way of Water", 2022, 180, "James Cameron",1, 2)""")
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# UPDATE
cursor.execute("""UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'""")
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE-Change Alien to Horror")
        
# DELETE
cursor.execute("""DELETE from film WHERE film_name = 'Gladiator'""")
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")
    
