class MediaIntrface:

    def __init__(self, path):

        if path is None or path == '':
            raise ValueError('Error!! No File to play')
        else:
            self.__path = path
        self._type = 'UnKnown Type'

    def get_path(self):
        return self.__path

    def set_path(self, path):
        if path is None or path == '':
            raise ValueError('Error!! No File to play')

        self.__path = path

    def play(self):
        raise NotImplementedError('Sory!!  Not Implemented yet!!')

    def stop(self):
        print('Stop '+self.__path)
        
    def __del__(self):
        print('Delete '+self.__path +' as '+self._type)
        
    path = property(get_path, set_path)

    

class MP4(MediaIntrface):

    def play(self):
        self._type = 'MP4'
        return self.path + ' is playing as '+self._type


class WVM(MediaIntrface):
    def play(self):
        self._type = 'WVM'
        return self.path + ' is playing as '+self._type


def play(media):
    print(media.play())


def stop(media):
    media.stop()


MP4media = MP4('//ExampleURI...//')
WVMmedia = WVM('//ExampleURI...//')

print(' Run MP4 -------------------------')
play(MP4media)
print(' Stop MP4 -------------------------')
stop(MP4media)

print(' Run WVM -------------------------')
play(WVMmedia)
print(' Stop WVM -------------------------')
stop(WVMmedia)

del MP4media
del WVMmedia