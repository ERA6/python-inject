import typing


T = typing.TypeVar('T')
Injector = typing.TypeVar('Injector')


def configure(
    config: typing.Optional[typing.Callable], bind_in_runtime: bool = True
) -> None: ...


def configure_once(
    config: typing.Optional[typing.Callable], bind_in_runtime: bool = True
) -> None: ...


def clear_and_configure(
    config: typing.Optional[typing.Callable], bind_in_runtime: bool = True
) -> None: ...


def is_configured() -> bool: ...


def clear() -> None: ...


def params(**args_to_classes: typing.Type[T]) -> typing.Callable: ...


def autoparams(*selected_args: str) -> typing.Callable: ...


def instance(cls: typing.Type[T]) -> T: ...


def attr(cls: typing.Type[T]) -> T: ...


def get_injector() -> typing.Optional[Injector]: ...


def get_injector_or_die() -> Injector: ...

