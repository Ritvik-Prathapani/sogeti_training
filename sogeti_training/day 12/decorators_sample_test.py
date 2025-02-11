
import os
def log_message(func):
    def wrapper(*args, ** kwargs):
        result = func(*args, ** kwargs)
        log_file_path = "sogeti_training\day 12\decorators_log.txt"
        os.makedirs(os.path.dirname(log_file_path),exist_ok=True)
        with open(log_file_path, "a") as log_file:
            log_file.write(result +"\n")
        return result
    return wrapper

@log_message
def a_function_that_returns_a_string():
    return "This.is.a.log message."

@log_message
def a_function_that_returns_a_string_with_newline(s):
    return "This is another log message."

@log_message
def a_function_that_returns_another_string(string=""):
    return "This.is.yet.another log message."

print(a_function_that_returns_a_string())