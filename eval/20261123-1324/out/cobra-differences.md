# cobra (go): graph differences to verify

Repo `https://github.com/spf13/cobra` at `88b30ab89da2d0d0abb153818746c5a2d30eccec`. Old engine `25ae40bf8662`, graph v2 `b3cd5e698314`.

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

In-repo calls found by the oracle: 2192. Both right 1500, gap 2, v2 gain 690, both miss 0.
Scored edges: v2 2202 (0 wrong), dev 1502 (0 wrong). Not scored: v2 25, dev 0.
CALLS recall: dev 68.5% (1502/2192), v2 99.9% (2190/2192). CALLS precision: dev 100.0% (1502/1502), v2 100.0% (2202/2202).
Line precision judges each engine only on lines where the oracle has a call it can map, and counts edges that sit on no oracle call (decorator lines) as wrong. Do not rank the engines on it alone.
v2 precision at exact call sites (published): 1.0.
Flags: {"dev_multi_both_right": 269} (def_line_* = the line defines a function of the target's own name, usually the oracle's mistake; dev_multi_* = dev was right but had several targets on the line).
Scorer notes: {"dev_edges_with_file_source_never_scored": 0, "dev_calls_without_site_line": 0}.
Check against the published scores: OK (full).

## How each v2 miss happened

| group | v2 miss | reason | calls |
|---|---|---|---|
| gap | silent | - | 2 |

`no_node`: v2 has no node for the target. `wrong_target`: v2 resolved this call to another target. `external`: v2 called it external. `reported`: only unresolved edges, with v2's reason. `silent`: no v2 edge at this call at all.

Verdict: `confirmed` (the row is what its group says), `oracle wrong`, `dev wrong`, `v2 right after all`, or `?`.
Cause: one short phrase for the code shape (for example `method on a constructor-injected field`). Reuse phrases.
Reason true: for a `reported` miss, `yes` or `no`.

## Gaps: dev is right, v2 is not (2 of 2)
<!-- kind: gap -->

What v2 loses against the old engine. Check: is the oracle target right, does dev's edge really go there, and is v2 really wrong?

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `command.go:1329` | `func (c commandSorterByName) Less(i, j int) bool { return c[i].Name() < c[j].Name() }` | command.go:1541 Command#Name(). | method::command.go::Command::Name | no edge | silent |  |  |  |
| 2 | `doc/util.go:52` | `func (s byName) Less(i, j int) bool { return s[i].Name() < s[j].Name() }` | command.go:1541 Command#Name(). | method::command.go::Command::Name | no edge | silent |  |  |  |

## Wrong v2 edges (0 of 0)
<!-- kind: v2_wrong -->

A v2 edge on a line where the oracle has a call, whose target is none of that line's oracle targets. `at call site: no` means the edge sits on no call the oracle saw (for example a decorator line). Check: is v2's target wrong?

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|

## v2 gains: v2 is right, dev is not (25 of 690)
<!-- kind: v2_gain -->

