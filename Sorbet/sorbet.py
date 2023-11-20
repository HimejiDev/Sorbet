from color import *
from format_strings import *
import inspect
import executing

DEFAULT_PREFIX = "🍨"


def get_arg_strings(call_frame):
    callNode = Source.executing(call_frame).node
    source = Source.for_frame(call_frame)
    return [source.get_text_with_indentation(arg) for arg in callNode.args]


class Source(executing.Source):
    def get_text_with_indentation(self, node):
        result = self.asttokens().get_text(node)
        if "\n" in result:
            result = " " * node.first_token.start[1] + result
            result = result
        result = result.strip()
        return result


class Sorbet:
    """The Sorbet class."""

    def __init__(self, prefix=DEFAULT_PREFIX, output=False, includeContext=False):
        """Initializes the Sorbet class.

        :param prefix: The prefix to use for the logger.
        :param output: Whether to output to the console.
        :param includeContext: Whether to include the context in the output.

        :type prefix: str
        :type output: bool
        :type includeContext: bool

        :return: None
        """
        self.enabled = True
        self.prefix = prefix
        self.output = output
        self.includeContext = includeContext

    def __call__(self, *args):
        """Called when the class is called.

        :param args: The arguments to pass to the class.

        :type args: Tuple[Any]

        :return: Any | None
        """
        if self.enabled:
            callFrame = inspect.currentframe().f_back
            try:
                out = self._out(callFrame, *args)
            except executing.NoSourceAvailableError as err:
                out = f"{self.prefix} | {color.red('Error')}: {err.infoMessage}"
            print(out)

        if not args:  # sb()
            returns = None
        elif len(args) == 1:  # sb(1)
            returns = args[0]
        else:  # sb(1, 2, 3).
            returns = args
        return returns

    def _get_caller_info(self, caller_frame):
        """Gets the caller info.

        :param caller_frame: The caller frame.

        :type caller_frame: inspect.FrameInfo

        :return: Tuple[str, int, str]
        """
        function_name = caller_frame.f_code.co_name
        line_number = caller_frame.f_lineno
        file_name = caller_frame.f_code.co_filename
        return function_name, line_number, file_name.split("\\")[-1]

    def _out(self, callFrame, *args):
        """Formats the output.

        :param callFrame: The call frame.
        :param args: The arguments to pass to the class.

        :type callFrame: inspect.FrameInfo
        :type args: Tuple[Any]

        :return: str
        """
        if not args:
            caller_info = self._get_caller_info(callFrame)
            return f"{self.prefix} | {color.cyan(caller_info[2])}:{color.cyan(str(caller_info[1]))} > {color.cyan(caller_info[0])}{'()' if caller_info[0] != '<module>' else ''} | {color.cyan(get_time())} ; {color.cyan(get_date())}"
        else:
            return f"{self.prefix} | {self._format_args(args)}"

    def _format_args(self, *args):
        """Formats the arguments.

        :param args: The arguments to format.

        :type args: Tuple[Any]

        :return: str
        """
        return args


sb = Sorbet()
