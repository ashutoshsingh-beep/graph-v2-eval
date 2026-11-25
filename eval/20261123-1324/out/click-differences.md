# click (python): graph differences to verify

Repo `https://github.com/pallets/click` at `934813e4d421071a1b3db3973c02fe2721359a6e`. Old engine `25ae40bf8662`, graph v2 `b3cd5e698314`.

## Status

Fill this in. `graph-eval.sh report` reads it, and the next run copies it forward.

- intern: 
- stage: not started   (not started | verifying | grouping patterns | done)
- language version: (auto)   write a value here to correct the detected one
- framework: (auto)   write a value here to correct the detected one
- next: 
- blocked by: 
- issues filed: 

## Counts

In-repo calls found by the oracle: 2283. Both right 990, gap 147, v2 gain 883, both miss 263.
Scored edges: v2 2787 (568 wrong), dev 1678 (96 wrong). Not scored: v2 644, dev 418.
CALLS recall: dev 49.8% (1137/2283), v2 82.0% (1873/2283). CALLS precision: dev 94.3% (1582/1678), v2 79.6% (2219/2787).
Line precision judges each engine only on lines where the oracle has a call it can map, and counts edges that sit on no oracle call (decorator lines) as wrong. Do not rank the engines on it alone.
v2 precision at exact call sites (published): 0.9984.
Flags: {"def_line_both_miss": 35, "dev_multi_both_right": 183, "dev_multi_gap": 36} (def_line_* = the line defines a function of the target's own name, usually the oracle's mistake; dev_multi_* = dev was right but had several targets on the line).
Scorer notes: {"dev_edges_with_file_source_never_scored": 16, "dev_calls_without_site_line": 0}.
Check against the published scores: OK (full).

## How each v2 miss happened

| group | v2 miss | reason | calls |
|---|---|---|---|
| both_miss | reported | dynamic_dispatch | 211 |
| gap | reported | dynamic_dispatch | 134 |
| both_miss | silent | - | 41 |
| gap | silent | - | 10 |
| both_miss | no_node | - | 8 |
| gap | reported | many_candidates | 3 |
| both_miss | reported | many_candidates | 3 |

`no_node`: v2 has no node for the target. `wrong_target`: v2 resolved this call to another target. `external`: v2 called it external. `reported`: only unresolved edges, with v2's reason. `silent`: no v2 edge at this call at all.

Verdict: `confirmed` (the row is what its group says), `oracle wrong`, `dev wrong`, `v2 right after all`, or `?`.
Cause: one short phrase for the code shape (for example `method on a constructor-injected field`). Reuse phrases.
Reason true: for a `reported` miss, `yes` or `no`.

## Gaps: dev is right, v2 is not (25 of 147)
<!-- kind: gap -->

