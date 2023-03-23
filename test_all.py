import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    packages = ['tests']
    for package in packages:
        print(f'Start running tests in package {package}')
        suite.addTests(loader.discover(package))

    print('\n')
    print('==== Running All Tests ====')
    print('\n')

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    
    print('\n')
    print('==== All Tests Completed ====')
