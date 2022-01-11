# Stubs for docutils.writers.odf_odt (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import nodes, writers
from docutils.readers import standalone
from docutils.transforms import Transform
from types import ModuleType
from typing import Any, AnyStr, Dict, Iterator, List, Match, Mapping, MutableMapping, MutableSequence, Optional, Pattern, Set, Sequence, Tuple, Type, Union
from xml.etree import ElementTree as etree
import zipfile

VERSION: str
__docformat__: str
IMAGE_NAME_COUNTER: Iterator[int]
WhichElementTree: str
s1: str

class PIL: ...

class _ElementInterface: ...

class _ElementInterfaceWrapper(_ElementInterface):
    def __init__(self, tag: str, attrib: Optional[Mapping] = ...) -> None: ...
    def setparent(self, parent: Any) -> None: ...
    def getparent(self) -> Any: ...

SPACES_PATTERN: Pattern[str]
TABS_PATTERN: Pattern[str]
FILL_PAT1: Pattern[str]
FILL_PAT2: Pattern[str]
TABLESTYLEPREFIX: str
TABLENAMEDEFAULT: str
TABLEPROPERTYNAMES: Tuple[str, ...]
GENERATOR_DESC: str
NAME_SPACE_1: str
CONTENT_NAMESPACE_DICT: Dict[str, str]
CNSD: Dict[str, str]
STYLES_NAMESPACE_DICT: Dict[str, str]
SNSD: Dict[str, str]
MANIFEST_NAMESPACE_DICT: Dict[str, str]
MANNSD: Dict[str, str]
META_NAMESPACE_DICT: Dict[str, str]
METNSD: Dict[str, str]
CONTENT_NAMESPACE_ATTRIB: Dict[str, str]
STYLES_NAMESPACE_ATTRIB: Dict[str, str]
MANIFEST_NAMESPACE_ATTRIB: Dict[str, str]
META_NAMESPACE_ATTRIB: Dict[str, str]

def Element(tag: str, attrib: Optional[Dict[str, Any]] = ..., nsmap: Optional[Any] = ..., nsdict: Mapping[str, str] = ...) -> _ElementInterfaceWrapper: ...
def SubElement(parent: _ElementInterfaceWrapper, tag: str, attrib: Optional[Dict[str, Any]] = ..., nsmap: Optional[Any] = ..., nsdict: Mapping[str, str] = ...) -> _ElementInterfaceWrapper: ...
def fix_ns(tag: str, attrib: Mapping[str, Any], nsdict: Mapping[str, str]) -> Tuple[str, Dict[str, Any]]: ...
def add_ns(tag: str, nsdict: Mapping[str, str] = ...) -> str: ...
def ToString(et: Any) -> str: ...
def escape_cdata(text: str) -> str: ...

WORD_SPLIT_PAT1: Pattern[str]

def split_words(line) -> List[str]: ...

class TableStyle:
    border: Optional[str] = ...
    backgroundcolor: Any = ...
    def __init__(self, border: Optional[str] = ..., backgroundcolor: Optional[Any] = ...) -> None: ...
    def get_border_(self) -> Optional[str]: ...
    border_: Optional[str] = ...
    def set_border_(self, border: Optional[str]) -> None: ...
    def get_backgroundcolor_(self) -> Any: ...
    backgroundcolor_: Any = ...
    def set_backgroundcolor_(self, backgroundcolor: Any) -> None: ...

BUILTIN_DEFAULT_TABLE_STYLE: TableStyle

class ListLevel:
    level: Any = ...
    sibling_level: bool = ...
    nested_level: bool = ...
    def __init__(self, level: int, sibling_level: bool = ..., nested_level: bool = ...) -> None: ...
    def set_sibling(self, sibling_level: bool) -> None: ...
    def get_sibling(self) -> bool: ...
    def set_nested(self, nested_level: bool) -> None: ...
    def get_nested(self) -> bool: ...
    def set_level(self, level: int) -> None: ...
    def get_level(self) -> int: ...

