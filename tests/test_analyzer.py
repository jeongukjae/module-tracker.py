import pytest

from module_tracker.analyzer import parse_file_content


@pytest.mark.parametrize(
    "file_content,result",
    [
        pytest.param("import ast", ["ast"]),
        pytest.param("from ast import AST", ["ast"]),
        pytest.param("import ast as a", ["ast"]),
        pytest.param("import ast, time, os", ["ast", "time", "os"]),
        pytest.param("from .some.relative import kk", []),
        pytest.param("from ...some.relative import kk", []),
    ],
)
def test_analyze_import_statement(file_content, result):
    assert parse_file_content(file_content) == result
