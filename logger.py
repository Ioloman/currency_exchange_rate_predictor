import os.path
from typing import Callable, Literal, Optional, Any, Final


LOG_FILE = 'log.log'

if os.path.exists(LOG_FILE):
    open(LOG_FILE, 'wt').close()

TYPE: Final = Literal['method', 'function', 'classmethod', 'staticmethod']
OUT: Final = Literal['console', 'file']


def log(method_role: str = '--', type_: TYPE = 'method', out: OUT = 'console',
        class_: Optional[str] = None, role_: Optional[str] = None) -> Callable[..., Callable]:
    def actual_decorator(func: Callable) -> Callable[..., Any]:
        def wrapper(*args, **kwargs) -> Any:
            # action before
            if out == 'file' and not os.path.exists(LOG_FILE):
                open(LOG_FILE, 'wt').close()
            if type_ == 'function':
                result = f'<{func.__name__}> -- {type_}'
                if out == 'console':
                    print(result)
                elif out == 'file':
                    with open(LOG_FILE, 'at') as file:
                        file.write(result + '\n')
            else:
                method = func.__name__
                if type_ == 'method':
                    cls = args[0].__class__.__name__
                    try:
                        role = args[0].__class__.role.__name__
                    except AttributeError:
                        role = '--'
                    id_ = id(args[0])
                elif type_ == 'classmethod':
                    cls = args[0].__name__
                    try:
                        role = args[0].role.__name__
                    except AttributeError:
                        role = '--'
                    id_ = cls
                elif type_ == 'staticmethod':
                    if class_:
                        cls = class_
                    else:
                        cls = '--'
                    if role_:
                        role = role_
                    else:
                        role = '--'
                    id_ = class_

                result = f'<{cls}>_<{role}>_<{id_}>:<{method}>[<{method_role}>] -- {type_}'
                if out == 'console':
                    print(result)
                elif out == 'file':
                    with open(LOG_FILE, 'at') as file:
                        file.write(result + '\n')

            return_value = func(*args, **kwargs)
            # action after
            return return_value
        return wrapper
    return actual_decorator
