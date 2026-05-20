import glob
import os
import sys

# Workspace-sibling layout: snore_core / scaffolder / surfacer live next to
# surf_scaf, not nested under it.
sys.path.insert(0, os.path.abspath(".."))

from snore_core.build_utils import print_error


default_lib_name = "SurfScaf"
default_addon_dir_name = "surf_scaf"


def set_up(
    env: object,
    cpp_paths: list[str],
    sources: list[str],
    surf_scaf_addon_dir_name: str,
    is_setup_for_self=False,
) -> None:
    for sibling in ("snore_core", "scaffolder", "surfacer"):
        if not os.path.isdir("../" + sibling):
            print_error(
                "../{} must be a workspace-sibling directory.\n"
                "Run scripts/bootstrap-workspace.ps1 from the bootstrapper "
                "repo to clone all required siblings.".format(sibling)
            )
            sys.exit(1)

    src_path = (
        is_setup_for_self
        and "src/"
        or "../{}/src/".format(surf_scaf_addon_dir_name)
    )
    cpp_paths.extend([src_path])
    sources.extend(glob.glob("{}**/*.cpp".format(src_path), recursive=True))
