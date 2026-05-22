class_name DemoLevel
extends ScaffolderLevel


func _ready() -> void:
    # TODO: Re-enable super._ready() once C++ ScaffolderLevel
    # exposes _ready via _bind_methods. The GDScript parser
    # rejects calls to virtual overrides on GDExtension parents
    # that aren't bound, even though they exist at runtime.
    G.level = self