What v2 loses against the old engine. Check: is the oracle target right, does dev's edge really go there, and is v2 really wrong?

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `src/click/_termui_impl.py:781` | `with raw_terminal() as fd:` | src/click/_termui_impl.py:699 raw_terminal(). | function::src/click/_termui_impl.py::raw_terminal | unresolved unresolved::python::raw_terminal | reported (many_candidates) |  |  |  |
| 2 | `src/click/core.py:1221` | `super().__init__(name, context_settings)` | src/click/core.py:870 BaseCommand#__init__(). | method::src/click/core.py::BaseCommand::__init__ | unresolved unresolved::python::super().__init__ | reported (dynamic_dispatch) |  |  |  |
| 3 | `src/click/core.py:1477` | `results.extend(super().shell_complete(ctx, incomplete))` | src/click/core.py:965 BaseCommand#shell_complete(). | method::src/click/core.py::BaseCommand::shell_complete | unresolved unresolved::python::super().shell_complete | reported (dynamic_dispatch) |  |  |  |
| 4 | `src/click/core.py:1520` | `super().__init__(name, **attrs)` | src/click/core.py:1206 Command#__init__(). | method::src/click/core.py::Command::__init__ | unresolved unresolved::python::super().__init__ | reported (dynamic_dispatch) |  |  |  |
| 5 | `src/click/formatting.py:187` | `self.write(f"{'':>{self.current_indent}}{heading}:\n")` | src/click/formatting.py:133 HelpFormatter#write(). | method::src/click/formatting.py::HelpFormatter::write | unresolved unresolved::python::self.write | reported (dynamic_dispatch) |  |  |  |
| 6 | `src/click/formatting.py:192` | `self.write("\n")` | src/click/formatting.py:133 HelpFormatter#write(). | method::src/click/formatting.py::HelpFormatter::write | unresolved unresolved::python::self.write | reported (dynamic_dispatch) |  |  |  |
| 7 | `src/click/formatting.py:262` | `self.write_heading(name)` | src/click/formatting.py:185 HelpFormatter#write_heading(). | method::src/click/formatting.py::HelpFormatter::write_heading | unresolved unresolved::python::self.write_heading | reported (dynamic_dispatch) |  |  |  |
| 8 | `src/click/types.py:186` | `self.fail(value, param, ctx)` | src/click/types.py:130 ParamType#fail(). | method::src/click/types.py::ParamType::fail | no edge | silent |  |  |  |
| 9 | `src/click/types.py:208` | `enc = _get_argv_encoding()` | src/click/_compat.py:512 _get_argv_encoding(). | function::src/click/_compat.py::_get_argv_encoding | unresolved unresolved::python::_get_argv_encoding | reported (many_candidates) |  |  |  |
| 10 | `src/click/types.py:297` | `self.fail(` | src/click/types.py:130 ParamType#fail(). | method::src/click/types.py::ParamType::fail | no edge | silent |  |  |  |
| 11 | `src/click/types.py:391` | `self.fail(` | src/click/types.py:130 ParamType#fail(). | method::src/click/types.py::ParamType::fail | no edge | silent |  |  |  |
| 12 | `src/click/types.py:414` | `self.fail(` | src/click/types.py:130 ParamType#fail(). | method::src/click/types.py::ParamType::fail | no edge | silent |  |  |  |
| 13 | `src/click/types.py:470` | `self.fail(` | src/click/types.py:130 ParamType#fail(). | method::src/click/types.py::ParamType::fail | no edge | silent |  |  |  |
| 14 | `src/click/types.py:611` | `self.fail(` | src/click/types.py:130 ParamType#fail(). | method::src/click/types.py::ParamType::fail | no edge | silent |  |  |  |
| 15 | `src/click/types.py:635` | `self.fail(` | src/click/types.py:130 ParamType#fail(). | method::src/click/types.py::ParamType::fail | no edge | silent |  |  |  |
| 16 | `src/click/types.py:745` | `self.fail(f"'{format_filename(value)}': {e.strerror}", param, ctx)` | src/click/types.py:130 ParamType#fail(). | function::src/click/utils.py::format_filename; method::src/click/types.py::ParamType::fail | import python::.::src/click/utils.py::src/click/utils/format_filename().#20f87597 | silent; dev has 2 targets on this line |  |  |  |
| 17 | `src/click/types.py:880` | `self.fail(` | src/click/types.py:130 ParamType#fail(). | method::src/click/types.py::ParamType::fail | no edge | silent |  |  |  |
| 18 | `src/click/types.py:990` | `self.fail(` | src/click/types.py:130 ParamType#fail(). | method::src/click/types.py::ParamType::fail | no edge | silent |  |  |  |
| 19 | `src/click/utils.py:310` | `if should_strip_ansi(file, color):` | src/click/_compat.py:496 should_strip_ansi(). | function::src/click/_compat.py::should_strip_ansi | unresolved unresolved::python::should_strip_ansi | reported (dynamic_dispatch) |  |  |  |
| 20 | `tests/test_context.py:313` | `assert cli.main([], "test_exit_not_standalone", standalone_mode=False) == 1` | src/click/core.py:995 BaseCommand#main(). | method::src/click/core.py::BaseCommand::main | unresolved unresolved::python::cli.main | reported (many_candidates) |  |  |  |
| 21 | `tests/test_utils.py:104` | `assert click.format_filename(b"foo.txt") == "foo.txt"` | src/click/utils.py:404 format_filename(). | function::src/click/utils.py::format_filename | unresolved unresolved::python::click.format_filename | reported (dynamic_dispatch) |  |  |  |
| 22 | `tests/test_utils.py:214` | `styled_text = click.style(text, fg="red")` | src/click/termui.py:462 style(). | function::src/click/termui.py::style | unresolved unresolved::python::click.style | reported (dynamic_dispatch) |  |  |  |
| 23 | `tests/test_utils.py:267` | `click.prompt("Prompt to stdin")` | src/click/termui.py:79 prompt(). | function::src/click/termui.py::prompt | unresolved unresolved::python::click.prompt | reported (dynamic_dispatch) |  |  |  |
| 24 | `tests/test_utils.py:352` | `with click.open_file(filename, errors="ignore") as f:` | src/click/utils.py:355 open_file(). | function::src/click/utils.py::open_file | unresolved unresolved::python::click.open_file | reported (dynamic_dispatch) |  |  |  |
| 25 | `tests/test_utils.py:467` | `assert user in click.utils._expand_args(["~"])` | src/click/utils.py:575 _expand_args(). | function::src/click/utils.py::_expand_args | unresolved unresolved::python::click.utils._expand_args | reported (dynamic_dispatch) |  |  |  |

## Wrong v2 edges (25 of 568)
<!-- kind: v2_wrong -->

