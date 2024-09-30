from openai import OpenAI
import os
client = OpenAI(api_key= os.environ.get('OPEN_AI_KEY'))

def transcribe_audio_whisper(client, audio_file, prompt=None, model = "whisper-1", response_format="text", timestamp_granularities=["word"]):
  return client.audio.transcriptions.create(
    file=audio_file,
    prompt = prompt,
    model=model,
    response_format=response_format,
    timestamp_granularities=timestamp_granularities
  )

def generate_corrected_transcript(temperature, system_prompt, audio_file):
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": transcribe(audio_file, "")
            }
        ]
    )
    return response.choices[0].message.content


