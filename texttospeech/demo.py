from gtts import gTTS
import os

def obtain_file_path(file_name):
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'texttospeech', 'data', file_name)
    return file_path

text = '''There was an idea, to bring together a group of remarkable people. To see, if they could become something more.
        To help people, so when they needed us, we could fight a battles that they never could'''

output = gTTS(text=text, lang='en' , slow=False)
file_path = obtain_file_path('output.mp3')
os.makedirs(os.path.dirname(file_path), exist_ok=True)
output.save(file_path)

# starting audio
os.system(f"start {file_path}")
