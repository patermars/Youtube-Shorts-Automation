from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

# Initialize ElevenLabs client with your API key
client = ElevenLabs(api_key="YOUR_API_KEY_HERE")


def text_to_speech_file(text: str, voice_id: str, file_name: str) -> str:
    """
    Converts text to speech and saves it as an MP3 file.

    Args:
        text (str): The text to be converted to speech.
        voice_id (str): The ID of the voice to be used.
        file_name (str): The name of the output file (without extension).

    Returns:
        str: The path to the saved audio file.
    """
    try:
        # Call the text-to-speech conversion API with detailed parameters
        response = client.text_to_speech.convert(
            voice_id=voice_id,
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2",
            voice_settings=VoiceSettings(
                stability=0.5,
                similarity_boost=0.75,
                style=0.0,
                use_speaker_boost=True,
            ),
        )

        # Define the path for the output MP3 file
        file_path = f"{file_name}.mp3"

        # Write the audio to the file
        with open(file_path, "wb") as audio_file:
            for chunk in response:
                if chunk:
                    audio_file.write(chunk)

        print(f"{file_path}: Audio file saved successfully!")
        return file_path

    except Exception as e:
        print(f"An error occurred during text-to-speech conversion: {e}")
        return ""

def main():
    # Example usage
    text = "Your text here"
    voice_id = "21m00Tcm4TlvDq8ikWAM"  # Example voice ID
    file_name = "output_audio"

    # Convert text to speech and save the file
    saved_file_path = text_to_speech_file(text, voice_id, file_name)
    if saved_file_path:
        print(f"File saved at: {saved_file_path}")



if __name__ == "__main__":
    main()

