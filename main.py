from Logger import logger, log_func


@log_func
def test_func():
    a = 5*2


def main():
    logger.info('line from logger')
    test_func()
    print('seminar bitch')






if __name__ == '__main__':
    main()