What v2 adds. Verify a few so the gain is real.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `active_help_test.go:185` | `comps = AppendActiveHelp(comps, activeHelpMessage2)` | active_help.go:38 AppendActiveHelp(). | no edge | exact go::.::active_help.go::AppendActiveHelp().#6e9dcefe |  |  |  |  |
| 2 | `active_help_test.go:207` | `comps = AppendActiveHelp(comps, activeHelpMessage)` | active_help.go:38 AppendActiveHelp(). | no edge | exact go::.::active_help.go::AppendActiveHelp().#6e9dcefe |  |  |  |  |
| 3 | `bash_completions.go:453` | `WriteStringAndCheck(buf, fmt.Sprintf("    commands+=(%q)\n", c.Name()))` | cobra.go:243 WriteStringAndCheck(). | method::command.go::Command::Name | exact go::.::cobra.go::WriteStringAndCheck().#cf7e9380 |  |  |  |  |
| 4 | `bash_completions_test.go:96` | `assertNoErr(t, rootCmd.MarkFlagFilename("filename", "json", "yaml", "yml"))` | cobra_test.go:27 assertNoErr(). | method::shell_completions.go::Command::MarkFlagFilename | exact go::.::cobra_test.go::assertNoErr().#a5a1273a |  |  |  |  |
| 5 | `bash_completions_test.go:107` | `assertNoErr(t, rootCmd.MarkFlagCustom("custom", "__complete_custom"))` | cobra_test.go:27 assertNoErr(). | method::shell_completions.go::Command::MarkFlagCustom | exact go::.::cobra_test.go::assertNoErr().#a5a1273a |  |  |  |  |
| 6 | `bash_completions_test.go:197` | `checkRegex(t, output, fmt.Sprintf(`_root_echo\(\)\n{[^}]*flags_completion\+=\("__%s_handle_filename_extension_flag json\` | command.go:1541 Command#Name(). | function::bash_completions_test.go::checkRegex | exact go::.::command.go::Command#Name().#f9065fa7 |  |  |  |  |
| 7 | `bash_completions_test.go:213` | `check(t, output, `local_nonpersistent_flags+=("--two=")`)` | bash_completions_test.go:33 check(). | no edge | exact go::.::bash_completions_test.go::check().#b9381bad |  |  |  |  |
| 8 | `command.go:489` | `return c.Parent().HelpFunc()` | command.go:484 Command#HelpFunc(). | method::command.go::Command::Parent | exact go::.::command.go::Command#HelpFunc().#f9065fa7 |  |  |  |  |
| 9 | `command.go:1306` | `CheckErr(cmd.Help())` | cobra.go:235 CheckErr(). | method::command.go::Command::Help | exact go::.::cobra.go::CheckErr().#ec1078cf |  |  |  |  |
| 10 | `command.go:1512` | `c.Println("  -"+f.Shorthand+",", "--"+f.Name, "["+f.DefValue+"]", "", f.Value, "  [LP]")` | command.go:1440 Command#Println(). | no edge | exact go::.::command.go::Command#Println().#79140da9 |  |  |  |  |
| 11 | `command.go:1991` | `if c.HasAvailableSubCommands() {` | command.go:1662 Command#HasAvailableSubCommands(). | no edge | exact go::.::command.go::Command#HasAvailableSubCommands().#f9065fa7 |  |  |  |  |
| 12 | `command.go:2031` | `fmt.Fprintf(w, "\n  %s %s", rpad(subcmd.CommandPath(), subcmd.CommandPathPadding()), subcmd.Short)` | command.go:1465 Command#CommandPath(). | method::command.go::Command::CommandPathPadding | exact go::.::command.go::Command#CommandPath().#f9065fa7 |  |  |  |  |
| 13 | `command_test.go:859` | `c.Flags().String("bar", "", "")` | command.go:1688 Command#Flags(). | no edge | exact go::.::command.go::Command#Flags().#f9065fa7 |  |  |  |  |
| 14 | `command_test.go:881` | `assertNoErr(t, child.MarkFlagRequired("bar1"))` | cobra_test.go:27 assertNoErr(). | method::shell_completions.go::Command::MarkFlagRequired | exact go::.::cobra_test.go::assertNoErr().#a5a1273a |  |  |  |  |
| 15 | `command_test.go:2325` | `rootCmd.Flags().BoolP("bool", "b", false, "")` | command.go:1688 Command#Flags(). | no edge | exact go::.::command.go::Command#Flags().#f9065fa7 |  |  |  |  |
| 16 | `completions.go:399` | `finalArgs = finalCmd.Flags().Args()` | command.go:1688 Command#Flags(). | no edge | exact go::.::command.go::Command#Flags().#f9065fa7 |  |  |  |  |
| 17 | `completions.go:893` | `return cmd.Root().GenFishCompletion(out, !noDesc)` | command.go:892 Command#Root(). | method::fish_completions.go::Command::GenFishCompletion | exact go::.::command.go::Command#Root().#f9065fa7 |  |  |  |  |
| 18 | `completions.go:918` | `return cmd.Root().GenPowerShellCompletionWithDesc(out)` | command.go:892 Command#Root(). | method::powershell_completions.go::Command::GenPowerShellCompletionWithDesc | exact go::.::command.go::Command#Root().#f9065fa7 |  |  |  |  |
| 19 | `completions_test.go:2547` | `assertNoErr(t, rootCmd.Execute())` | cobra_test.go:27 assertNoErr(). | no edge | exact go::.::cobra_test.go::assertNoErr().#a5a1273a |  |  |  |  |
| 20 | `completions_test.go:3010` | `choices := []string{"apple", Completion("banana"), CompletionWithDesc("orange", "orange are orange")}` | completions.go:136 Completion# | function::completions.go::CompletionWithDesc | exact go::.::completions.go::Completion# |  |  |  |  |
| 21 | `doc/cmd_test.go:31` | `echoCmd.PersistentFlags().BoolP("persistentbool", "p", false, "help message for flag persistentbool")` | command.go:1775 Command#PersistentFlags(). | no edge | exact go::.::command.go::Command#PersistentFlags().#f9065fa7 |  |  |  |  |
| 22 | `doc/man_docs_test.go:59` | `checkStringContains(t, output, translate(echoCmd.Name()))` | doc/cmd_test.go:95 checkStringContains(). | method::command.go::Command::Name | exact go::.::doc/cmd_test.go::doc/checkStringContains().#b9381bad |  |  |  |  |
| 23 | `doc/man_docs_test.go:95` | `checkStringContains(t, output, translate(echoCmd.Name()))` | doc/cmd_test.go:95 checkStringContains(). | no edge | exact go::.::doc/cmd_test.go::doc/checkStringContains().#b9381bad |  |  |  |  |
| 24 | `doc/md_docs_test.go:78` | `checkStringOmits(t, output, "Options inherited from parent commands")` | doc/cmd_test.go:101 checkStringOmits(). | no edge | exact go::.::doc/cmd_test.go::doc/checkStringOmits().#b9381bad |  |  |  |  |
| 25 | `fish_completions_test.go:86` | `checkOmit(t, output, "-c root_colon")` | bash_completions_test.go:27 checkOmit(). | no edge | exact go::.::bash_completions_test.go::checkOmit().#b9381bad |  |  |  |  |

## Both miss (0 of 0)
<!-- kind: both_miss -->

Neither engine has a right edge. Check the oracle target first; real rows are shared blind spots.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|

## Wrong dev edges (0 of 0)
<!-- kind: dev_wrong -->

A dev edge whose target is none of the line's oracle targets. Check a few: this is where dev's precision goes.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|

## v2 edges the score cannot judge (10 of 25)
<!-- kind: v2_unscored -->

v2 edges on lines where the oracle has no call with a target v2 has a node for. Not in any score. Look for calls the oracle misses (v2 right, oracle silent) and for v2 edges that are plainly wrong.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `command_test.go:1733` | `validateHook(args, "parent PersistentPreRun")` | no oracle call with a target | no edge | exact go::.::command_test.go::testPersistentHooks().validateHook().#49ae76b5 (at call site: yes) |  |  |  |  |
| 2 | `command_test.go:1745` | `validateHook(args, "parent PersistentPostRun")` | no oracle call with a target | no edge | exact go::.::command_test.go::testPersistentHooks().validateHook().#49ae76b5 (at call site: yes) |  |  |  |  |
| 3 | `command_test.go:1758` | `validateHook(args, "child Run")` | no oracle call with a target | no edge | exact go::.::command_test.go::testPersistentHooks().validateHook().#49ae76b5 (at call site: yes) |  |  |  |  |
| 4 | `command_win.go:32` | `c.Print(MousetrapHelpText)` | no oracle call with a target | no edge | name go::.::command.go::Command#Print().#79140da9 (at call site: no) |  |  |  |  |
| 5 | `command_win.go:36` | `c.Println("Press return to continue...")` | no oracle call with a target | no edge | name go::.::command.go::Command#Println().#79140da9 (at call site: no) |  |  |  |  |
| 6 | `completions_test.go:678` | `var _ SliceValue = (*customMultiString)(nil)` | no oracle call with a target | no edge | exact go::.::completions_test.go::customMultiString# (at call site: no) |  |  |  |  |
| 7 | `completions_test.go:3241` | `c := getCmd()` | no oracle call with a target | no edge | exact go::.::completions_test.go::TestCompletionForOneRequiredGroupFlags().getCmd().#f9065fa7 (at call site: yes) |  |  |  |  |
| 8 | `completions_test.go:3335` | `c := getCmd()` | no oracle call with a target | no edge | exact go::.::completions_test.go::TestCompletionForMutuallyExclusiveFlags().getCmd().#f9065fa7 (at call site: yes) |  |  |  |  |
| 9 | `completions_test.go:3916` | `run()` | no oracle call with a target | no edge | exact go::.::completions_test.go::TestDisableDescriptions().run().#f9065fa7 (at call site: yes) |  |  |  |  |
| 10 | `flag_groups_test.go:165` | `c := getCmd()` | no oracle call with a target | no edge | exact go::.::flag_groups_test.go::TestValidateFlagGroups().getCmd().#f9065fa7 (at call site: yes) |  |  |  |  |

## dev edges the score cannot judge (0 of 0)
<!-- kind: dev_unscored -->

The same for dev.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|

## Both right (spot check) (10 of 1500)
<!-- kind: both_right -->

The machine says both engines are right. Check a few: if these are wrong, every score is too high.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `bash_completions.go:594` | `WriteStringAndCheck(buf, "    must_have_one_flag=()\n")` | cobra.go:243 WriteStringAndCheck(). | function::cobra.go::WriteStringAndCheck | exact go::.::cobra.go::WriteStringAndCheck().#cf7e9380 |  |  |  |  |
| 2 | `command.go:1690` | `c.flags = flag.NewFlagSet(c.DisplayName(), flag.ContinueOnError)` | command.go:1474 Command#DisplayName(). | method::command.go::Command::DisplayName | exact go::.::command.go::Command#DisplayName().#f9065fa7 |  |  |  |  |
| 3 | `command.go:1899` | `c.updateParentsPflags()` | command.go:1907 Command#updateParentsPflags(). | method::command.go::Command::updateParentsPflags | exact go::.::command.go::Command#updateParentsPflags().#f9065fa7 |  |  |  |  |
| 4 | `command_test.go:246` | `childCmd.AddCommand(granchildCmd)` | command.go:1342 Command#AddCommand(). | method::command.go::Command::AddCommand | exact go::.::command.go::Command#AddCommand().#018ed86d |  |  |  |  |
| 5 | `command_test.go:1098` | `output, err := executeCommand(parentCmd, "help", "child")` | command_test.go:32 executeCommand(). | function::command_test.go::executeCommand | exact go::.::command_test.go::executeCommand().#937a0262 |  |  |  |  |
| 6 | `completions.go:297` | `subCmd, _, err := c.Find(args)` | command.go:757 Command#Find(). | method::command.go::Command::Find | exact go::.::command.go::Command#Find().#36227eb4 |  |  |  |  |
| 7 | `completions_test.go:1629` | `rootCmd.Flags().IntP("introot", "i", -1, "help message for flag introot")` | command.go:1688 Command#Flags(). | method::command.go::Command::Flags | exact go::.::command.go::Command#Flags().#f9065fa7 |  |  |  |  |
| 8 | `doc/rest_docs.go:116` | `if !child.IsAvailableCommand() \|\| child.IsAdditionalHelpTopicCommand() {` | command.go:1628 Command#IsAdditionalHelpTopicCommand(). | method::command.go::Command::IsAdditionalHelpTopicCommand; method::command.go::Command::IsAvailableCommand | exact go::.::command.go::Command#IsAdditionalHelpTopicCommand().#f9065fa7 | dev has 2 targets on this line |  |  |  |
| 9 | `doc/yaml_docs.go:161` | `forceMultiLine(flag.Usage),` | doc/util.go:41 forceMultiLine(). | function::doc/util.go::forceMultiLine | exact go::.::doc/util.go::doc/forceMultiLine().#fb4e25e4 |  |  |  |  |
| 10 | `fish_completions_test.go:52` | `assertNoErr(t, rootCmd.GenFishCompletion(buf, true))` | cobra_test.go:27 assertNoErr(). | function::cobra_test.go::assertNoErr; method::fish_completions.go::Command::GenFishCompletion | exact go::.::cobra_test.go::assertNoErr().#a5a1273a | dev has 2 targets on this line |  |  |  |

