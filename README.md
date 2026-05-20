# surf_scaf

> **Status: rewrite in progress.** This branch (`main`) is intentionally
> minimal during active development; the real code lives on `dev`.

A "combined" Godot 4 GDExtension that bundles
[snore_core](https://github.com/SnoringCatGames/snore_core),
[scaffolder](https://github.com/SnoringCatGames/scaffolder), and
[surfacer](https://github.com/SnoringCatGames/surfacer) into a single
binary. Required because Godot 4 currently does not support one
GDExtension depending on another GDExtension's classes (see
[godot-rust/gdext#615](https://github.com/godot-rust/gdext/issues/615)
and [godot-proposals#13997](https://github.com/godotengine/godot-proposals/issues/13997)).

## Branches

| Branch | Content |
|---|---|
| `main` (this) | Minimal during the rewrite — just this README. |
| `dev` | Active Godot 4 + C++/GDExtension development. |

## Where to go next

- Current work in progress: `git checkout dev`
- Umbrella project: [bootstrapper](https://github.com/SnoringCatGames/bootstrapper)
