import logging

# 1. Configure logging and save logs to file
logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 2. Custom Exception
class NegativeNumberError(Exception):
    pass


def divide_numbers(a, b):
    try:
        # 3. Simulate runtime errors
        if a < 0 or b < 0:
            raise NegativeNumberError("Negative numbers are not allowed")

        result = a / b

    # 4. Handle multiple exceptions
    except ZeroDivisionError as e:
        logging.error("ZeroDivisionError occurred", exc_info=True)
        print("Error: Cannot divide by zero")

    except NegativeNumberError as e:
        logging.error(e, exc_info=True)
        print("Error:", e)

    except TypeError as e:
        logging.error("TypeError occurred", exc_info=True)
        print("Error: Invalid data type")

    else:
        # 5. else block (runs if no exception)
        print("Result:", result)

    finally:
        # 6. finally block (always executes)
        print("Execution completed\n")


# 7. Test cases to debug using logs
divide_numbers(10, 2)     # No error
divide_numbers(10, 0)     # ZeroDivisionError
divide_numbers(-5, 2)     # Custom error
divide_numbers(10, "a")  # TypeError
