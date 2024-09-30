import os

def read_audio_file(file_path):
   return open(file_path, "rb")

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

def generate_corrected_transcript(client, temperature, system_prompt, model ="gpt-4o-mini", audio_file=None, audio_text=None):
    user_content = audio_text if audio_text else transcribe_audio_whisper(client, audio_file)
    
    response = client.chat.completions.create(
        model=model,
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

def write_to_file(directory_path, file_name, content):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    
    file_path = os.path.join(directory_path, file_name)
    
    with open(file_path, "w") as file:
        file.write(content)
    
    print(f"File '{file_name}' has been written to '{directory_path}'.")

def summarize_transcript_open_ai(client, transcript, model = "gpt-4o-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant who is an expert in summarizing transcripts"},
            {"role": "user", "content": "Please summarize the following transcript: "},
            {"role": "user", "content": transcript}
        ]
    )
    return response.choices[0].message.content

def summarize_transcript_hugging_face(summarizer, transcript, max_length=200, min_length=30, do_sample=False):
   return summarizer(transcript, max_length=max_length, min_length=min_length, do_sample=do_sample)[0]['summary_text']
   
    




