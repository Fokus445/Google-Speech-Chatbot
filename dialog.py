
from google.cloud import dialogflow

from GoogleTextToSpeech import GoogleTextToSpeech


class DF_intents:

    def __init__(self, project_id, session_id, language_code):
        self.project_id = project_id
        self.session_id = session_id
        self.tts = GoogleTextToSpeech(language_code)
        self.language_code = language_code

    def detect_intent_texts(self, texts):
        """Returns the result of detect intent with texts as inputs.

        Using the same `session_id` between requests allows continuation
        of the conversation."""

        session_client = dialogflow.SessionsClient()

        session = session_client.session_path(self.project_id, self.session_id)
        print("Session path: {}\n".format(session))

        for text in texts:
            text_input = dialogflow.TextInput(text=text, language_code=self.language_code)

            query_input = dialogflow.QueryInput(text=text_input)

            response = session_client.detect_intent(
                request={"session": session, "query_input": query_input}
            )

            print("=" * 20)
            print("Query text: {}".format(response.query_result.query_text))
            print(
                "Detected intent: {} (confidence: {})\n".format(
                    response.query_result.intent.display_name,
                    response.query_result.intent_detection_confidence,
                )
            )
            print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))

            self.tts.speak(response.query_result.fulfillment_text)

