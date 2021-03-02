import lyricsgenius
from googletrans import Translator
translator = Translator()


def cleanup(lyric:str):
    cleaned_lyrics = ""
    out_lyrics = lyric.splitlines(False)

    for line in  out_lyrics:
        if "[" in line or '\n' in line:
            print("Drop: " + line)
            next 
        else:
            print("Keep: " + line)
            cleaned_lyrics  += line + '\n'
            next

    return cleaned_lyrics



def Transmify(clyric:str,lang_list:list):
    temp_ly = clyric
    for lang in lang_list:
        temp_ly = Translate_to(temp_ly,lang)
    return temp_ly



def Translate_to(ablyric:str,lang:str):
    out = translator.translate(ablyric,lang)
    return out



song_input = input("Song:")
artist = input("Artist:")
artist = artist.upper()
genius_token = 'fECdK0XOaoB6S_yRqa6VZZnWFPddCMm1Gf4-7sLPW5JPBg8Y9rvgDZoWBc1XjMnF'
lang_codes = ['afrikaans','albanian','amharic','arabic','armenian','azerbaijani','basque','belarusian','bengali','bosnian','bulgarian','catalan','ceb''cebuano','chichewa','chinese(simplified)','chinese(traditional)','corsican','croatian','czech','danish','dutch','esperanto','english']
lang_avail = lang_codes.count

genius = lyricsgenius.Genius(genius_token)
if artist != "NA":
    song = genius.search_song(song_input,artist)
else:
    song = genius.search_song(song_input)

    
lyrics = song.lyrics
print("Here are the unmodified lyrics:\n" + lyrics)
print("\nDoing some cleaning up before Transmifying.")
pretty_lyrics = cleanup(lyrics)
print("Lyric cleanup successfull!\n" + pretty_lyrics)
print("Now is where we work the Transmifying magic!")
final_magic = Transmify(pretty_lyrics,lang_codes)
print("And the Emmy Goes to:\n\n\n\n"+ final_magic)

        
    







