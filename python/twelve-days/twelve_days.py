start_verse_dict = {1: "first",
                    2: "second",
                    3: "third",
                    4: "fourth",
                    5: "fifth",
                    6: "sixth",
                    7: "seventh",
                    8: "eighth",
                    9: "ninth",
                    10: "tenth",
                    11: "eleventh",
                    12: "twelfth"}
    
end_verse_dict = {2: "two Turtle Doves",
                  3: "three French Hens",
                  4: "four Calling Birds",
                  5: "five Gold Rings",
                  6: "six Geese-a-Laying",
                  7: "seven Swans-a-Swimming",
                  8: "eight Maids-a-Milking",
                  9: "nine Ladies Dancing",
                  10: "ten Lords-a-Leaping",
                  11: "eleven Pipers Piping",
                  12: "twelve Drummers Drumming"}

def recite(start_verse, end_verse):

    song = f'On the {start_verse_dict[start_verse]} day of Christmas my true love gave to me: '

    if start_verse > 1:
        for i in range(start_verse, 1, -1):
            song += end_verse_dict[i]
            song += ", " if i > 2 else ", and "
    last_verse = "a Partridge in a Pear Tree."
    song += last_verse
    complete_song = [song]

    if start_verse < end_verse:
        for i in range(start_verse, end_verse):
            complete_song += recite(i+1, i+1)

    return complete_song


