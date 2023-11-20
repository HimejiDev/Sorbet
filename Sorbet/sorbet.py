from color import *
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
        print(
            f"{color.white(self.prefix)} {color.bright_black('|')} Hi! I'm Sorbet, a logger made by Himeji."
        )

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
        caller_function = caller_frame.function
        caller_line = caller_frame.lineno
        caller_file = caller_frame.filename
        return caller_function, caller_line, caller_file


sb = Sorbet()
