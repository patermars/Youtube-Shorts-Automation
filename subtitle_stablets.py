import stable_whisper


def generate_srt_file(model_name: str, audio_path: str, output_file: str = 'output.srt') -> None:
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
        
        # Transcribe the audio file
        result = model.transcribe(audio_path)

        # Save the transcription to an SRT file
        result.to_srt_vtt(output_file, segment_level=False, word_level=True)

        print(f"{output_file}: SRT file generated successfully!")

    except Exception as e:
        print(f"An error occurred during transcription: {e}")

def main():
    # Example usage
    model_name = 'base.en'  # Example model name
    audio_path = 'story.mp3'  # Example audio file path
    output_file = 'story.srt'  # Example output file name

    # Generate SRT file
    generate_srt_file(model_name, audio_path, output_file)

if __name__ == "__main__":
    main()
    
