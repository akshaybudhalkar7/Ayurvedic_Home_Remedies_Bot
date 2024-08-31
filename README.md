# Ayurvedic Home Remedies Bot

This project is a chatbot designed to provide users with Ayurvedic home remedies for common ailments. The bot is built using Python and can be integrated into various platforms, providing natural remedies and advice based on Ayurvedic practices.

## Features

- **User-Friendly Interface**: Easy-to-use interface for interacting with the bot.
- **Natural Remedies**: Provides many remedies for common health issues.
- **Integration with Platforms**: Can be integrated into different platforms like websites, messaging apps, etc.
- **Personalized Advice**: Offers personalized suggestions based on user input.
- **Educational Content**: Provides information about Ayurveda and the benefits of natural remedies.


## Installation

To set up the bot locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/akshaybudhalkar7/Ayurvedic_Home_Remedies_Bot.git
   cd Ayurvedic_Home_Remedies_Bot
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Ollama on a Local Machine**
  Download Ollama from the below URL
  https://ollama.com/

4. **Install Ollama application**

5. **Download the LLM model from Ollama**
     Go to cmd
     run the command "Ollama run "gemma2:2b"

## Run the application

1. Go to the Application folder
2. Run "python ingest.py" - This will create a vector store on the "Ayurvedic_Home_Remedies_Bot/vectorstore/db_faiss" This directory will contain index.faiss and index.pkl file
3. Open the terminal and then run "streamlit run Application/main.py" This will open the streamlit app on a web browser.

## Please refer below image of Streamlit Application
![image](https://github.com/user-attachments/assets/7a057369-2af2-4999-924c-9555d9b69e39)


   

     
     


