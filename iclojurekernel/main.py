from ipykernel.kernelbase import Kernel
from ipykernel.kernelapp import IPKernelApp
from repl_wrapper import ReplWrapper


class IClojureKernel(Kernel):
    implementation = 'IClojureKernel'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {'mimetype': 'text/plain'}
    banner = "Clojure"

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self.repl = ReplWrapper()

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if len(code.strip()) == 0:
            return self._create_ok_response()

        # Code already has a newline at the end, strip that:
        code = code.rstrip()
        output = self.repl.sendline(code)

        if not silent:
            stream_content = {'name': 'stdout', 'text': output}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return self._create_ok_response()

    def _create_ok_response(self):
        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {}}


def main():
    IPKernelApp.launch_instance(kernel_class=IClojureKernel)


if __name__ == '__main__':
    main()