class Writer(writers.Writer):
    MIME_TYPE: str = ...
    EXTENSION: str = ...
    supported: Tuple[str, ...] = ...
    default_stylesheet: str = ...
    default_stylesheet_path: str = ...
    default_template: str = ...
    default_template_path: str = ...
    settings_spec: Tuple[str, Any, Tuple[Tuple[str, List[str], Dict[str, Any]], ...]] = ...
    settings_defaults: Dict[str, str] = ...
    relative_path_settings: Tuple[str, ...] = ...
    config_section: str = ...
    config_section_dependencies: Sequence[str] = ...
    translator_class: Type["ODFTranslator"] = ...
    def __init__(self) -> None: ...
    settings: Any = ...
    visitor: "ODFTranslator" = ...
    output: str = ...
    def translate(self) -> None: ...
    def assemble_my_parts(self) -> None: ...
    def update_stylesheet(self, stylesheet_root: _ElementInterfaceWrapper, language_code: str, region_code: str) -> Tuple[bool, _ElementInterfaceWrapper, Set[_ElementInterfaceWrapper]]: ...
    def write_zip_str(self, zfile: zipfile.ZipFile, name: str, bytes: AnyStr, compress_type: int = ...) -> None: ...
    def store_embedded_files(self, zfile: zipfile.ZipFile) -> None: ...
    def get_settings(self) -> bytes: ...
    def get_stylesheet(self) -> str: ...
    def copy_from_stylesheet(self, outzipfile: zipfile.ZipFile) -> None: ...
    def assemble_parts(self) -> None: ...
    def create_manifest(self) -> str: ...
    def create_meta(self) -> str: ...

