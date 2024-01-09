# Interview Practice Assistant

This Python script is designed to assist users in practicing data structure and algorithm-related interview questions. The assistant engages with the user by posing questions, transcribing speech responses into text, and evaluating answers that you have given .Then you are provided with a score according to your given answers .

![Logo](https://assets-global.website-files.com/5d0cef7a72ca1b074065dfda/5fbb28398b0fcca170077fe3_Group.svg )

## Prerequisites

- OpenAI GPT-3.5 Turbo API key: Obtain and set the API key in the `.env` file.
- Python 3.x

## Dependencies

- `re` (regular expressions)
- `openai` (OpenAI GPT-3.5 Turbo API)
- `pyttsx3` (text-to-speech conversion)
- `speech_recognition` (speech recognition)
- `dotenv` (for loading API key from the `.env` file)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Interview-Practice-Assistant.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up your OpenAI API key:
    - Create a `.env` file in the root directory.
    - Add your OpenAI GPT-3.5 Turbo API key to the `.env` file:

        ```
        API_KEY=your-api-key-goes-here
        ```

## Usage

1. Run the script:

    ```bash
    python interview_assistant.py
    ```

2. The assistant will ask predefined questions. Speak your responses, and the assistant will evaluate them using the OpenAI model.

## Customization

Feel free to customize the list of interview questions (`dsa_questions`) or modify the script for your specific use case.

## Advantages

- **Personalized Practice:** Users can practice interview questions in a conversational manner, enhancing their ability to articulate solutions.
- **Real-time Feedback:** The OpenAI model provides immediate feedback on the quality of responses, helping users identify areas for improvement.
- **Voice Interaction:** The script supports voice input, making the practice experience more interactive and resembling a real interview scenario.

## Conclusion

The Interview Practice Assistant leverages cutting-edge technology to offer an interactive and personalized interview preparation experience. Whether you are a job seeker honing your skills or an interviewer looking to simulate questions, this tool provides a dynamic platform for practicing and refining your responses. By integrating speech recognition and the power of GPT-3.5 Turbo, the assistant strives to make the interview preparation process more engaging and effective.

## Notes

- Adjust pyttsx3 settings (voice, volume, rate) in the code according to your preferences.
- Ensure the `.env` file contains the correct OpenAI GPT-3.5 Turbo API key.


