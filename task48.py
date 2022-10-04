import datetime


class TimeInfoMixin():
    def get_time(self):
        now = datetime.datetime.now()
        return now.strftime('%d-%m-%Y %H:%M')


class MusicPlayMixin():
    def play_music(self, name: str):
        print(f'Now is playing {name}')


class Notebook(TimeInfoMixin, MusicPlayMixin):
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color


lenovo = Notebook('lenovo', 'grey')
print(lenovo.get_time())
lenovo.play_music('Piano')
print(Notebook.__mro__)
