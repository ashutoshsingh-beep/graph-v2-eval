# cobra: v2 against the scip-go oracle, 20 sampled disagreements

Commit `88b30ab89da2d0d0abb153818746c5a2d30eccec`, v2 `b3cd5e698314`, seed `20261031:cobra`.
Neither side is assumed right. Fill the verdict column with v2, oracle, both or neither.

| # | file:line | source | v2 | oracle | verdict |
|---|---|---|---|---|---|
| 1 | `bash_completions.go:602` | `if flag.Value.Type() != "bool" {` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::go::flag.Value.Type` | `external github.com/spf13/pflag:github.com/spf13/pflag` | |
| 2 | `bash_completions_test.go:68` | `_, err := stdin.Write([]byte(s))` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::go::stdin.Write` | `external go-stdlib:io` | |
| 3 | `bash_completions_test.go:71` | `stdin.Close()` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::go::stdin.Close` | `external go-stdlib:io` | |
| 4 | `cobra.go:244` | `_, err := b.WriteString(s)` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::go::b.WriteString` | `external go-stdlib:io` | |
| 5 | `command.go:1329` | `func (c commandSorterByName) Less(i, j int) bool { return c[i].Name() < c[j].Name() }` | v2_unresolved_or_absent: `no CALLS edge at this site` | `command.go:1541 Command#Name().` | |
| 6 | `command.go:1329` | `func (c commandSorterByName) Less(i, j int) bool { return c[i].Name() < c[j].Name() }` | v2_unresolved_or_absent: `no CALLS edge at this site` | `command.go:1541 Command#Name().` | |
| 7 | `command_test.go:2609` | `key := cmd.Context().Value(key{})` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::go::cmd.Context().Value` | `external go-stdlib:context` | |
| 8 | `command_test.go:2638` | `val := cmd.Context().Value(key{})` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::go::cmd.Context().Value` | `external go-stdlib:context` | |
| 9 | `command_test.go:2660` | `key := cmd.Context().Value(key{})` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::go::cmd.Context().Value` | `external go-stdlib:context` | |
| 10 | `command_test.go:2688` | `key := cmd.Context().Value(key{})` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::go::cmd.Context().Value` | `external go-stdlib:context` | |
| 11 | `command_test.go:2934` | `_, err := cmd.OutOrStdout().Write([]byte(helpText))` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::go::cmd.OutOrStdout().Write` | `external go-stdlib:io` | |
| 12 | `completions.go:447` | `strings.Contains(flag.Value.Type(), "Slice") \|\|` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::go::flag.Value.Type` | `external github.com/spf13/pflag:github.com/spf13/pflag` | |
| 13 | `completions.go:448` | `strings.Contains(flag.Value.Type(), "Array") \|\|` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::go::flag.Value.Type` | `external github.com/spf13/pflag:github.com/spf13/pflag` | |
| 14 | `completions.go:449` | `strings.HasPrefix(flag.Value.Type(), "stringTo")` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::go::flag.Value.Type` | `external github.com/spf13/pflag:github.com/spf13/pflag` | |
| 15 | `completions_test.go:1282` | `} else if ctx.Value("testKey") != "123" {` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::go::ctx.Value` | `external go-stdlib:context` | |
| 16 | `doc/man_docs.go:114` | `_, err := w.Write(md2man.Render(b))` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::go::w.Write` | `external go-stdlib:io` | |
| 17 | `doc/man_docs.go:173` | `if flag.Value.Type() == "string" {` | v2_unresolved_or_absent: `unresolved R8 dynamic_dispatch unresolved::go::flag.Value.Type` | `external github.com/spf13/pflag:github.com/spf13/pflag` | |
| 18 | `doc/util.go:52` | `func (s byName) Less(i, j int) bool { return s[i].Name() < s[j].Name() }` | v2_unresolved_or_absent: `no CALLS edge at this site` | `command.go:1541 Command#Name().` | |
| 19 | `doc/util.go:52` | `func (s byName) Less(i, j int) bool { return s[i].Name() < s[j].Name() }` | v2_unresolved_or_absent: `no CALLS edge at this site` | `command.go:1541 Command#Name().` | |
| 20 | `doc/yaml_docs.go:143` | `if _, err := w.Write(final); err != nil {` | v2_unresolved_or_absent: `unresolved R8 no_candidate unresolved::go::w.Write` | `external go-stdlib:io` | |