A v2 edge on a line where the oracle has a call, whose target is none of that line's oracle targets. `at call site: no` means the edge sits on no call the oracle saw (for example a decorator line). Check: is v2's target wrong?

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `examples/aliases/aliases.py:119` | `@cli.command()` | src/click/core.py:1855 Group#command(). | no edge | exact python::.::examples/aliases/aliases.py::examples/aliases/aliases/commit().#f9065fa7 (at call site: no) |  |  |  |  |
| 2 | `examples/naval/naval.py:52` | `@click.argument("x", type=float)` | src/click/decorators.py:315 argument(). | function::src/click/decorators.py::argument | import python::.::src/click/decorators.py::src/click/decorators/argument().decorator().#58c0ebbe (at call site: no) |  |  |  |  |
| 3 | `tests/test_basic.py:29` | `@click.command()` | src/click/decorators.py:137 command(). | no edge | exact python::.::tests/test_basic.py::tests/test_basic/test_repr().command().#f9065fa7 (at call site: no) |  |  |  |  |
| 4 | `tests/test_basic.py:57` | `@click.group()` | src/click/decorators.py:254 group(). | no edge | exact python::.::tests/test_basic.py::tests/test_basic/test_basic_group().cli().#f9065fa7 (at call site: no) |  |  |  |  |
| 5 | `tests/test_basic.py:117` | `@click.command()` | src/click/decorators.py:137 command(). | no edge | exact python::.::tests/test_basic.py::tests/test_basic/test_string_option().cli().#ff92409d (at call site: no) |  |  |  |  |
| 6 | `tests/test_basic.py:210` | `@click.command()` | src/click/decorators.py:137 command(). | no edge | exact python::.::tests/test_basic.py::tests/test_basic/test_boolean_switch().cli().#ff92409d (at call site: no) |  |  |  |  |
| 7 | `tests/test_basic.py:408` | `@click.option("--start_date", type=click.DateTime())` | src/click/decorators.py:343 option().; src/click/types.py:334 DateTime# | function::src/click/decorators.py::option | import python::.::src/click/decorators.py::src/click/decorators/option().decorator().#58c0ebbe (at call site: no) |  |  |  |  |
| 8 | `tests/test_chain.py:95` | `@click.group(invoke_without_command=True, chain=chain)` | src/click/decorators.py:254 group(). | no edge | exact python::.::tests/test_chain.py::tests/test_chain/test_no_command_result_callback().cli().… (at call site: no) |  |  |  |  |
| 9 | `tests/test_chain.py:136` | `@click.group(chain=True, invoke_without_command=True)` | src/click/decorators.py:254 group(). | no edge | exact python::.::tests/test_chain.py::tests/test_chain/test_pipeline().cli().#ff92409d (at call site: no) |  |  |  |  |
| 10 | `tests/test_chain.py:207` | `@click.group(chain=True)` | src/click/decorators.py:254 group(). | no edge | exact python::.::tests/test_chain.py::tests/test_chain/test_multicommand_arg_behavior().cli().#… (at call site: no) |  |  |  |  |
| 11 | `tests/test_command_decorators.py:5` | `@click.command` | src/click/decorators.py:137 command(). | no edge | exact python::.::tests/test_command_decorators.py::tests/test_command_decorators/test_command_n… (at call site: yes) |  |  |  |  |
| 12 | `tests/test_command_decorators.py:35` | `@click.group` | src/click/decorators.py:254 group(). | no edge | exact python::.::tests/test_command_decorators.py::tests/test_command_decorators/test_group_no_… (at call site: yes) |  |  |  |  |
| 13 | `tests/test_command_decorators.py:64` | `@click.argument("b")` | src/click/decorators.py:315 argument(). | function::src/click/decorators.py::argument | import python::.::src/click/decorators.py::src/click/decorators/argument().decorator().#58c0ebbe (at call site: no) |  |  |  |  |
| 14 | `tests/test_defaults.py:18` | `@click.option("--foo", default=[23, 42], type=click.FLOAT, multiple=True)` | src/click/decorators.py:343 option(). | function::src/click/decorators.py::option | import python::.::src/click/decorators.py::src/click/decorators/option().decorator().#58c0ebbe (at call site: no) |  |  |  |  |
| 15 | `tests/test_defaults.py:46` | `@click.command` | src/click/decorators.py:137 command(). | no edge | exact python::.::tests/test_defaults.py::tests/test_defaults/test_multiple_flag_default().cli()… (at call site: yes) |  |  |  |  |
| 16 | `tests/test_formatting.py:234` | `@click.command(context_settings=dict(help_option_names=["--man"]))` | src/click/decorators.py:137 command(). | no edge | exact python::.::tests/test_formatting.py::tests/test_formatting/test_formatting_usage_custom_h… (at call site: no) |  |  |  |  |
| 17 | `tests/test_formatting.py:340` | `@click.option("-f", "in_file", default="out.txt", help="Output file name")` | src/click/decorators.py:343 option(). | function::src/click/decorators.py::option | import python::.::src/click/decorators.py::src/click/decorators/option().decorator().#58c0ebbe (at call site: no) |  |  |  |  |
| 18 | `tests/test_options.py:860` | `@click.argument("b", nargs=-1)` | src/click/decorators.py:315 argument(). | function::src/click/decorators.py::argument | import python::.::src/click/decorators.py::src/click/decorators/argument().decorator().#58c0ebbe (at call site: no) |  |  |  |  |
| 19 | `tests/test_termui.py:116` | `with _create_progress(length, pos=pos) as progress:` | tests/test_termui.py:21 _create_progress(). | function::tests/test_termui.py::_create_progress | name python::.::src/click/_termui_impl.py::src/click/_termui_impl/ProgressBar#__exit__().#0699… (at call site: no) |  |  |  |  |
| 20 | `tests/test_termui.py:433` | `@click.command()` | src/click/decorators.py:137 command(). | no edge | exact python::.::tests/test_termui.py::tests/test_termui/test_confirmation_prompt().cli().#ff92… (at call site: no) |  |  |  |  |
| 21 | `tests/test_testing.py:247` | `@click.command()` | src/click/decorators.py:137 command(). | no edge | exact python::.::tests/test_testing.py::tests/test_testing/test_exit_code_and_output_from_sys_e… (at call site: no) |  |  |  |  |
| 22 | `tests/test_types.py:38` | `(click.IntRange(0, 5), "6", "6 is not in the range 0<=x<=5."),` | src/click/types.py:517 IntRange# | no edge | name python::.::src/click/types.py::src/click/types/_NumberRangeBase#__init__().#aa077a00 (at call site: no) |  |  |  |  |
| 23 | `tests/test_utils.py:394` | `@click.command()` | src/click/decorators.py:137 command(). | no edge | exact python::.::tests/test_utils.py::tests/test_utils/test_open_file_atomic_permissions_existi… (at call site: no) |  |  |  |  |
| 24 | `tests/typing/typing_help_option.py:6` | `@click.command()` | src/click/decorators.py:137 command(). | no edge | exact python::.::tests/typing/typing_help_option.py::tests/typing/typing_help_option/hello().#f… (at call site: no) |  |  |  |  |
| 25 | `tests/typing/typing_version_option.py:11` | `@click.version_option("0.1")` | src/click/decorators.py:412 version_option(). | function::src/click/decorators.py::version_option | name python::.::src/click/decorators.py::src/click/decorators/option().decorator().#58c0ebbe (at call site: no) |  |  |  |  |

