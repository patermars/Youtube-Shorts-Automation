import stable_whisper

# GitHub Links:
# openai-whisper: https://github.com/openai/whisper
# stable-whisper: https://github.com/jianfch/stable-whisper


def generate_srt_file(model_name: str, text_path:str, audio_path: str, output_file: str = 'output.srt') -> None:
    """
    Transcribes an audio file and generates an SRT file.

    Args:
        model_name (str): The name of the model to be loaded.
        audio_path (str): The path to the audio file to be transcribed.
        output_file (str): The name of the output SRT file.

    Returns:
        None
    """
    try:
        # Load the specified model
        model = stable_whisper.load_model(model_name)

        # Reading our story file
        with open(text_path, 'r') as file:
            text = file.read()
        
        # Aligning the audio file
        result = model.align(audio_path, text, language='en')  #aligning the audio as we already have the text so we dont really need to transcribe and spend unneccessary compute power

        # Save the transcription to an SRT file
        result.to_srt_vtt(output_file, segment_level=False, word_level=True)  #if you want to display 1 word at a time, use this
        # result.to_srt_vtt(output_file, segment_level=False, word_level=True)  #if you want to display whole sentence at a time, use this
        # result.to_srt_vtt(output_file, segment_level=False, word_level=True)  #if you want to display whole sentence but highlight the word being spoken, use this

        print(f"{output_file}: SRT file generated successfully!")

    except Exception as e:
        print(f"An error occurred during transcription: {e}")

def main():
    # Example usage
    model_name = 'base.en'  # Example model name
    text_path = 'story.txt' # Example story file name
    audio_path = 'story.mp3'  # Example audio file path
    output_file = 'story.srt'  # Example output file name

    # Generate SRT file
    generate_srt_file(model_name, text_path, audio_path, output_file)

if __name__ == "__main__":
    main()
    
