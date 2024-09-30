def transcribe_audio_whisper(client, audio_file, prompt=None, model = "whisper-1", response_format="verbose_json", timestamp_granularities=["word"]):
  if response_format == "text":
    return client.audio.transcriptions.create(
    model=model, 
    file=audio_file, 
    response_format=response_format,
    prompt=prompt,
    )
  else:
    return client.audio.transcriptions.create(
    file=audio_file,
    model=model,
    response_format=response_format,
    timestamp_granularities=timestamp_granularities,
    prompt = prompt
    )

def generate_corrected_transcript(client, temperature, system_prompt, audio_file=None, audio_text=None):
    user_content = audio_text if audio_text else transcribe_audio_whisper(client, audio_file)
    
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
                "content": user_content
            }
        ]
    )
    return response.choices[0].message.content



