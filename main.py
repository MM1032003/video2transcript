import speech_recognition as sr
import moviepy.editor as mp
from googletrans import Translator
import os, time

translate   = input('Do You Want To Translate To Arabic ? (Y/N) : ').lower()

while translate not in ['y', 'yes', 'n', 'no']:
    translate   = input('Do You Want To Translate To Arabic ? (Y/N) : ').lower()


if translate in ['y', 'yes']:
    translate   = True
else:
    translate   = False


dir_files           = os.listdir()
video_extentions    = ['mp4', 'mov', 'wmv', 'flv', 'avi', 'avchd', 'webm', 'mkv']
for file in dir_files:

    file_name, file_extention   = os.path.splitext(file)
    file_extention              = file_extention.strip('.')

    if file_extention in video_extentions:

        print(f'Processing {file}')
        time.sleep(2.5)

        sr_obj              = sr.Recognizer()
        video_clip_obj      = mp.VideoFileClip(file)
        audio               = sr.AudioFile(f"{file_name}.wav")

        print(f"Creating The Audio File {file_name}.wav")
        time.sleep(2.5)

        video_clip_obj.audio.write_audiofile(f"{file_name}.wav")

        with audio as source:
            audio_file  = sr_obj.record(source)

        result  = sr_obj.recognize_google(audio_file)
        translator_obj  = Translator(service_urls=['translate.google.com'])

        with open(f"{file_name}.txt", 'w') as audio_txt:

            print(f'Writing Down The Text in {file_name}.txt')
            time.sleep(2.5)

            audio_txt.write(result)
            if translate:

                print(f"Translating....")
                time.sleep(2.5)

                audio_txt.write("\n"+ "#"*80 + '\n')
                audio_txt.write(translator_obj.translate(result, src='en', dest='ar').text)

        video_clip_obj.close()

        print(f"Removing {file_name}.wav")
        time.sleep(2.5)

        os.remove(f'{file_name}.wav')

        print(f"{file} is done")
        print('#' * 80)
        
