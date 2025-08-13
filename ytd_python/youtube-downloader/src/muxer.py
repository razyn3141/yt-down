import ffmpeg

class Muxer:
    def mux(self, video_file, audio_file, output_file):
        video = ffmpeg.input(video_file)
        audio = ffmpeg.input(audio_file)
        (
            ffmpeg
            .output(video, audio, output_file, vcodec='libx264', acodec='aac', strict='experimental')
            .run(overwrite_output=True)
        )