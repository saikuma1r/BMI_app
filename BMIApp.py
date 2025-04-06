from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class BMIApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.height_input = TextInput(hint_text="Enter height (cm)", input_filter='float', multiline=False)
        self.weight_input = TextInput(hint_text="Enter weight (kg)", input_filter='float', multiline=False)

        self.calculate_button = Button(text="Calculate BMI")
        self.calculate_button.bind(on_press=self.calculate_bmi)

        self.result_label = Label(text="Your BMI will appear here")

        self.layout.add_widget(self.height_input)
        self.layout.add_widget(self.weight_input)
        self.layout.add_widget(self.calculate_button)
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate_bmi(self, instance):
        try:
            height_cm = float(self.height_input.text)
            weight_kg = float(self.weight_input.text)
            height_m = height_cm / 100
            bmi = weight_kg / (height_m ** 2)

            if bmi < 18.5:
                status = "Underweight"
            elif 18.5 <= bmi < 25:
                status = "Normal"
            elif 25 <= bmi < 30:
                status = "Overweight"
            else:
                status = "Obese"

            self.result_label.text = f"Your BMI: {bmi:.2f} ({status})"
        except:
            self.result_label.text = "Please enter valid numbers."


if __name__ == '__main__':
    BMIApp().run()
