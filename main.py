from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
import datetime
import webbrowser

class MustaraAI(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title Label
        title = Label(
            text="MUSTARA AI ASSISTANT",
            size_hint=(1, 0.1),
            font_size='20sp',
            bold=True,
            color=(1, 0.4, 0.7, 1)
        )
        self.layout.add_widget(title)

        # Scrollable Chat Area
        self.scroll = ScrollView(size_hint=(1, 0.75))
        self.chat_history = Label(
            text="Mustara: Konnichiwa! I am Mustara.\nType: time, date, weather, settings, youtube, whatsapp, or search!\n\n",
            size_hint_y=None,
            font_size='16sp',
            halign='left',
            valign='top'
        )
        self.chat_history.bind(texture_size=self.update_chat_size)
        self.scroll.add_widget(self.chat_history)
        self.layout.add_widget(self.scroll)

        # Input and Send Button Layout
        input_layout = BoxLayout(size_hint=(1, 0.15), spacing=5)
        self.user_input = TextInput(
            hint_text="Type command here (e.g. time, weather)",
            multiline=False,
            size_hint=(0.75, 1)
        )
        self.user_input.bind(on_text_validate=self.process_command)
        input_layout.add_widget(self.user_input)

        send_btn = Button(
            text="Send",
            size_hint=(0.25, 1),
            background_color=(0.6, 0.1, 0.3, 1)
        )
        send_btn.bind(on_press=self.process_command)
        input_layout.add_widget(send_btn)

        self.layout.add_widget(input_layout)
        return self.layout

    def update_chat_size(self, instance, value):
        instance.text_size = (instance.width, None)
        instance.height = instance.texture_size[1]

    def process_command(self, instance):
        query = self.user_input.text.strip().lower()
        if not query:
            return

        self.chat_history.text += f"You: {query}\n"
        self.user_input.text = ""

        # Command handling
        if "time" in query:
            now = datetime.datetime.now().strftime("%I:%M %p")
            reply = f"Mustara: The current time is {now}."
        elif "date" in query:
            today = datetime.datetime.now().strftime("%d %B %Y")
            reply = f"Mustara: Today's date is {today}."
        elif "youtube" in query:
            webbrowser.open("https://www.youtube.com")
            reply = "Mustara: Opening YouTube..."
        elif "whatsapp" in query:
            webbrowser.open("https://api.whatsapp.com")
            reply = "Mustara: Opening WhatsApp..."
        elif "weather" in query:
            webbrowser.open("https://www.google.com/search?q=weather")
            reply = "Mustara: Checking the weather for you..."
        elif "search" in query:
            webbrowser.open("https://www.google.com")
            reply = "Mustara: Opening Google Search..."
        else:
            reply = "Mustara: Command not recognized. Try 'time', 'date', 'youtube', or 'weather'."

        self.chat_history.text += f"{reply}\n\n"
        self.scroll.scroll_y = 0

if __name__ == '__main__':
    MustaraAI().run()
          
