# Author     : Fedya Serafiev
# Version    : 1.1
# License    : MIT
# Copyright  : Fedya Serafiev (2023)
# Github     : https://github.com/cezar4o/youtube-downloader
# Contact    : https://urocibg.eu/

from pytube import YouTube
import os
def download_mp3(url, destination='.'):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file
def main():
    print("Добре дошли в youtube-downloader!")
    while True:
        url = input("\nВъведете URL адреса на видеоклипа, който искате да изтеглите "
                    "(или въведете 'exit' за изход):\n>> ")
        
        if url.lower() == 'exit':
            break
        destination = input("Въведете дестинацията (оставете празно за текущата директория):\n>> ") or '.'
        download_mp3(url, destination)
        print("Файлът е изтеглен успешно.")
if __name__ == "__main__":
    main()
