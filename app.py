import streamlit as  st
from generate import generate_text
import speech_recognition as sr
from gtts import gTTS

model_path='C:\\Users\\DELL\\Documents\\HACK_CONCLAVE\\model'

st.set_page_config('Student Mental Health Center')

st.title("Let's Talk it out:wink:")

st.write('This is your mental health assistant:robot_face:')

st.write('Share your problem below :')

prompt=st.text_area('Enter your query')

ask=st.button('Submit')

if ask:
    if prompt=='':
        st.write('Please, ask a valid question!')
    else:
        prompt=prompt.lower()
        if prompt=='hi' or prompt=='hey' or prompt=='hello' or prompt=='i need help' or prompt=='is anybody there':
            st.write('Hello! Tell me your problem:slightly_smiling_face:')
        elif prompt=='thank you' or prompt=='thank u' or prompt=='thanku' or prompt=='thanks' or prompt=='thank you so much' or prompt=='thank u so much' or prompt=='got it':
            st.write('Thanks for visiting.All the best!:slightly_smiling_face:')
        else:
            ans=generate_text(model_path,prompt)
            st.write('Ans : ',ans)
        
st.write('OR')

speak=st.button('Speak query:microphone:')

def record():
    rec=sr.Recognizer()
    with sr.Microphone() as mic:
        st.write('Listening...')
        audio=rec.listen(mic)
    try:
        prompt=rec.recognize_google(audio)
        speech=gTTS(text='You said'+prompt,lang='en',slow=False)
        speech.save('audio.mp3')
        st.audio('audio.mp3')
        st.text_input('You said :',value=prompt)
        if prompt=='hi' or prompt=='hey' or prompt=='hello' or prompt=='i need help' or prompt=='is anybody there':
            speech=gTTS(text='Hello! Tell me your problem',lang='en',slow=False)
            speech.save('audio.mp3')
            st.audio('audio.mp3')
            st.write('Hello! Tell me your problem:slightly_smiling_face:')
        else:
            answer=generate_text(model_path,prompt)
            speech=gTTS(text=answer,lang='en',slow=False)
            speech.save('audio.mp3')
            st.audio('audio.mp3')
            st.write(answer)
    except sr.UnknownValueError:
        speech=gTTS(text='Speak again',lang='en',slow=False)
        speech.save('audio.mp3')
        st.audio('audio.mp3')
        st.error('Speak again!')
    except sr.RequestError as re:
        st.error(re)

if speak:
    record()
