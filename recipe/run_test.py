import sys
from subprocess import call

FAIL_UNDER = "90"
COV = ["coverage"]
RUN = ["run", "--source=rich", "--branch", "-m"]
PYTEST = ["pytest", "-vv", "--color=yes", "--tb=long"]
REPORT = ["report", "--show-missing", "--skip-covered", f"--fail-under={FAIL_UNDER}"]

SKIPS = [
    # https://github.com/conda-forge/rich-feedstock/pull/135
    ## confusion with `ipython` installed
    "(test_markdown and test_inline_code)",
    "(test_syntax and test_blank_lines)",
    "(test_syntax and test_python_render_simple_indent_guides)",
    "(test_syntax and test_from_path)",
    "(test_syntax and test_syntax_guess_lexer)",
]

SKIP_OR = " or ".join(SKIPS)
K = ["-k", f"not ({SKIP_OR})"]


if __name__ == "__main__":
    sys.exit(
        # run the tests
        call([*COV, *RUN, *PYTEST, *K, "src/tests"])
        # maybe run coverage
        or call([*COV, *REPORT])
    )
