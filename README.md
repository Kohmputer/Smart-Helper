# Introduction
Smart Helper is EnableMe’s upcoming offer, aiming to harness AI to curate personalized
guidance for individuals navigating significant health challenges. It leverages EnableMe's
rich resources on various disabilities and chronic illnesses and seeks to intelligently integrate
information, services, and communities from across the world to provide comprehensive support.

Smart Helper offers its users relevant information at the right time in the preferred format. It
aims to assist them in not just coping with their new situation but thriving and reaching their
full potential, by also connecting them with wider communities and opportunties.

# The Objective of Smart Helper Chatbot
Develop an initial prototype for Smart Helper focused on diabetes management. This
prototype should cater to individuals newly diagnosed with diabetes, offering them precisely
the information they need, when they need it. The **goal** is to alleviate the overwhelm of
diagnosis, providing a personalized, interactive, and engaging experience. 

The Smart Helper should:

At *Stage 1* (now)
- Answer common questions related to diabetes.
- Offer personalized advice and information on diabetes management.
  
At *Stage 2*
- Connect users with community support and resources.
  
At *Stage 3*
- Provide reminders for medication, appointments, and glucose monitoring.

# User Flow & Architecture
![Untitled Diagram drawio](https://github.com/Kohmputer/Smart-Helper/assets/137958418/19b12cb0-6b82-4180-b6df-5cead1923ea5)




# Approach
1. Design the Chatbot
   - Ensure the chatbot UI is user-friendly and accessible to people with various disabilities.
   - This project is an Assistance Chatbot built using OpenAI's **GPT-3.5** and **Python**.

2. Bot Interaction (Conversation Flow)
“Welcome to Smart Helper!“ 👋
 - Chatbot: Hi HM, welcome back! How are you feeling today?
 - HM: Not that great.. I was diagnosed with Type-2 diabetes. 
 - Chatbot: I’m sorry to hear you’re not doing well today. It’s not always easy to discuss, but is there any way I can help?
 - HM: Not sure to be honest… 
 - Chatbot: No worries! Take your time. Let me know if you need anything. I can assist you with the following. 
 (Provide click options of: Connect me to the diabetes community. I’m anxious. I’m sad. Leave me alone)




# Prototype
<img width="1105" alt="Screenshot 2024-03-24 at 14 31 22" src="https://github.com/Kohmputer/Smart-Helper/assets/137958418/038e193f-b210-461f-bb37-026a13f92763">


# Room for Improvement + Next Steps
- **Integration with EnableMe’s Ecosystem**: Utilize EnableMe's existing resources by linking to articles, videos, and community forums relevant to the user's questions.
- **Personalization**: Enable the chatbot to suggest articles, connect users with community threads, or set up peer support sessions based on the conversation.
- **Testing & Iteration**:
  - Conduct thorough testing with a diverse group of users, including those newly diagnosed with diabetes and individuals with various disabilities.
  - Collect feedback to refine conversation flows, improve AI models, and enhance UI accessibility.

# Requirements 
1. Python 3.6+
2. ChatGPT API key
3. OpenAI python library

# How to install requirements
1. Python 3.6+
   1. Install python through theri official website - https://www.python.org/downloads/
   2. pip - Python package manager will be automatically installed with python

3. ChatGPT API key
   1. Go to https://platform.openai.com/account/api-keys
   2. Sign up
   3. You will see an option to create a new API key or use an existing one
   4. Copy the API key and paste it in the python file
   5. You have to put a new API key to start using the API

5. OpenAI python library
   1. Open command prompt in terminal
   2. Type pip install --upgrade openai
   3. Press enter

# Set Up 
1. Install required dependencies
2. Set up your OpenAI API key in the code. Replace YOUR_API_KEY with your actual API key.
3. Run the chatbot using the following command: `python main.py`
 
# Disclaimer
The Smart Helper Assistance Chatbot is designed to provide general medical information and support. It is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified healthcare providers with any questions you may have regarding a medical condition.