## v2 gains: v2 is right, dev is not (25 of 883)
<!-- kind: v2_gain -->

What v2 adds. Verify a few so the gain is real.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `examples/termui/termui.py:162` | `click.echo("  b: back")` | src/click/utils.py:219 echo(). | no edge | import python::.::src/click/utils.py::src/click/utils/echo().#e6dcab7f |  |  |  |  |
| 2 | `src/click/core.py:1697` | `return _process_result(sub_ctx.command.invoke(sub_ctx))` | src/click/core.py:1664 MultiCommand#_process_result(). | no edge | name python::.::src/click/core.py::src/click/core/MultiCommand#invoke()._process_result().#eb0… | dev has no node for the target |  |  |  |
| 3 | `src/click/core.py:1729` | `return _process_result(rv)` | src/click/core.py:1664 MultiCommand#_process_result(). | no edge | name python::.::src/click/core.py::src/click/core/MultiCommand#invoke()._process_result().#eb0… | dev has no node for the target |  |  |  |
| 4 | `src/click/core.py:1899` | `return decorator(func)` | src/click/core.py:1893 Group#decorator().; src/click/core.py:1945 Group#decorator(). | function::src/click/core.py::Group.group.<locals>.decorator | name python::.::src/click/core.py::src/click/core/Group#command().decorator().#940ed7fa | dev has no node for the target |  |  |  |
| 5 | `src/click/core.py:1951` | `return decorator(func)` | src/click/core.py:1893 Group#decorator().; src/click/core.py:1945 Group#decorator(). | function::src/click/core.py::Group.group.<locals>.decorator | name python::.::src/click/core.py::src/click/core/Group#group().decorator().#940ed7fa | dev has no node for the target |  |  |  |
| 6 | `src/click/core.py:2324` | `return tuple(self.type(x, self, ctx) for x in check_iter(value))` | src/click/core.py:2305 Parameter#check_iter(). | function::src/click/core.py::Parameter.type_cast_value.<locals>.check_iter | name python::.::src/click/core.py::src/click/core/Parameter#type_cast_value().check_iter().#eb… | dev has no node for the target |  |  |  |
| 7 | `src/click/core.py:2329` | `value = tuple(check_iter(value))` | src/click/core.py:2305 Parameter#check_iter(). | no edge | name python::.::src/click/core.py::src/click/core/Parameter#type_cast_value().check_iter().#eb… | dev has no node for the target |  |  |  |
| 8 | `src/click/core.py:2345` | `return tuple(convert(x) for x in check_iter(value))` | src/click/core.py:2305 Parameter#check_iter(). | function::src/click/core.py::Parameter.type_cast_value.<locals>.convert | name python::.::src/click/core.py::src/click/core/Parameter#type_cast_value().check_iter().#eb… | dev has no node for the target |  |  |  |
| 9 | `src/click/core.py:2758` | `rv = [_write_opts(self.opts)]` | src/click/core.py:2745 Option#_write_opts(). | function::src/click/core.py::Option.get_help_record.<locals>._write_opts | name python::.::src/click/core.py::src/click/core/Option#get_help_record()._write_opts().#7d9f… | dev has no node for the target |  |  |  |
| 10 | `src/click/shell_completion.py:49` | `echo(comp.complete())` | src/click/utils.py:219 echo(). | no edge | import python::.::src/click/utils.py::src/click/utils/echo().#e6dcab7f |  |  |  |  |
| 11 | `tests/test_arguments.py:129` | `@click.argument("input", type=click.Path(allow_dash=True))` | src/click/types.py:768 Path# | function::src/click/decorators.py::argument | import python::.::src/click/types.py::src/click/types/Path# |  |  |  |  |
| 12 | `tests/test_arguments.py:160` | `@click.argument("output", type=click.File("w"), default="-")` | src/click/types.py:643 File# | function::src/click/decorators.py::argument | import python::.::src/click/types.py::src/click/types/File# |  |  |  |  |
| 13 | `tests/test_basic.py:264` | `@click.option("--file", type=click.File("r"))` | src/click/types.py:643 File# | function::src/click/decorators.py::option | import python::.::src/click/types.py::src/click/types/File# |  |  |  |  |
| 14 | `tests/test_basic.py:387` | `@click.argument("method", type=click.Choice(["foo", "bar", "baz"]))` | src/click/types.py:227 Choice# | function::src/click/decorators.py::argument | import python::.::src/click/types.py::src/click/types/Choice# |  |  |  |  |
| 15 | `tests/test_defaults.py:17` | `@click.command()` | src/click/decorators.py:137 command(). | no edge | import python::.::src/click/decorators.py::src/click/decorators/command().#afa412d0 |  |  |  |  |
| 16 | `tests/test_normalization.py:20` | `@click.option("--choice", type=click.Choice(["Foo", "Bar"]))` | src/click/types.py:227 Choice# | function::src/click/decorators.py::option | import python::.::src/click/types.py::src/click/types/Choice# |  |  |  |  |
| 17 | `tests/test_options.py:354` | `["--in"], type=click.File(), default=__file__, show_default=True` | src/click/types.py:643 File# | no edge | import python::.::src/click/types.py::src/click/types/File# |  |  |  |  |
| 18 | `tests/test_options.py:548` | `@click.command()` | src/click/decorators.py:137 command(). | no edge | import python::.::src/click/decorators.py::src/click/decorators/command().#afa412d0 |  |  |  |  |
| 19 | `tests/test_options.py:549` | `@click.option("--foo", type=click.Choice(["Orange", "Apple"]))` | src/click/types.py:227 Choice# | function::src/click/decorators.py::option | import python::.::src/click/types.py::src/click/types/Choice# |  |  |  |  |
| 20 | `tests/test_options.py:649` | `@click.command()` | src/click/decorators.py:137 command(). | no edge | import python::.::src/click/decorators.py::src/click/decorators/command().#afa412d0 |  |  |  |  |
| 21 | `tests/test_options.py:857` | `@click.command()` | src/click/decorators.py:137 command(). | no edge | import python::.::src/click/decorators.py::src/click/decorators/command().#afa412d0 |  |  |  |  |
| 22 | `tests/test_shell_completion.py:58` | `Group("get", commands=[Command("full")]),` | src/click/core.py:1790 Group# | no edge | import python::.::src/click/core.py::src/click/core/Group# |  |  |  |  |
| 23 | `tests/test_shell_completion.py:267` | `Option(["-b"], type=Choice(["a", "b"]), hidden=True),` | src/click/core.py:2452 Option# | class::src/click/types.py::Choice; method::src/click/types.py::Choice::__init__ | import python::.::src/click/core.py::src/click/core/Option# |  |  |  |  |
| 24 | `tests/test_termui.py:229` | `@click.option("-f", default=__file__, prompt="file", type=click.File(**file_kwargs))` | src/click/types.py:643 File# | function::src/click/decorators.py::option | import python::.::src/click/types.py::src/click/types/File# |  |  |  |  |
| 25 | `tests/test_testing.py:295` | `result = runner.invoke(cli_float_ctx_exit)` | src/click/testing.py:353 CliRunner#invoke(). | no edge | import python::.::src/click/testing.py::src/click/testing/CliRunner#invoke().#19d1892b |  |  |  |  |

