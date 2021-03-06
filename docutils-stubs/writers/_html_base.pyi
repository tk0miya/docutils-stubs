# Stubs for docutils.writers._html_base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import nodes, writers
from docutils.frontend import Values
from docutils.transforms import Transform
from types import ModuleType
from typing import Any, Callable, Dict, List, Optional, overload, Pattern, Sequence, Tuple, Type

class PIL: ...

class Writer(writers.Writer):
    supported: Tuple[str, ...] = ...
    default_template: str = ...
    settings_defaults: Dict[str, str] = ...
    config_section_dependencies: Sequence[str] = ...
    visitor_attributes: List[str] = ...
    def get_transforms(self) -> List[Type[Transform]]: ...
    visitor: nodes.NodeVisitor = ...
    output: str = ...
    def translate(self) -> None: ...
    def apply_template(self) -> str: ...
    def interpolation_dict(self) -> Dict[str, str]: ...
    def assemble_parts(self) -> None: ...

class HTMLTranslator(nodes.NodeVisitor):
    xml_declaration: str = ...
    doctype: str = ...
    doctype_mathml: str = ...
    head_prefix_template: str = ...
    content_type: str = ...
    generator: str = ...
    mathjax_script: str = ...
    mathjax_url: str = ...
    stylesheet_link: str = ...
    embedded_stylesheet: str = ...
    words_and_spaces: Pattern[str] = ...
    in_word_wrap_point: Pattern[str] = ...
    lang_attribute: str = ...
    special_characters: Dict[int, str] = ...
    settings: Values = ...
    language: ModuleType = ...
    meta: List[str] = ...
    head_prefix: List[str] = ...
    html_prolog: List[str] = ...
    head: List[str] = ...
    stylesheet: List[str] = ...
    body_prefix: List[str] = ...
    body_pre_docinfo: List[str] = ...
    docinfo: List[str] = ...
    body: List[str] = ...
    fragment: List[str] = ...
    body_suffix: List[str] = ...
    section_level: int = ...
    initial_header_level: int = ...
    math_output: str = ...
    math_output_options: List[str] = ...
    context: List[Any] = ...
    topic_classes: List[Any] = ...
    colspecs: List[nodes.colspec] = ...
    compact_p: bool = ...
    compact_simple: bool = ...
    compact_field_list: bool = ...
    in_docinfo: bool = ...
    in_sidebar: bool = ...
    in_footnote_list: bool = ...
    title: List[str] = ...
    subtitle: List[str] = ...
    header: List[str] = ...
    footer: List[str] = ...
    html_head: List[str] = ...
    html_title: List[str] = ...
    html_subtitle: List[str] = ...
    html_body: List[str] = ...
    in_document_title: int = ...
    in_mailto: bool = ...
    author_in_authors: bool = ...
    math_header: List[str] = ...
    def __init__(self, document: nodes.document) -> None: ...
    def astext(self) -> str: ...
    def encode(self, text: str) -> str: ...
    def cloak_mailto(self, uri: str) -> str: ...
    def cloak_email(self, addr: str) -> str: ...
    def attval(self, text: str, whitespace: Pattern[str] = ...) -> str: ...
    def stylesheet_call(self, path: str) -> str: ...
    @overload
    def starttag(self, node: nodes.Node, tagname: str, **attributes) -> str: ...
    @overload  # NOQA: F811
    def starttag(self, node: nodes.Node, tagname: str, suffix: str = ..., **attributes) -> str: ...
    @overload  # NOQA: F811
    def starttag(self, node: nodes.Node, tagname: str, suffix: str = ..., empty: bool = ..., **attributes) -> str: ...
    def emptytag(self, node: nodes.Node, tagname: str, suffix: str = ..., **attributes) -> str: ...
    def set_class_on_child(self, node: nodes.Node, class_: Any, index: int = ...) -> None: ...
    def visit_Text(self, node: nodes.Text) -> None: ...
    def depart_Text(self, node: nodes.Text) -> None: ...
    def visit_abbreviation(self, node: nodes.Element) -> None: ...
    def depart_abbreviation(self, node: nodes.Element) -> None: ...
    def visit_acronym(self, node: nodes.Element) -> None: ...
    def depart_acronym(self, node: nodes.Element) -> None: ...
    def visit_address(self, node: nodes.Element) -> None: ...
    def depart_address(self, node: nodes.Element) -> None: ...
    def visit_admonition(self, node: nodes.Element) -> None: ...
    def depart_admonition(self, node: Optional[nodes.Element] = ...) -> None: ...
    attribution_formats: Dict[str, Tuple[str, str]] = ...
    def visit_attribution(self, node: nodes.Element) -> None: ...
    def depart_attribution(self, node: nodes.Element) -> None: ...
    def visit_author(self, node: nodes.Element) -> None: ...
    def depart_author(self, node: nodes.Element) -> None: ...
    def visit_authors(self, node: nodes.Element) -> None: ...
    def depart_authors(self, node: nodes.Element) -> None: ...
    def visit_block_quote(self, node: nodes.Element) -> None: ...
    def depart_block_quote(self, node: nodes.Element) -> None: ...
    def check_simple_list(self, node: nodes.Node) -> bool: ...
    def is_compactable(self, node: nodes.Node) -> bool: ...
    def visit_bullet_list(self, node: nodes.Element) -> None: ...
    def depart_bullet_list(self, node: nodes.Element) -> None: ...
    def visit_caption(self, node: nodes.Element) -> None: ...
    def depart_caption(self, node: nodes.Element) -> None: ...
    def visit_citation(self, node: nodes.Element) -> None: ...
    def depart_citation(self, node: nodes.Element) -> None: ...
    def visit_citation_reference(self, node: nodes.Element) -> None: ...
    def depart_citation_reference(self, node: nodes.Element) -> None: ...
    def visit_classifier(self, node: nodes.Element) -> None: ...
    def depart_classifier(self, node: nodes.Element) -> None: ...
    def visit_colspec(self, node: nodes.Element) -> None: ...
    def depart_colspec(self, node: nodes.Element) -> None: ...
    def visit_comment(self, node: nodes.Element, sub: Callable[[str, str], str] = ...) -> None: ...
    def visit_compound(self, node: nodes.Element) -> None: ...
    def depart_compound(self, node: nodes.Element) -> None: ...
    def visit_container(self, node: nodes.Element) -> None: ...
    def depart_container(self, node: nodes.Element) -> None: ...
    def visit_contact(self, node: nodes.Element) -> None: ...
    def depart_contact(self, node: nodes.Element) -> None: ...
    def visit_copyright(self, node: nodes.Element) -> None: ...
    def depart_copyright(self, node: nodes.Element) -> None: ...
    def visit_date(self, node: nodes.Element) -> None: ...
    def depart_date(self, node: nodes.Element) -> None: ...
    def visit_decoration(self, node: nodes.Element) -> None: ...
    def depart_decoration(self, node: nodes.Element) -> None: ...
    def visit_definition(self, node: nodes.Element) -> None: ...
    def depart_definition(self, node: nodes.Element) -> None: ...
    def visit_definition_list(self, node: nodes.Element) -> None: ...
    def depart_definition_list(self, node: nodes.Element) -> None: ...
    def visit_definition_list_item(self, node: nodes.Element) -> None: ...
    def depart_definition_list_item(self, node: nodes.Element) -> None: ...
    def visit_description(self, node: nodes.Element) -> None: ...
    def depart_description(self, node: nodes.Element) -> None: ...
    def visit_docinfo(self, node: nodes.Element) -> None: ...
    def depart_docinfo(self, node: nodes.Element) -> None: ...
    def visit_docinfo_item(self, node: nodes.Element, name: str, meta: bool = ...) -> None: ...
    def depart_docinfo_item(self) -> None: ...
    def visit_doctest_block(self, node: nodes.Element) -> None: ...
    def depart_doctest_block(self, node: nodes.Element) -> None: ...
    def visit_document(self, node: nodes.Element) -> None: ...
    def depart_document(self, node: nodes.Element) -> None: ...
    def visit_emphasis(self, node: nodes.Element) -> None: ...
    def depart_emphasis(self, node: nodes.Element) -> None: ...
    def visit_entry(self, node: nodes.Element) -> None: ...
    def depart_entry(self, node: nodes.Element) -> None: ...
    def visit_enumerated_list(self, node: nodes.Element) -> None: ...
    def depart_enumerated_list(self, node: nodes.Element) -> None: ...
    def visit_field_list(self, node: nodes.Element) -> None: ...
    def depart_field_list(self, node: nodes.Element) -> None: ...
    def visit_field(self, node: nodes.Element) -> None: ...
    def depart_field(self, node: nodes.Element) -> None: ...
    def visit_field_name(self, node: nodes.Element) -> None: ...
    def depart_field_name(self, node: nodes.Element) -> None: ...
    def visit_field_body(self, node: nodes.Element) -> None: ...
    def depart_field_body(self, node: nodes.Element) -> None: ...
    def visit_figure(self, node: nodes.Element) -> None: ...
    def depart_figure(self, node: nodes.Element) -> None: ...
    def visit_footer(self, node: nodes.Element) -> None: ...
    def depart_footer(self, node: nodes.Element) -> None: ...
    def visit_footnote(self, node: nodes.Element) -> None: ...
    def depart_footnote(self, node: nodes.Element) -> None: ...
    def visit_footnote_reference(self, node: nodes.Element) -> None: ...
    def depart_footnote_reference(self, node: nodes.Element) -> None: ...
    def visit_generated(self, node: nodes.Element) -> None: ...
    def depart_generated(self, node: nodes.Element) -> None: ...
    def visit_header(self, node: nodes.Element) -> None: ...
    def depart_header(self, node: nodes.Element) -> None: ...
    object_image_types: Dict[str, str] = ...
    def visit_image(self, node: nodes.Element) -> None: ...
    def depart_image(self, node: nodes.Element) -> None: ...
    def visit_inline(self, node: nodes.Element) -> None: ...
    def depart_inline(self, node: nodes.Element) -> None: ...
    def visit_label(self, node: nodes.Element) -> None: ...
    def depart_label(self, node: nodes.Element) -> None: ...
    def visit_legend(self, node: nodes.Element) -> None: ...
    def depart_legend(self, node: nodes.Element) -> None: ...
    def visit_line(self, node: nodes.Element) -> None: ...
    def depart_line(self, node: nodes.Element) -> None: ...
    def visit_line_block(self, node: nodes.Element) -> None: ...
    def depart_line_block(self, node: nodes.Element) -> None: ...
    def visit_list_item(self, node: nodes.Element) -> None: ...
    def depart_list_item(self, node: nodes.Element) -> None: ...
    def visit_literal(self, node: nodes.Element) -> None: ...
    def depart_literal(self, node: nodes.Element) -> None: ...
    def visit_literal_block(self, node: nodes.Element) -> None: ...
    def depart_literal_block(self, node: nodes.Element) -> None: ...
    math_tags: Dict[str, Tuple[str, str, str]] = ...
    def visit_math(self, node: nodes.Element, math_env: str = ...) -> None: ...
    def depart_math(self, node: nodes.Element) -> None: ...
    def visit_math_block(self, node: nodes.Element) -> None: ...
    def depart_math_block(self, node: nodes.Element) -> None: ...
    def visit_meta(self, node: nodes.Element) -> None: ...
    def depart_meta(self, node: nodes.Element) -> None: ...
    def add_meta(self, tag) -> None: ...
    def visit_option(self, node: nodes.Element) -> None: ...
    def depart_option(self, node: nodes.Element) -> None: ...
    def visit_option_argument(self, node: nodes.Element) -> None: ...
    def depart_option_argument(self, node: nodes.Element) -> None: ...
    def visit_option_group(self, node: nodes.Element) -> None: ...
    def depart_option_group(self, node: nodes.Element) -> None: ...
    def visit_option_list(self, node: nodes.Element) -> None: ...
    def depart_option_list(self, node: nodes.Element) -> None: ...
    def visit_option_list_item(self, node: nodes.Element) -> None: ...
    def depart_option_list_item(self, node: nodes.Element) -> None: ...
    def visit_option_string(self, node: nodes.Element) -> None: ...
    def depart_option_string(self, node: nodes.Element) -> None: ...
    def visit_organization(self, node: nodes.Element) -> None: ...
    def depart_organization(self, node: nodes.Element) -> None: ...
    def visit_paragraph(self, node: nodes.Element) -> None: ...
    def depart_paragraph(self, node: nodes.Element) -> None: ...
    def visit_problematic(self, node: nodes.Element) -> None: ...
    def depart_problematic(self, node: nodes.Element) -> None: ...
    def visit_raw(self, node: nodes.Element) -> None: ...
    def visit_reference(self, node: nodes.Element) -> None: ...
    def depart_reference(self, node: nodes.Element) -> None: ...
    def visit_revision(self, node: nodes.Element) -> None: ...
    def depart_revision(self, node: nodes.Element) -> None: ...
    def visit_row(self, node: nodes.Element) -> None: ...
    def depart_row(self, node: nodes.Element) -> None: ...
    def visit_rubric(self, node: nodes.Element) -> None: ...
    def depart_rubric(self, node: nodes.Element) -> None: ...
    def visit_section(self, node: nodes.Element) -> None: ...
    def depart_section(self, node: nodes.Element) -> None: ...
    def visit_sidebar(self, node: nodes.Element) -> None: ...
    def depart_sidebar(self, node: nodes.Element) -> None: ...
    def visit_status(self, node: nodes.Element) -> None: ...
    def depart_status(self, node: nodes.Element) -> None: ...
    def visit_strong(self, node: nodes.Element) -> None: ...
    def depart_strong(self, node: nodes.Element) -> None: ...
    def visit_subscript(self, node: nodes.Element) -> None: ...
    def depart_subscript(self, node: nodes.Element) -> None: ...
    def visit_substitution_definition(self, node: nodes.Element) -> None: ...
    def visit_substitution_reference(self, node: nodes.Element) -> None: ...
    def visit_subtitle(self, node: nodes.Element) -> None: ...
    def depart_subtitle(self, node: nodes.Element) -> None: ...
    def visit_superscript(self, node: nodes.Element) -> None: ...
    def depart_superscript(self, node: nodes.Element) -> None: ...
    def visit_system_message(self, node: nodes.Element) -> None: ...
    def depart_system_message(self, node: nodes.Element) -> None: ...
    def visit_table(self, node: nodes.Element) -> None: ...
    def depart_table(self, node: nodes.Element) -> None: ...
    def visit_target(self, node: nodes.Element) -> None: ...
    def depart_target(self, node: nodes.Element) -> None: ...
    def visit_tbody(self, node: nodes.Element) -> None: ...
    def depart_tbody(self, node: nodes.Element) -> None: ...
    def visit_term(self, node: nodes.Element) -> None: ...
    def depart_term(self, node: nodes.Element) -> None: ...
    def visit_tgroup(self, node: nodes.Element) -> None: ...
    def depart_tgroup(self, node: nodes.Element) -> None: ...
    def visit_thead(self, node: nodes.Element) -> None: ...
    def depart_thead(self, node: nodes.Element) -> None: ...
    def visit_title(self, node: nodes.Element) -> None: ...
    def depart_title(self, node: nodes.Element) -> None: ...
    def visit_title_reference(self, node: nodes.Element) -> None: ...
    def depart_title_reference(self, node: nodes.Element) -> None: ...
    def visit_topic(self, node: nodes.Element) -> None: ...
    def depart_topic(self, node: nodes.Element) -> None: ...
    def visit_transition(self, node: nodes.Element) -> None: ...
    def depart_transition(self, node: nodes.Element) -> None: ...
    def visit_version(self, node: nodes.Element) -> None: ...
    def depart_version(self, node: nodes.Element) -> None: ...
    def unimplemented_visit(self, node: nodes.Node) -> None: ...

