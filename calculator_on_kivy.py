from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class SumApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        input1 = TextInput(font_size=30, height=100)
        input2 = TextInput(font_size=30, height=100)
        button = Button(text='Сложить', font_size=30, height=100)
        output = Label(font_size=30, height=100)

        def sum(*args):
            output.text = str(int(input1.text) + int(input2.text))

        button.bind(on_press=sum)
        layout.add_widget(input1)
        layout.add_widget(input2)
        layout.add_widget(button)
        layout.add_widget(output)
        return layout

if __name__ == '__main__':
    SumApp().run()
