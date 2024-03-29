# Stubs for docutils.frontend (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import configparser as CP
from docutils.utils import DependencyList
import docutils.nodes
import optparse
from typing import Any, Dict, List, MutableSequence, Optional, Sequence, Tuple, Union

__docformat__: str

def store_multiple(option, opt, value: Any, parser, *args, **kwargs) -> None: ...
def read_config_file(option, opt, value, parser) -> None: ...
def validate_encoding(setting: str, value: str, option_parser: optparse.OptionParser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...) -> str: ...
def validate_encoding_error_handler(setting, value: str, option_parser: optparse.OptionParser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...) -> str: ...
def validate_encoding_and_error_handler(setting: str, value: str, option_parser: optparse.OptionParser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...) -> str: ...
def validate_boolean(setting: str, value: Union[bool, str], option_parser: optparse.OptionParser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...) -> bool: ...
def validate_ternary(setting: str, value: Union[bool, str], option_parser: optparse.OptionParser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...) -> Optional[bool]: ...
def validate_nonnegative_int(setting: str, value: Union[float, int, str], option_parser: optparse.OptionParser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...) -> int: ...
def validate_threshold(setting: str, value: Any, option_parser: optparse.OptionParser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...) -> int: ...
def validate_colon_separated_string_list(setting: str, value: Union[str, List[str]], option_parser: optparse.OptionParser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...) -> Union[str, List[str]]: ...
def validate_comma_separated_list(setting: str, value: Union[str, List[str]], option_parser: optparse.OptionParser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...) -> List[str]: ...
def validate_url_trailing_slash(setting: str, value: str, option_parser: optparse.OptionParser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...) -> str: ...
def validate_dependency_file(setting: str, value: Any, option_parser: optparse.OptionParser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...) -> DependencyList: ...
def validate_strip_class(setting: str, value: List[str], option_parser: optparse.OptionParser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...) -> List[str]: ...
def validate_smartquotes_locales(setting: str, value: Union[str, List[str]], option_parser: optparse.OptionParser, config_parser: Optional[Any] = ..., config_section: Optional[Any] = ...) -> List[Tuple[str, str]]: ...
def make_paths_absolute(pathdict: Dict[Any, Union[str, List[str]]], keys: Sequence[Any], base_path: Optional[str] = ...) -> None: ...
def make_one_path_absolute(base_path: str, path: str) -> str: ...
def filter_settings_spec(settings_spec: Tuple[str, Any, Tuple[Tuple[str, List[str], Dict[str, Any]], ...]], *exclude, **replace) -> Tuple[str, Any, Tuple[Tuple[str, List[str], Dict[str, Any]], ...]]: ...

class Values(optparse.Values):
    record_dependencies: DependencyList = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def update(self, other_dict, option_parser: optparse.OptionParser) -> None: ...
    def copy(self) -> "Values": ...

class Option(optparse.Option):
    ATTRS: List[str] = ...
    def process(self, opt: str, value, values, parser) -> int: ...

class OptionParser(optparse.OptionParser, docutils.SettingsSpec):
    standard_config_files: List[str] = ...
    threshold_choices: List[str] = ...
    thresholds: Dict[str, int] = ...
    booleans: Dict[str, bool] = ...
    default_error_encoding: Optional[str] = ...
    default_error_encoding_error_handler: str = ...
    settings_spec: Tuple[str, Any, Tuple[Tuple[str, List[str], Dict[str, Any]], ...]] = ...
    settings_defaults: Dict[str, Any] = ...
    relative_path_settings: List[str] = ...
    config_section: str = ...
    version_template: str = ...
    lists: Dict = ...
    config_files: List[str] = ...
    version: str = ...
    components: Any = ...
    def __init__(self, components: Any = ..., defaults: Optional[Any] = ..., read_config_files: Optional[Any] = ..., *args, **kwargs) -> None: ...
    def populate_from_components(self, components: Sequence[Any]) -> None: ...
    def get_standard_config_files(self) -> List[str]: ...
    def get_standard_config_settings(self) -> Values: ...
    def get_config_file_settings(self, config_file: str) -> Dict[str, Any]: ...
    def check_values(self, values: Values, args: MutableSequence[str]) -> Values: ...  # type: ignore
    def check_args(self, args: MutableSequence[str]) -> Tuple[Optional[str], Optional[str]]: ...
    def set_defaults_from_dict(self, defaults: Dict[str, Any]) -> None: ...
    def get_default_values(self) -> Values: ...
    def get_option_by_dest(self, dest) -> Option: ...

class ConfigParser(CP.RawConfigParser):
    old_settings: Dict[str, Tuple[str, str]] = ...
    old_warning: str = ...
    not_utf8_error: str = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def read(self, filenames: Union[str, Sequence[str]], option_parser: OptionParser) -> None: ...  # type: ignore
    def handle_old_config(self, filename: str) -> None: ...
    def validate_settings(self, filename: str, option_parser: OptionParser) -> None: ...
    def optionxform(self, optionstr: str) -> str: ...
    def get_section(self, section: str) -> Dict[str, str]: ...

class ConfigDeprecationWarning(DeprecationWarning): ...