class SimpleListChecker(nodes.GenericNodeVisitor):
    def default_visit(self, node: nodes.Node) -> None: ...
    def visit_list_item(self, node: nodes.Element) -> None: ...
    def pass_node(self, node: nodes.Element) -> None: ...
    def ignore_node(self, node: nodes.Element) -> None: ...
    visit_Text: Callable[[nodes.Text], None] = ...
    visit_paragraph: Callable[[nodes.Element], None] = ...
    visit_bullet_list: Callable[[nodes.Element], None] = ...
    visit_enumerated_list: Callable[[nodes.Element], None] = ...
    visit_docinfo: Callable[[nodes.Element], None] = ...
    visit_author: Callable[[nodes.Element], None] = ...
    visit_authors: Callable[[nodes.Element], None] = ...
    visit_address: Callable[[nodes.Element], None] = ...
    visit_contact: Callable[[nodes.Element], None] = ...
    visit_copyright: Callable[[nodes.Element], None] = ...
    visit_date: Callable[[nodes.Element], None] = ...
    visit_organization: Callable[[nodes.Element], None] = ...
    visit_status: Callable[[nodes.Element], None] = ...
    visit_version: Callable[[nodes.Element], None] = ...
    visit_definition_list: Callable[[nodes.Element], None] = ...
    visit_definition_list_item: Callable[[nodes.Element], None] = ...
    visit_term: Callable[[nodes.Element], None] = ...
    visit_classifier: Callable[[nodes.Element], None] = ...
    visit_definition: Callable[[nodes.Element], None] = ...
    visit_field_list: Callable[[nodes.Element], None] = ...
    visit_field: Callable[[nodes.Element], None] = ...
    visit_field_body: Callable[[nodes.Element], None] = ...
    visit_field_name: Callable[[nodes.Element], None] = ...
    visit_comment: Callable[[nodes.Element], None] = ...
    visit_substitution_definition: Callable[[nodes.Element], None] = ...
    visit_target: Callable[[nodes.Element], None] = ...
    visit_pending: Callable[[nodes.Element], None] = ...
