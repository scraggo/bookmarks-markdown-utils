import pyperclip

class PyperInterface:
  def __init__(self, in_message, out_message):
    self.in_message = in_message
    self.out_message = out_message
    self.in_data = ''
    self.out_data = ''

  def get_clipboard(self, pause = True):
    print(self.in_message)
    if pause:
      input('> ')
    self.in_data = pyperclip.paste()
    return self.in_data

  def send_to_clipboard(self, data):
    pyperclip.copy(data)
    self.out_data = data
    print(self.out_message)
