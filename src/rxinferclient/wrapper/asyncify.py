from typing import TypeVar, Type, Any, Callable
from functools import wraps
from inspect import ismethod, isfunction, iscoroutinefunction
from asyncer import asyncify as asyncer_asyncify

T = TypeVar('T')

def asyncify(cls: Type[T]) -> Type[T]:
    """Create an async version of a class using asyncer."""
    class AsyncWrapper:
        def __init__(self, *args, **kwargs):
            self._wrapped = cls(*args, **kwargs)
            self._async_cache = {}

        def __getattr__(self, name: str) -> Any:
            """
            Delegate attribute access to the wrapped class.
            If the attribute is a method, return its async version.
            """
            attr = getattr(self._wrapped, name)
            
            # If it's not a method or function, or it's private, return as is
            if not (ismethod(attr) or isfunction(attr)) or name.startswith('_'):
                return attr
                
            # If it's already async, return as is
            if iscoroutinefunction(attr):
                return attr
                
            # Check if we already created an async version
            if name not in self._async_cache:
                self._async_cache[name] = asyncer_asyncify(attr)
                
            return self._async_cache[name]

    return AsyncWrapper
