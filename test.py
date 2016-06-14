r"""What is the point of this.
The goal is to show basic understanding
of python by pulling together a few ideas
to make a simple console app.

Highlights:
    - uses the PEP 8 style guide as best as possible
    - shows use of regex
    - shows basic use of sqlite
    and more

This is a simple thing, but hopfully it'll show
there is a good base to start from.  It is not complete
it is not at all anthing more then a sample app.

function foo(a, b){
  _a = (a<b?a:b);
  _b = (a<b?b:a);
  for(i=_a;i>0;i--){
    if(_a%i==0 && _b%i==0){
      console.log(i);return;
    }
  }
}foo(25,10)


Thank you - jeremyBass
"""
import sys

#note wise to update
def update_pip():
    import pip
    pip.main(['install', '-q', '--upgrade', 'pip'])

def is_installed(package: str):
    import importlib
    spam_loader = importlib.find_loader(package)
    return spam_loader is not None


def install(package: str, named: str = ''):
    if '' == named:
        named = package
    if False == is_installed(named):
        import pip
        pip.main(['install', '-q', package])

def uninstall(package: str):
    print('looking for ' + package)
    if False != is_installed(package):
        import pip
        print('found ' + package)
        pip.main(['uninstall', '-yq', package])


def is_prime(list: list):
    for n in list:
        for x in range(2, n):
            if n % x == 0:
                print( '{0} equals {1} * {2}'.format(n, x, n//x) )
                break
        else:
            # loop
            print('{0} is a prime number'.format(n))

def fib_high_point(start: int, end: int):
    from random import randint
    return randint(start, end)

def fib(number: int):
    a, b = 0, 1
    out = ''
    while a < number:
        if b < number:
            end = ','
        else:
            end = '\n'
        out = out + str(a) + end
        a, b = b, a+b
    return out


def query_yes_no(question: str, default: str = "no"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if None is default:
        prompt = " [y/n] "
    elif "yes" == default:
        prompt = " [Y/n] "
    elif "no" == default:
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and '' == choice:
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def validate_names(_name: str):
    import re
    regex = re.compile(r'^[^\W\d_]+(-[^\W\d_]+)?$', re.U)
    result = regex.match(_name) is not None
    return result

def confrim_odd_name(_type: str, _name: str):
    confirm = query_yes_no("Are you sure your {type} name is {name}?".format(name=_name, type=_type))
    if True == confirm:
        print("Fair enough, I want to meet your parents some some day though. :) ")
        return _name
    elif False == confirm:
        print("ok, well..")
        return ask_name(_type)
    else:
        print("truly sorry here I didn't understand that'")
        return confrim_odd_name(_type, _name)


def ask_name(_type: str,_name: str = '',count: int = 0):
    if "" != _name:
        if count > 1:
            return confrim_odd_name(_type, _name)
        else:
            print('Oh, I am sorry, "{name}" seems a like odd {type} name.\n If i may again..'.format(name=_name, type=_type))

    _name = input("What is your {type} name?".format(type=_type))
    seemsOk = validate_names(_name)

    if False == seemsOk:
        if count >= 0:
            count += 1
            return ask_name(_type, _name, count)
    else:
        return _name

def do_art(first_name: str, last_name: str):
    if False != is_installed('pyfiglet'):
        from colorama import init
        init(strip = not sys.stdout.isatty()) # strip colors if stdout is redirected
        from termcolor import cprint
        from pyfiglet import figlet_format

        cprint(figlet_format('{fn} {}'.format(last_name, fn=first_name), font='starwars'),
            'yellow', 'on_red', attrs=['bold'])
    else:
        print("oh I'm sorry it seems that the system didn't have the correct thing to show the trick")

def ask_about_art(first_name: str, last_name: str):
    confirm = query_yes_no("Would you like to see a trick?")
    if True == confirm:
        do_art(first_name, last_name)
    elif False == confirm:
        print("ok, well.. maybe next time")
    else:
        print("truly sorry here I didn't understand that'")
        return confrim_odd_name(first_name, last_name)

def ask_about_fib():
    confirm = query_yes_no("Would you like to see a randomize fibonacci sequence?")
    if True == confirm:
        setup = []

        for _ in range(10):
            setup.append(fib(fib_high_point(500,500000)))
        print('and another...\n'.join(map(str,setup)))
    elif False == confirm:
        print("ok, well.. maybe next time")
    else:
        print("truly sorry here I didn't understand that'")
        return ask_about_fib()


def ask_about_primes():
    confirm = query_yes_no("Would you like to see a prime number test?")
    if True == confirm:
        is_prime([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
    elif False == confirm:
        print("ok, well.. maybe next time")
    else:
        print("truly sorry here I didn't understand that'")
        return ask_about_primes()

def ask_about_dec():
    confirm = query_yes_no('Ok, enough "fun" would you like to read the doc?')
    if True == confirm:
        print(__doc__)
    elif False == confirm:
        print("ok, well.. maybe next time")
    else:
        print("truly sorry here I didn't understand that'")
        return ask_about_dec()

def run():
    from db import db
    init = db()
    print('Welcome, I don\'t know your name..')
    first_name = ask_name("first")

    # show understanding of formated strign concatination like printf of php
    print('Thank you {name} but I like to be formal,'.format(name=first_name))
    last_name = ask_name("last")

    init.set('helloWorld', ('firstname', 'lastname'), (first_name, last_name))

    # show understanding up positioning
    print('It is so wounderful to meet you {fn} {}.'\
            .format(last_name, fn=first_name) + '  I have also stored your name my mind (database).')

    ask_about_art(first_name, last_name)
    ask_about_fib()
    ask_about_primes()
    ask_about_dec()
    print('well... that was it :) so...\n Thank you come again.')

def system_check():
    update_pip()
    if len(sys.argv) > 1:
        print(sys.argv[1])
        if "clean" == sys.argv[1]:
            uninstall('pyfiglet')
            uninstall('termcolor')
            uninstall('colorama')
            print("cleaned")
            exit()

    if __name__ == '__main__':
        if False == is_installed('pyfiglet'):
            print('It looks like this is the first time running.\nWe will start the show in just a minute, please wait a secound as we prepare.')
            install('git+https://github.com/pwaller/pyfiglet','pyfiglet')
            install('termcolor')
            install('colorama')

def setup():
    from db import db
    system_check()
    init = db()
    init.create_db()
    run()

setup()


