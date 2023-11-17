from color import *

DEFAULT_PREFIX = "🍨"

# 🍨 | [object name]: [object Object]
# 🍨 | [file].py:[line] > [function] | [time] ; [date]


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


sb = Sorbet()
