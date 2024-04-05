import makefile_reader
from target_invoker import target_invoker

makefile_targets = makefile_reader.target_list
json_targets = target_invoker.get_targets()
print(f"makefile Targets are: {makefile_targets}")
print(f"json targets are: {json_targets}")
found_targets = [x for x in json_targets if x in makefile_targets]
print(f"found targets are: {found_targets}")

