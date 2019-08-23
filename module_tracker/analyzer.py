import ast
from typing import List, Type, Union, cast

ImportType = Type[Union[ast.Import, ast.ImportFrom]]


def parse_file(file_name: str) -> List[str]:
    with open(file_name) as f:
        return parse_file_content(f.read())


def parse_file_content(file_content: str) -> List[str]:
    parsed_file = ast.parse(file_content)
    return [
        import_name
        for node in ast.walk(parsed_file)
        if _is_import_statement(node)
        for import_name in _get_imported_modules(node)
    ]


def _is_import_statement(node: ast.AST) -> bool:
    return isinstance(node, (ast.Import, ast.ImportFrom))


def _get_imported_modules(node: ast.AST):
    import_statement = cast(ImportType, node)

    if isinstance(import_statement, ast.Import):
        return _get_modules_from_import_statement(import_statement)
    elif isinstance(import_statement, ast.ImportFrom):
        return _get_modules_from_import_from_statement(import_statement)

    return []


def _get_modules_from_import_statement(import_statement):
    return [_normalized_name(alias.name) for alias in import_statement.names]


def _get_modules_from_import_from_statement(import_from_statement):
    return [_normalized_name(import_from_statement.module)] if import_from_statement.level == 0 else []


def _normalized_name(import_name: str) -> str:
    return import_name.split(".")[0]