## Both miss (25 of 263)
<!-- kind: both_miss -->

Neither engine has a right edge. Check the oracle target first; real rows are shared blind spots.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `examples/imagepipe/imagepipe.py:250` | `@cli.command("sharpen")` | src/click/core.py:1855 Group#command(). | no edge | unresolved unresolved::python::cli.command | reported (dynamic_dispatch) |  |  |  |
| 2 | `examples/termui/termui.py:117` | `@cli.command()` | src/click/core.py:1855 Group#command(). | no edge | unresolved unresolved::python::cli.command | reported (dynamic_dispatch) |  |  |  |
| 3 | `examples/termui/termui.py:144` | `@cli.command()` | src/click/core.py:1855 Group#command(). | no edge | unresolved unresolved::python::cli.command | reported (dynamic_dispatch) |  |  |  |
| 4 | `src/click/_termui_impl.py:217` | `item_info = self.item_show_func(self.current_item)` | src/click/_termui_impl.py:65 ProgressBar#item_show_func. | function::tests/test_termui.py::test_progressbar_format_progress_line_with_show_func.<loc… | unresolved unresolved::python::self.item_show_func | no_node; dev has no node for the target |  |  |  |
| 5 | `src/click/_termui_impl.py:754` | `def raw_terminal() -> t.Iterator[int]:` | src/click/_termui_impl.py:699 raw_terminal(). | no edge | no edge | silent; oracle reads a definition as a call |  |  |  |
| 6 | `src/click/core.py:1743` | `cmd_name = ctx.token_normalize_func(cmd_name)` | src/click/core.py:395 Context#token_normalize_func. | no edge | unresolved unresolved::python::ctx.token_normalize_func | no_node; dev has no node for the target |  |  |  |
| 7 | `src/click/core.py:2238` | `def get_default(` | src/click/core.py:2233 Parameter#get_default(). | no edge | no edge | silent; oracle reads a definition as a call |  |  |  |
| 8 | `src/click/core.py:2345` | `return tuple(convert(x) for x in check_iter(value))` | src/click/core.py:2318 Parameter#convert(). | function::src/click/core.py::Parameter.type_cast_value.<locals>.convert | unresolved unresolved::python::convert | reported (many_candidates); dev has no node for the target |  |  |  |
| 9 | `src/click/core.py:2347` | `return convert(value)` | src/click/core.py:2318 Parameter#convert(). | no edge | unresolved unresolved::python::convert | reported (many_candidates); dev has no node for the target |  |  |  |
| 10 | `src/click/core.py:2365` | `value = self.callback(ctx, self, value)` | src/click/core.py:2130 Parameter#callback. | no edge | unresolved unresolved::python::self.callback | no_node; dev has no node for the target |  |  |  |
| 11 | `src/click/core.py:2440` | `results = self._custom_shell_complete(ctx, self, incomplete)` | src/click/core.py:2138 Parameter#_custom_shell_complete. | no edge | unresolved unresolved::python::self._custom_shell_complete | no_node; dev has no node for the target |  |  |  |
| 12 | `src/click/core.py:2449` | `return self.type.shell_complete(ctx, self, incomplete)` | src/click/types.py:139 ParamType#shell_complete(). | no edge | unresolved unresolved::python::self.type.shell_complete | reported (dynamic_dispatch) |  |  |  |
| 13 | `src/click/decorators.py:167` | `def command(` | src/click/decorators.py:137 command(). | no edge | no edge | silent; oracle reads a definition as a call |  |  |  |
| 14 | `src/click/decorators.py:260` | `def group(` | src/click/decorators.py:254 group(). | no edge | no edge | silent; oracle reads a definition as a call |  |  |  |
| 15 | `src/click/exceptions.py:88` | `_("Error: {message}").format(message=self.format_message()),` | src/click/exceptions.py:38 ClickException#format_message(). | no edge | unresolved unresolved::python::self.format_message | reported (dynamic_dispatch) |  |  |  |
| 16 | `src/click/exceptions.py:176` | `msg_extra = self.param.type.get_missing_message(self.param)` | src/click/types.py:89 ParamType#get_missing_message(). | no edge | unresolved unresolved::python::self.param.type.get_missing_message | reported (dynamic_dispatch) |  |  |  |
| 17 | `src/click/parser.py:124` | `return f"{prefix}{ctx.token_normalize_func(opt)}"` | src/click/core.py:395 Context#token_normalize_func. | no edge | unresolved unresolved::python::ctx.token_normalize_func | no_node; dev has no node for the target |  |  |  |
| 18 | `src/click/types.py:179` | `return self.func(value)` | src/click/types.py:168 FuncParamType#func. | function::src/click/_compat.py::_make_cached_stream_func.<locals>.func | unresolved unresolved::python::self.func | no_node; dev has no node for the target |  |  |  |
| 19 | `src/click/types.py:282` | `ctx.token_normalize_func(normed_choice): original` | src/click/core.py:395 Context#token_normalize_func. | no edge | unresolved unresolved::python::ctx.token_normalize_func | no_node; dev has no node for the target |  |  |  |
| 20 | `src/click/types.py:897` | `self.fail(` | src/click/types.py:130 ParamType#fail(). | no edge | no edge | silent |  |  |  |
| 21 | `tests/test_context.py:317` | `def cli(ctx):` | tests/test_context.py:310 test_exit_not_standalone().cli(). | no edge | no edge | silent; oracle reads a definition as a call |  |  |  |
| 22 | `tests/test_context.py:320` | `assert cli.main([], "test_exit_not_standalone", standalone_mode=False) == 0` | src/click/core.py:995 BaseCommand#main(). | no edge | unresolved unresolved::python::cli.main | reported (many_candidates) |  |  |  |
| 23 | `tests/test_options.py:386` | `def cmd(arg):` | tests/test_options.py:375 test_nargs_envvar().cmd(). | no edge | no edge | silent; oracle reads a definition as a call |  |  |  |
| 24 | `tests/typing/typing_aliased_group.py:26` | `_, cmd, args = super().resolve_command(ctx, args)` | src/click/core.py:1731 MultiCommand#resolve_command(). | no edge | unresolved unresolved::python::super().resolve_command | reported (dynamic_dispatch) |  |  |  |
| 25 | `tests/typing/typing_aliased_group.py:44` | `@cli.command()` | src/click/core.py:1855 Group#command(). | no edge | unresolved unresolved::python::cli.command | reported (dynamic_dispatch) |  |  |  |

