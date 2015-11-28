import pexpect
import pexpect.exceptions


class ReplWrapper:
    def __init__(self):
        try:
            self.lein = pexpect.spawn('lein repl')
        except pexpect.exceptions.ExceptionPexpect:
            raise LeiningenNotFoundException()

        # Wait for the expected prompt:
        self._wait_for_prompt()

    def sendline(self, line):
        self.lein.sendline(line)
        self._wait_for_prompt()
        return self.lein.before
    """
    def sendline(self, line):
        return "you wrote '{}'".format(line)
        """

    def _wait_for_prompt(self):
        self.lein.expect('user=>')


class LeiningenNotFoundException(Exception):
    pass


if __name__ == '__main__':
    print "Creating wrapper..."
    try:
        repl = ReplWrapper()
    except LeiningenNotFoundException:
        print "You need to install Leiningen"

    while True:
        line = raw_input(">>> ")
        print repl.sendline(line)
