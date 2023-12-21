from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class Main1(App):
    def build(self):
        img = AsyncImage(source='https://supermariorun.com/assets/img/stage/mario03.png',
                         size_hint=(1, 0.5),
                         pos_hint={'center_x': 0.5, 'center_y': 0.5})
        return img

if __name__ == '__main__':
    app = Main1()
    app.run()