## Wrong dev edges (15 of 88 rows, 96 edges)
<!-- kind: dev_wrong -->

A dev edge whose target is none of the line's oracle targets. Check a few: this is where dev's precision goes.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `examples/complex/complex/commands/cmd_init.py:13` | `ctx.log(f"Initialized the repository in {click.format_filename(path)}")` | src/click/utils.py:404 format_filename(). | method::examples/complex/complex/cli.py::Environment::log | python::.::src/click/utils.py::src/click/utils/format_filename().#20f87597 |  |  |  |  |
| 2 | `examples/imagepipe/imagepipe.py:247` | `yield copy_filename(image.filter(ImageFilter.EMBOSS), image)` | examples/imagepipe/imagepipe.py:69 copy_filename(). | function::examples/termui/termui.py::progress.<locals>.filter | python::.::examples/imagepipe/imagepipe.py::examples/imagepipe/imagepipe/copy_filename().… |  |  |  |  |
| 3 | `src/click/core.py:949` | `self.parse_args(ctx, args)` | src/click/core.py:952 BaseCommand#parse_args(). | method::src/click/core.py::MultiCommand::parse_args | no edge |  |  |  |  |
| 4 | `src/click/core.py:1367` | `self.format_options(ctx, formatter)` | src/click/core.py:1387 Command#format_options(). | method::src/click/core.py::MultiCommand::format_options | no edge |  |  |  |  |
| 5 | `src/click/core.py:1553` | `command = self.get_command(ctx, name)` | src/click/core.py:1758 MultiCommand#get_command(). | method::src/click/core.py::Group::get_command | no edge |  |  |  |  |
| 6 | `src/click/core.py:1553` | `command = self.get_command(ctx, name)` | src/click/core.py:1758 MultiCommand#get_command(). | method::src/click/core.py::CommandCollection::get_command | no edge |  |  |  |  |
| 7 | `src/click/core.py:1738` | `cmd = self.get_command(ctx, cmd_name)` | src/click/core.py:1758 MultiCommand#get_command(). | method::src/click/core.py::CommandCollection::get_command | no edge |  |  |  |  |
| 8 | `src/click/decorators.py:45` | `return f(get_current_context().obj, *args, **kwargs)` | src/click/globals.py:13 get_current_context(). | function::tests/test_utils.py::test_prompts_abort.<locals>.f ×2 | python::.::src/click/globals.py::src/click/globals/get_current_context().#8071d4f9 |  |  |  |  |
| 9 | `src/click/shell_completion.py:292` | `args, incomplete = self.get_completion_args()` | src/click/shell_completion.py:256 ShellComplete#get_completion_args(). | method::src/click/shell_completion.py::BashComplete::get_completion_args | no edge |  |  |  |  |
| 10 | `src/click/shell_completion.py:292` | `args, incomplete = self.get_completion_args()` | src/click/shell_completion.py:256 ShellComplete#get_completion_args(). | method::src/click/shell_completion.py::ZshComplete::get_completion_args | no edge |  |  |  |  |
| 11 | `src/click/shell_completion.py:294` | `out = [self.format_completion(item) for item in completions]` | src/click/shell_completion.py:277 ShellComplete#format_completion(). | method::src/click/shell_completion.py::BashComplete::format_completion | no edge |  |  |  |  |
| 12 | `src/click/types.py:464` | `return self._clamp(self.min, 1, self.min_open)  # type: ignore` | src/click/types.py:480 _NumberRangeBase#_clamp(). | method::src/click/types.py::FloatRange::_clamp | no edge |  |  |  |  |
| 13 | `tests/test_context.py:42` | `ctx.obj = Foo()` | tests/test_context.py:33 test_get_context_objects().Foo# | class::tests/test_context.py::test_ensure_context_objects.<locals>.Foo | python::.::tests/test_context.py::tests/test_context/test_get_context_objects().Foo#; python::.::tests/test_context.py::tests/test_context/test_get_context_objects().Foo#__ini… |  |  |  |  |
| 14 | `tests/test_context.py:270` | `ctx.obj = Foo()` | tests/test_context.py:262 test_make_pass_decorator_args().Foo# | class::tests/test_context.py::test_ensure_context_objects.<locals>.Foo | python::.::tests/test_context.py::tests/test_context/test_make_pass_decorator_args().Foo# |  |  |  |  |
| 15 | `tests/test_termui.py:65` | `with click.progressbar(Hinted(10), label="test") as progress:` | src/click/termui.py:283 progressbar().; tests/test_termui.py:45 test_progressbar_length_hint().Hinted# | method::tests/test_termui.py::test_progressbar_length_hint.<locals>.Hinted::__init__ ×2 | python::.::src/click/_termui_impl.py::src/click/_termui_impl/ProgressBar#__enter__().#f90…; python::.::src/click/_termui_impl.py::src/click/_termui_impl/ProgressBar#__exit__().#0699…; python::.::src/click/termui.py::src/click/termui/progressbar().#56cfc6c5; python::.::tests/test_termui.py::tests/test_termui/test_progressbar_length_hint().Hinted#; python::.::tests/test_termui.py::tests/test_termui/test_progressbar_length_hint().Hinted#… |  |  |  |  |

