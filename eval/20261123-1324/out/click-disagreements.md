# click: v2 against the scip-python oracle, 30 sampled disagreements

Commit `934813e4d421071a1b3db3973c02fe2721359a6e`, v2 `b3cd5e698314`, seed `20261031:click`.
Neither side is assumed right. Fill the verdict column with v2, oracle, both or neither.

| # | file:line | source | v2 | oracle | verdict |
|---|---|---|---|---|---|
| 1 | `examples/imagepipe/imagepipe.py:146` | `@cli.command("crop")` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::cli.command` | `src/click/core.py:1855 Group#command().` | |
| 2 | `examples/naval/naval.py:37` | `@ship.command("shoot")` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::ship.command` | `src/click/core.py:1855 Group#command().` | |
| 3 | `src/click/_compat.py:46` | `rv = getattr(stream, "encoding", None) or sys.getdefaultencoding()` | v2_unresolved_or_absent: `unresolved R8 reflection unresolved::python::getattr` | `external python-stdlib:builtins` | |
| 4 | `src/click/_compat.py:75` | `return self._stream.isatty()` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::self._stream.isatty` | `external python-stdlib:typing` | |
| 5 | `src/click/_compat.py:468` | `self._f.close()` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::self._f.close` | `external python-stdlib:typing` | |
| 6 | `src/click/_compat.py:519` | `def auto_wrap_for_ansi(` | v2_unresolved_or_absent: `no CALLS edge at this site` | `src/click/_compat.py:11 auto_wrap_for_ansi.auto_wrap_for_ansi.` | |
| 7 | `src/click/_compat.py:559` | `return getattr(sys.stdin, "encoding", None) or sys.getfilesystemencoding()` | v2_unresolved_or_absent: `unresolved R8 reflection unresolved::python::getattr` | `external python-stdlib:builtins` | |
| 8 | `src/click/_termui_impl.py:491` | `f.write(text.encode(encoding))` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::f.write` | `external python-stdlib:typing` | |
| 9 | `src/click/_termui_impl.py:776` | `f.close()` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::f.close` | `external python-stdlib:io` | |
| 10 | `src/click/core.py:1939` | `if self.group_class is not None and kwargs.get("cls") is None:` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::python::kwargs.get` | `external python-stdlib:builtins` | |
| 11 | `src/click/core.py:2426` | `return " / ".join(f"'{x}'" for x in hint_list)` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::python::"/".join` | `external python-stdlib:builtins` | |
| 12 | `src/click/core.py:2666` | `second = second.lstrip()` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::python::second.lstrip` | `external python-stdlib:builtins` | |
| 13 | `src/click/core.py:2999` | `super().__init__(param_decls, required=required, **attrs)` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::super().__init__` | `src/click/core.py:2093 Parameter#__init__().` | |
| 14 | `src/click/decorators.py:407` | `kwargs.setdefault("confirmation_prompt", True)` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::python::kwargs.setdefault` | `external python-stdlib:typing` | |
| 15 | `src/click/exceptions.py:88` | `_("Error: {message}").format(message=self.format_message()),` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::self.format_message` | `src/click/exceptions.py:38 ClickException#format_message().` | |
| 16 | `src/click/formatting.py:262` | `self.write_heading(name)` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::self.write_heading` | `src/click/formatting.py:185 HelpFormatter#write_heading().` | |
| 17 | `src/click/types.py:467` | `return self._clamp(self.max, -1, self.max_open)  # type: ignore` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::self._clamp` | `src/click/types.py:480 _NumberRangeBase#_clamp().` | |
| 18 | `src/click/types.py:853` | `return t.cast("os.PathLike[str]", self.type(value))` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::python::self.type` | `external python-stdlib:builtins` | |
| 19 | `src/click/utils.py:136` | `open(filename, mode).close()` | v2_target_differs: `name R4 python::.::src/click/utils.py::src/click/utils/LazyFile#open().#f9065fa7` | `external python-stdlib:builtins` | |
| 20 | `tests/test_arguments.py:196` | `assert expect in result.exception.format_message()` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::result.exception.format_message` | `src/click/exceptions.py:123 BadParameter#format_message().` | |
| 21 | `tests/test_chain.py:231` | `@l1a.command()` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::l1a.command` | `src/click/core.py:1855 Group#command().` | |
| 22 | `tests/test_command_decorators.py:5` | `@click.command` | v2_target_differs: `exact framework_calls:click:click.command python::.::tests/test_command_decorators.py::tests/test_command_decorators/test_command_no_parens().cli().#f9065fa7` | `src/click/decorators.py:137 command().` | |
| 23 | `tests/test_command_decorators.py:35` | `@click.group` | v2_target_differs: `exact framework_calls:click:click.group python::.::tests/test_command_decorators.py::tests/test_command_decorators/test_group_no_parens().grp().#f9065fa7` | `src/click/decorators.py:254 group().` | |
| 24 | `tests/test_defaults.py:46` | `@click.command` | v2_target_differs: `exact framework_calls:click:click.command python::.::tests/test_defaults.py::tests/test_defaults/test_multiple_flag_default().cli().#0ab2c236` | `src/click/decorators.py:137 command().` | |
| 25 | `tests/test_shell_completion.py:351` | `prev_available_shells = click.shell_completion._available_shells.copy()` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::python::click.shell_completion._available_shells.copy` | `external python-stdlib:builtins` | |
| 26 | `tests/test_utils.py:100` | `assert click.unstyle(text) == expect` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::click.unstyle` | `src/click/termui.py:591 unstyle().` | |
| 27 | `tests/test_utils.py:261` | `click.echo("Echo to standard error", err=True)` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::click.echo` | `src/click/utils.py:219 echo().` | |
| 28 | `tests/test_utils.py:293` | `click.pause("Pause to stdout")` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::python::click.pause` | `src/click/termui.py:753 pause().` | |
| 29 | `tests/typing/typing_help_option.py:13` | `assert_type(hello, click.Command)` | v2_unresolved_or_absent: `unresolved R8 external_not_indexed unresolved::python::assert_type` | `external python-stdlib:typing` | |
| 30 | `tests/typing/typing_simple_example.py:17` | `assert_type(hello, click.Command)` | v2_unresolved_or_absent: `unresolved R8 external_not_indexed unresolved::python::assert_type` | `external python-stdlib:typing` | |
