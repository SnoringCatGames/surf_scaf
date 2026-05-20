# SurfScaf

_This is still under development and not ready for use._

This project defines a GDExtension that is the combination of the
[Surfacer](https://github.com/SnoringCatGames/surfacer),
[Scaffolder](https://github.com/SnoringCatGames/scaffolder), and
[SnoreCore](https://github.com/SnoringCatGames/snore_core) GDExtensions.

This dedicated combination super extension must exist, because Godot currently doesn't support one GDExtension depending on another. See [godot-rust/gdext#615](https://github.com/godot-rust/gdext/issues/615) and [godotengine/godot-proposals#13997](https://github.com/godotengine/godot-proposals/issues/13997).

## Building

This repo expects a **workspace-sibling layout** — see [bootstrapper](https://github.com/SnoringCatGames/bootstrapper) for the umbrella project and `scripts/bootstrap-workspace.ps1`, which clones all required sibling repos (snore_core, scaffolder, surfacer, godot-cpp, googletest, godot) into the workspace root in one go. Once siblings are in place, build with `scons sc_dev=yes sc_tests=yes` from this directory.
