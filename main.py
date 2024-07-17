import random
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from voiceover_elevenlabs import text_to_speech_file
from subtitle_stablets import generate_srt_file

# GitHub Links:
# openai-whisper: https://github.com/openai/whisper
# stable-whisper: https://github.com/jianfch/stable-whisper
# moviepy: https://github.com/Zulko/moviepy
# elevenlabs API: https://github.com/elevenlabs/elevenlabs-python

def subtitle_generator(txt: str) -> TextClip:
    """
    Generates a subtitle text clip.

    Args:
        txt (str): The subtitle text.

    Returns:
        TextClip: The generated text clip.
    """
    return TextClip(txt, font='FiraSans-Ultra', fontsize=130, color='white', stroke_color='black', stroke_width=4.5)

def create_audio_from_text(file_path: str, voice_id: str, output_name: str) -> str:
    """
    Reads text from a file, converts it to speech, and saves the audio file.

    Args:
        file_path (str): Path to the text file.
        voice_id (str): Voice ID for text-to-speech conversion.
        output_name (str): Output audio file name (without extension).

    Returns:
        str: Path to the saved audio file.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        audio_path = text_to_speech_file(text, voice_id, output_name)
        print(f"Audio saved at: {audio_path}")
        return audio_path
    except Exception as e:
        print(f"An error occurred while creating audio: {e}")
        return ""

def generate_final_video(heading_audio_path: str ,story_audio_path: str, subtitle_path: str,gameplay_video_path: str = 'gameplay.mp4',output_file: str = 'final.mp4') -> None:
    """
    Generates the final video with the given components.

    Args:
        gameplay_video_path (str): Path to the gameplay video.
        heading_audio_path (str): Path to the heading audio file.
        story_audio_path (str): Path to the story audio file.
        subtitle_path (str): Path to the subtitle file.
        output_file (str): Output video file name.

    Returns:
        None
    """
    try:
        audio1 = AudioFileClip(heading_audio_path)
        audio2 = AudioFileClip(story_audio_path)

        video = VideoFileClip(gameplay_video_path)

        v_start = round(random.uniform(0.00, video.duration - (audio1.duration + audio2.duration)), 2)
        video = video.subclip(v_start, v_start + (audio1.duration + audio2.duration))

        new_width = 1080
        new_height = 1920

        resized_clip = video.resize(height=new_height)
        video = resized_clip.crop(x_center=resized_clip.w / 2, width=new_width, y_center=resized_clip.h / 2, height=new_height)

        heading_image = ImageClip("heading.png").set_duration(audio1.duration).set_position("center")

        mixed_audio = CompositeAudioClip([audio1, audio2.set_start(audio1.duration + 2)])

        subtitles = SubtitlesClip(subtitle_path, subtitle_generator).set_position('center').set_start(audio1.duration + 2)

        video.audio = mixed_audio

        final_video = CompositeVideoClip([video, heading_image, subtitles])

        final_video.write_videofile(output_file, fps=video.fps, threads=4)
        print(f"Final video saved at: {output_file}")

    except Exception as e:
        print(f"An error occurred while generating the video: {e}")

def main():

    # Create heading audio
    heading_audio_path = create_audio_from_text(heading_txt_path, heading_voice_id, heading_audio_name)

    # Create story audio
    story_audio_path = create_audio_from_text(story_txt_path, story_voice_id, story_audio_name)

    # Generate story subtitle file
    generate_srt_file(subtitle_model, story_audio_path, subtitle_output_file)

    # Generate final video
    generate_final_video(gameplay_video_path, heading_audio_path, story_audio_path, subtitle_output_file, final_output_file)


if __name__ == "__main__":
    # Define file paths and parameters
    heading_txt_path = 'heading.txt'
    story_txt_path = 'story.txt'
    gameplay_video_path = 'gameplay.mp4'
    heading_voice_id = "ohiRYqXiLWMhtwmxSKao"
    story_voice_id = "ohiRYqXiLWMhtwmxSKao"
    heading_audio_name = "heading"
    story_audio_name = "story"
    subtitle_model = "base.en"
    subtitle_output_file = "story.srt"
    final_output_file = "final.mp4"
    main()