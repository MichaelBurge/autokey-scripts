old_level = int(store.get_global_value("TITAN_LEVEL") or 0)
new_level = dialog.input_dialog(message="Current level = %d" % old_level)[1]
store.set_global_value("TITAN_LEVEL", new_level)
