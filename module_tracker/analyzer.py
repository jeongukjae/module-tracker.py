import ast
from typing import List, Type, Union, cast

ImportType = Type[Union[ast.Import, ast.ImportFrom]]


def parse_file(file_content: str) -> List[str]:
    parsed_file = ast.parse(file_content)
    return [
        import_name
        for node in ast.walk(parsed_file)
        if _is_import_statement(node)
        for import_name in _get_imported_module(node)
    ]


def _is_import_statement(node: ast.AST) -> bool:
    return isinstance(node, (ast.Import, ast.ImportFrom))


def _get_imported_module(node: ast.AST):
    import_statement = cast(ImportType, node)
    if isinstance(import_statement, ast.Import):
        return [alias.name for alias in import_statement.names]
    elif isinstance(import_statement, ast.ImportFrom):
        return [import_statement.module]
