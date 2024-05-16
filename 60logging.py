import logging

logging.basicConfig(filename="App.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def divide(x, y):
    try:
        result = x/y
        # print(result)
    except ZeroDivisionError as e:
        logging.error("Division by Zero: {}".format(e))
    else:
        logging.info("{} divided by {} equals to {}".format(x, y, result))

divide(10, 5)
divide(10, 0)