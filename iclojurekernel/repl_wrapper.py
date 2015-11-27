import pexpect


class ReplWrapper:
    def __init__(self):
        self.lein = pexpect.spawn('lein repl')

        # Wait for the expected prompt:
        self._wait_for_prompt()


    # TODO: support multiple lines
    def sendline(self, line):
        self.lein.sendline(line)
        line = self.lein.read()
        self._wait_for_prompt()
        return line

    def _wait_for_prompt(self):
        print "Waiting for prompt..."
        self.lein.expect('user=>')


if __name__ == '__main__':
    print "Creating wrapper..."
    repl = ReplWrapper()

    print "Sending a line"
    print repl.sendline('(+ 1 2)')