## v2 edges the score cannot judge (10 of 644)
<!-- kind: v2_unscored -->

v2 edges on lines where the oracle has no call with a target v2 has a node for. Not in any score. Look for calls the oracle misses (v2 right, oracle silent) and for v2 edges that are plainly wrong.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `src/click/_termui_impl.py:651` | `url = _unquote_file(url)` | no oracle call with a target | no edge | name python::.::src/click/_termui_impl.py::src/click/_termui_impl/open_url()._unquote_file().#… (at call site: yes) |  |  |  |  |
| 2 | `src/click/_winconsole.py:50` | `STDOUT_HANDLE = GetStdHandle(-11)` | no oracle call with a target | no edge | name python::.::src/click/_winconsole.py::src/click/_winconsole/GetStdHandle. (at call site: yes) |  |  |  |  |
| 3 | `src/click/_winconsole.py:94` | `buf = Py_buffer()` | no oracle call with a target | class::src/click/_winconsole.py::Py_buffer | name python::.::src/click/_winconsole.py::src/click/_winconsole/Py_buffer# (at call site: yes) |  |  |  |  |
| 4 | `src/click/_winconsole.py:167` | `WriteConsoleW(` | no oracle call with a target | no edge | name python::.::src/click/_winconsole.py::src/click/_winconsole/WriteConsoleW. (at call site: yes) |  |  |  |  |
| 5 | `src/click/_winconsole.py:270` | `and _is_console(f)` | no oracle call with a target | function::src/click/_winconsole.py::_is_console | name python::.::src/click/_winconsole.py::src/click/_winconsole/_is_console().#84b923d0 (at call site: yes) |  |  |  |  |
| 6 | `tests/test_basic.py:67` | `result = runner.invoke(cli, ["--help"])` | no oracle call with a target | method::src/click/testing.py::CliRunner::invoke | name python::.::src/click/testing.py::src/click/testing/CliRunner#invoke().#19d1892b (at call site: no) |  |  |  |  |
| 7 | `tests/test_basic.py:292` | `with runner.isolated_filesystem():` | no oracle call with a target | method::src/click/testing.py::CliRunner::isolated_filesystem | name python::.::src/click/testing.py::src/click/testing/CliRunner#isolated_filesystem().#8f422… (at call site: no) |  |  |  |  |
| 8 | `tests/test_basic.py:347` | `result = runner.invoke(showtype, ["-f", "."])` | no oracle call with a target | no edge | name python::.::src/click/testing.py::src/click/testing/CliRunner#invoke().#19d1892b (at call site: no) |  |  |  |  |
| 9 | `tests/test_normalization.py:37` | `result = runner.invoke(cli, ["FOO"])` | no oracle call with a target | method::src/click/testing.py::CliRunner::invoke | name python::.::src/click/testing.py::src/click/testing/CliRunner#invoke().#19d1892b (at call site: no) |  |  |  |  |
| 10 | `tests/test_options.py:492` | `assert result.output == "42\n"` | no oracle call with a target | no edge | name python::.::src/click/testing.py::src/click/testing/Result#output().#f9065fa7 (at call site: no) |  |  |  |  |

## dev edges the score cannot judge (10 of 383 rows, 418 edges)
<!-- kind: dev_unscored -->

