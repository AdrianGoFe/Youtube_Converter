import pytube

link_youtube = input("Introduzca el enlace de YouTube que desee descargar, por favor: \n")

video_download = pytube.YouTube(link_youtube)
video_download.streams.filter(progressive=True, file_extension='mp4', resolution="720p").first().download()
print("Video descargado con éxito", link_youtube)