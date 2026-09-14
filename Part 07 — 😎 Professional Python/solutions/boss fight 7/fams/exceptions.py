# ./exceptions

'''Contains academy custom exceptions'''

class AcademyError(Exception):
  '''Generic academy error'''
  pass


class RegistrationError(AcademyError):
  '''Academy sub-error raised during failed registration operations.'''
  pass


class PlayerNotFoundError(AcademyError):
  '''Academy sub-error raised when searching for an unregistered player.'''
  pass


class PlayerAlreadyExistsError(RegistrationError):
  '''Registration sub-error raised when attempting to register already registered player.'''
  pass


class InvalidPlayerError(AcademyError):
  '''Academy sub-error raised when an invalid player argument is passed.'''
  pass