The same for dev.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `src/click/core.py:2758` | `rv = [_write_opts(self.opts)]` | no oracle call with a target | function::src/click/core.py::Option.get_help_record.<locals>._write_opts | python::.::src/click/core.py::src/click/core/Option#get_help_record()._write_opts().#7d9f… |  |  |  |  |
| 2 | `src/click/testing.py:294` | `char = sys.stdin.read(1)` | no oracle call with a target | method::src/click/testing.py::EchoingStdin::read ×2 | no edge |  |  |  |  |
| 3 | `src/click/utils.py:556` | `and not os.path.exists(path)` | no oracle call with a target | function::tests/test_basic.py::test_path_option.<locals>.exists | no edge |  |  |  |  |
| 4 | `tests/test_basic.py:250` | `result = runner.invoke(cli, ["--flag", value])` | no oracle call with a target | method::src/click/testing.py::CliRunner::invoke | python::.::src/click/testing.py::src/click/testing/CliRunner#invoke().#19d1892b |  |  |  |  |
| 5 | `tests/test_command_decorators.py:70` | `result = runner.invoke(cli, ["1", "2"])` | no oracle call with a target | method::src/click/testing.py::CliRunner::invoke | python::.::src/click/testing.py::src/click/testing/CliRunner#invoke().#19d1892b |  |  |  |  |
| 6 | `tests/test_context.py:364` | `return ctx.get_parameter_source("option")` | no oracle call with a target | method::src/click/core.py::Context::get_parameter_source ×2 | no edge |  |  |  |  |
| 7 | `tests/test_defaults.py:76` | `result = runner.invoke(cli, ["foo"])` | no oracle call with a target | method::src/click/testing.py::CliRunner::invoke | python::.::src/click/testing.py::src/click/testing/CliRunner#invoke().#19d1892b |  |  |  |  |
| 8 | `tests/test_formatting.py:106` | `result = runner.invoke(` | no oracle call with a target | method::src/click/testing.py::CliRunner::invoke | python::.::src/click/testing.py::src/click/testing/CliRunner#invoke().#19d1892b |  |  |  |  |
| 9 | `tests/test_testing.py:239` | `sys.exit("error")` | no oracle call with a target | method::src/click/core.py::Context::exit ×2 | no edge |  |  |  |  |
| 10 | `tests/test_testing.py:256` | `ctx.exit(1)` | no oracle call with a target | method::src/click/core.py::Context::exit | no edge |  |  |  |  |

## Both right (spot check) (10 of 990)
<!-- kind: both_right -->

The machine says both engines are right. Check a few: if these are wrong, every score is too high.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `src/click/_termui_impl.py:126` | `return self.generator()` | src/click/_termui_impl.py:328 ProgressBar#generator(). | method::src/click/_termui_impl.py::ProgressBar::generator | name python::.::src/click/_termui_impl.py::src/click/_termui_impl/ProgressBar#generator().#f90… |  |  |  |  |
| 2 | `src/click/_termui_impl.py:356` | `self.update(1)` | src/click/_termui_impl.py:297 ProgressBar#update(). | method::src/click/_termui_impl.py::ProgressBar::update | name python::.::src/click/_termui_impl.py::src/click/_termui_impl/ProgressBar#update().#ba323d… |  |  |  |  |
| 3 | `src/click/exceptions.py:73` | `file = get_text_stderr()` | src/click/_compat.py:351 get_text_stderr(). | function::src/click/_compat.py::get_text_stderr | import python::.::src/click/_compat.py::src/click/_compat/get_text_stderr().#bad01aa7 |  |  |  |  |
| 4 | `tests/test_arguments.py:203` | `@click.argument("arg", envvar="X", nargs=-1)` | src/click/decorators.py:315 argument(). | function::src/click/decorators.py::argument | import python::.::src/click/decorators.py::src/click/decorators/argument().#34329f1c |  |  |  |  |
| 5 | `tests/test_basic.py:211` | `@click.option("--on/--off", default=default)` | src/click/decorators.py:343 option(). | function::src/click/decorators.py::option | import python::.::src/click/decorators.py::src/click/decorators/option().#448c9f20 |  |  |  |  |
| 6 | `tests/test_commands.py:500` | `@click.option("!e", is_flag=True)` | src/click/decorators.py:343 option(). | function::src/click/decorators.py::option | import python::.::src/click/decorators.py::src/click/decorators/option().#448c9f20 |  |  |  |  |
| 7 | `tests/test_custom_classes.py:16` | `context = command.make_context("test", [])` | src/click/core.py:910 BaseCommand#make_context(). | method::src/click/core.py::BaseCommand::make_context | name python::.::src/click/core.py::src/click/core/BaseCommand#make_context().#465c52b6 |  |  |  |  |
| 8 | `tests/test_options.py:206` | `@click.option("--shout/--no-shout", envvar="SHOUT")` | src/click/decorators.py:343 option(). | function::src/click/decorators.py::option | import python::.::src/click/decorators.py::src/click/decorators/option().#448c9f20 |  |  |  |  |
| 9 | `tests/test_options.py:275` | `@click.option(` | src/click/decorators.py:343 option(). | function::src/click/decorators.py::option | import python::.::src/click/decorators.py::src/click/decorators/option().#448c9f20 |  |  |  |  |
| 10 | `tests/test_options.py:714` | `@click.option(*option_args, is_flag=True)` | src/click/decorators.py:343 option(). | function::src/click/decorators.py::option | import python::.::src/click/decorators.py::src/click/decorators/option().#448c9f20 |  |  |  |  |

