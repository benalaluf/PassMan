class GlobalData:
  def __init__(self):
    self._state = dict()

  def register_state(self, state):
    self._state[state.get_key()] = state

  def get_state_by_key(self, key: str):
    return self._state.get(key)
  
global_data = GlobalData()

class Data:
  def __init__(self, key: str, value=None):
    self._global_state = global_data
    self._key = key
    self._value = value
    self.register_with_global()
  
  def register_with_global(self):
    self._global_state.register_state(self)

  def get_key(self):
    return self._key

  def get_state(self):
    return self._value
