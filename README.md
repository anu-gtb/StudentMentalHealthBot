# StudentMentalHealthBot

# Introduction
This project is a web application for students utilizing GPT-2 model developed for their basic mental health support and information. In this app, students can ask queries about anything that affects their mental health.

This app can also be used by visually disabled students as this app contains a feature of speech recognition and then bot responds with an audio for them. 

The objectives of the Project are:
1. Create an AI application for students with mental illnesses at their earliest point.
2. Allow student users to express and think about their emotions in a safe and anonymous way.
3. Provide guidance for addressing the most common mental health issues such as anxiety, stress and depression.

# Implementation Steps
1. Feeding GPT-2 model with relevant existing understanding-based on deep learning experience, about various forms of human psychological problems like marriages, career issues or family matters within a larger scope like frequently asked questions regarding general mental wellbeing.
2. Designing an API to offer a human interface by which human beings can seek solutions to their troubles.

# Description of main files
1. final_bot.csv - Dataset used for fine-tuning of gpt-2.

   Consists of 10,285 rows and 1 column containing answers to different mental health-related queries.

2. fine-tuning.ipynb - For fine-tuning of gpt-2 with suitable dataset.

   Tech-Stack used - Python libraries - PyTorch, transformers, gpt-2

3. generate.py - For backend development.

   Tech-Stack used - Python libraries - transformers

4. app.py - For UI/UX development.

   Tech-Stack used - Streamlit, speech_reecognition, gtts


![Screenshot (221)](https://github.com/user-attachments/assets/2a2bf8ae-d271-427c-995f-797a859acfe3)
![Screenshot (224)](https://github.com/user-attachments/assets/49636c74-a471-41d5-83ea-d74a878cf01c)
![Screenshot (223)](https://github.com/user-attachments/assets/fa52eee0-28d3-4bfb-b1ac-b8fe12de01d6)

Demo video of working of app - https://youtu.be/JBod6dgVG6Q?si=MMBN0mti8MAzqJ2m

For visually disabled students - https://youtu.be/afbp3AX8cjk?si=xd_fuSc8CsUS-z0g
