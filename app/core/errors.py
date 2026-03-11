"""
Docstring for app.core.error
it's for make your own error that we will use in error handelr. 
"""
class AppError(Exception):
  def __init__(self,message,status_code,payload=None) :
    super().__init__(message) # to make all the Exception enhirt the excption class and decorate it by add the code_status and message.
    self.message=message
    self.status_code=status_code
    self.payload=payload

class NotFoundError(AppError):#when the some thing not found 
  def __init__(self,message="Resource not found.", payload=None):
    super().__init__(message, 404, payload)

class ValidationError(AppError):# when the data from user is wrong.
  def __init__(self, message="Validition faild.", payload=None):
    super().__init__(message,400, payload)

class AuthenticationError(AppError):
    def __init__(self, message="Authentication failed", payload=None):
        super().__init__(message, 401, payload)


class PermissionError(AppError):
    def __init__(self, message="Permission denied", payload=None):
        super().__init__(message, 403, payload)


class DatabaseError(AppError):# for sql error
    def __init__(self, message="Database error", payload=None):
        super().__init__(message, 500, payload)
