import pytest

from module_tracker.analyzer import parse_file


@pytest.mark.parametrize(
    "file_content,result",
    [
        pytest.param("import ast", ["ast"]),
        pytest.param("from ast import AST", ["ast"]),
        pytest.param("import ast as a", ["ast"]),
        pytest.param("import ast, time, os", ["ast", "time", "os"]),
    ],
)
def test_analyze(file_content, result):
    assert parse_file(file_content) == result
