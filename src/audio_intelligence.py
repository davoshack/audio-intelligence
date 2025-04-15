from ai_custom_utils.helper import get_deepgram_api_key

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)


# Path to the audio file
AUDIO_FILE = "demo_english.mp3"

API_KEY = get_deepgram_api_key()

def main():
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(API_KEY)

        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        #STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
          	model="nova-3-general",
            sentiment=True,
            intents=True,
            summarize="v2",
            topics=True,
        )

        # STEP 3: Call the transcribe_file method with the audio payload and options
        response = deepgram.listen.rest.v("1").transcribe_file(payload, options)

        # STEP 4: Print the response
        print(response.to_json(indent=4))

        # STEP 5: Save the response to a JSON file
        with open("response.json", "w") as json_file:
            json_file.write(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()
