import boto3

def text_to_speech(text, voice_id, output_file):
    polly_client = boto3.Session(
        aws_access_key_id='INGRESA TU ID DE AWS',
        aws_secret_access_key='INGRESA TU KEY SECRET DE AWS',
        region_name='us-west-2'
    ).client('polly')

    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId=voice_id
    )

    # Guardar el archivo de audio
    with open(output_file, 'wb') as file:
        file.write(response['AudioStream'].read())

if __name__ == "__main__":
    text = input("Ingrese el texto que desea convertir a voz: ")

    # Opciones de voces en español latino
    print("Seleccione una voz:")
    print("1. Lupe (Femenina)")
    print("2. Miguel (Masculina)")
    print("3. Penélope (Femenina)")

    choice = input("Ingrese el número de la voz que desea usar: ")

    if choice == '1':
        voice_id = 'Lupe'
    elif choice == '2':
        voice_id = 'Miguel'
    elif choice == '3':
        voice_id = 'Penelope'
    else:
        print("Selección no válida, se utilizará la voz por defecto (Lupe).")
        voice_id = 'Lupe'

    text_to_speech(text, voice_id, 'audio.mp3')
    print(f"Archivo de audio creado y guardado como audio.mp3 usando la voz {voice_id}.")
