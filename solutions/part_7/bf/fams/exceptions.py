# 🛡️ PART 2 — EXCEPTION DESIGN
class AcademyError(Exception):
  pass


class RegistrationError(AcademyError):
  pass


class PlayerNotFoundError(AcademyError):
  pass


class PlayerAlreadyExistsError(RegistrationError):
  pass


class InvalidPlayerError(AcademyError):
  pass