class ODFTranslator(nodes.GenericNodeVisitor):
    used_styles: Tuple[str, ...] = ...
    settings: Any = ...
    language_code: str = ...
    language: ModuleType = ...
    format_map: Dict[str, str] = ...
    section_level: int = ...
    section_count: int = ...
    content_tree: etree.ElementTree = ...
    current_element: _ElementInterfaceWrapper = ...
    automatic_styles: _ElementInterfaceWrapper = ...
    body_text_element: _ElementInterfaceWrapper = ...
    paragraph_style_stack: List[str] = ...
    list_style_stack: List[str] = ...
    table_count: int = ...
    column_count: int = ...
    trace_level: int = ...
    optiontablestyles_generated: bool = ...
    field_name: Any = ...
    field_element: Any = ...
    title: Optional[str] = ...
    image_count: int = ...
    image_style_count: int = ...
    image_dict: Dict[str, str] = ...
    embedded_file_list: List[Tuple[str, str]] = ...
    syntaxhighlighting: int = ...
    syntaxhighlight_lexer: str = ...
    header_content: List[etree.Element] = ...
    footer_content: List[etree.Element] = ...
    in_header: bool = ...
    in_footer: bool = ...
    blockstyle: str = ...
    in_table_of_contents: bool = ...
    table_of_content_index_body: Optional[_ElementInterfaceWrapper] = ...
    list_level: int = ...
    def_list_level: int = ...
    footnote_ref_dict: Dict[str, _ElementInterfaceWrapper] = ...
    footnote_list: List[Tuple[nodes.Node, _ElementInterfaceWrapper]] = ...
    footnote_chars_idx: int = ...
    footnote_level: int = ...
    pending_ids: List[str] = ...
    in_paragraph: bool = ...
    found_doc_title: bool = ...
    bumped_list_level_stack: List[ListLevel] = ...
    meta_dict: Dict[str, Any] = ...
    line_block_level: int = ...
    line_indent_level: int = ...
    citation_id: Optional[str] = ...
    style_index: int = ...
    str_stylesheet: str = ...
    str_stylesheetcontent: str = ...
    dom_stylesheet: etree.Element = ...
    table_styles: Dict[str, TableStyle] = ...
    in_citation: bool = ...
    inline_style_count_stack: List[int] = ...
    def __init__(self, document: nodes.document) -> None: ...
    def get_str_stylesheet(self) -> str: ...
    dom_stylesheetcontent: etree.Element = ...
    def retrieve_styles(self, extension: str) -> None: ...
    def extract_table_styles(self, styles_str: str) -> Dict[str, TableStyle]: ...
    def get_property(self, stylenode: Any) -> Any: ...
    def add_doc_title(self) -> None: ...
    def find_first_text_p(self, el: _ElementInterfaceWrapper) -> Optional[_ElementInterfaceWrapper]: ...
    def attach_page_style(self, el: _ElementInterfaceWrapper) -> None: ...
    def rststyle(self, name: str, parameters: Tuple[str] = ...) -> str: ...
    def generate_content_element(self, root: _ElementInterfaceWrapper) -> _ElementInterfaceWrapper: ...
    def setup_page(self) -> str: ...
    def get_dom_stylesheet(self) -> etree.Element: ...
    def setup_paper(self, root_el: _ElementInterfaceWrapper) -> None: ...
    def add_header_footer(self, root_el: _ElementInterfaceWrapper) -> None: ...
    code_none: int = ...
    code_field: int = ...
    code_text: int = ...
    field_pat: Pattern[str] = ...
    def create_custom_headfoot(self, parent: _ElementInterfaceWrapper, text: str, style_name: str, automatic_styles: _ElementInterfaceWrapper) -> None: ...
    def make_field_element(self, parent: _ElementInterfaceWrapper, text: str, style_name: str, automatic_styles: _ElementInterfaceWrapper) -> Optional[_ElementInterfaceWrapper]: ...
    def split_field_specifiers_iter(self, text: str) -> Iterator[Tuple[int, str]]: ...
    def astext(self) -> str: ...
    def content_astext(self) -> str: ...
    def set_title(self, title: str) -> None: ...
    def get_title(self) -> str: ...
    def set_embedded_file_list(self, embedded_file_list: List[Tuple[str, str]]) -> None: ...
    def get_embedded_file_list(self) -> List[Tuple[str, str]]: ...
    def get_meta_dict(self) -> Dict[str, Any]: ...
    def process_footnotes(self) -> None: ...
    def append_child(self, tag: str, attrib: Optional[Dict[str, Any]] = ..., parent: Optional[_ElementInterfaceWrapper] = ...) -> _ElementInterfaceWrapper: ...
    def append_p(self, style: str, text: Optional[Any] = ...) -> _ElementInterfaceWrapper: ...
    def append_pending_ids(self, el: _ElementInterfaceWrapper) -> None: ...
    def set_current_element(self, el: _ElementInterfaceWrapper) -> None: ...
    def set_to_parent(self) -> None: ...
    def generate_labeled_block(self, node: nodes.Node, label: str) -> _ElementInterfaceWrapper: ...
    def generate_labeled_line(self, node: nodes.Node, label: str) -> _ElementInterfaceWrapper: ...
    def encode(self, text: str) -> str: ...
    def dispatch_visit(self, node: nodes.Node) -> None: ...
    def handle_basic_atts(self, node: nodes.Node) -> None: ...
    def default_visit(self, node: nodes.Node) -> None: ...
    def default_departure(self, node: nodes.Node) -> None: ...
    footnote_chars: Any = ...
    def check_file_exists(self, path: str) -> int: ...
    def get_image_width_height(self, node: nodes.Node, attr: str) -> Union[Tuple[None, None], Tuple[float, str], Tuple[str, None]]: ...
    def convert_to_cm(self, size: str) -> Tuple[float, str]: ...
    def get_image_scale(self, node: nodes.Node) -> Union[float, int]: ...
    def get_image_scaled_width_height(self, node: nodes.Node, source: str) -> Tuple[str, str]: ...
    def get_page_width(self) -> float: ...
    def generate_figure(self, node: nodes.Node, source: str, destination: Any, current_element: _ElementInterfaceWrapper) -> Tuple[_ElementInterfaceWrapper, _ElementInterfaceWrapper, _ElementInterfaceWrapper, Optional[str]]: ...
    def generate_image(self, node: nodes.Node, source: str, destination: str, current_element, frame_attrs: Optional[MutableMapping[str, str]] = ...) -> Tuple[_ElementInterfaceWrapper, str]: ...
    def is_in_table(self, node: nodes.Node) -> bool: ...
    def fill_line(self, line: str) -> str: ...
    def fill_func1(self, matchobj: Match[str]) -> str: ...
    def fill_func2(self, matchobj: Match[str]) -> str: ...
    def get_table_style(self, node: nodes.Node) -> TableStyle: ...
    current_table_style: _ElementInterfaceWrapper = ...
    table_width: float = ...
    in_thead: bool = ...
    def generate_table_of_content_entry_template(self, el1: _ElementInterfaceWrapper) -> None: ...
    def find_title_label(self, node: nodes.Node, class_type: Type, label_key: str) -> str: ...
    save_current_element: _ElementInterfaceWrapper = ...
    def update_toc_page_numbers(self, el: _ElementInterfaceWrapper) -> None: ...
    def update_toc_collect(self, el: _ElementInterfaceWrapper, level: int, collection: MutableSequence[Tuple[int, _ElementInterfaceWrapper]]) -> None: ...
    def update_toc_add_numbers(self, collection: Sequence[Tuple[int, _ElementInterfaceWrapper]]) -> None: ...
    def generate_admonition(self, node: nodes.Node, label: str, title: Optional[str] = ...) -> None: ...

class Reader(standalone.Reader):
    def get_transforms(self) -> List[Type[Transform]]: ...
