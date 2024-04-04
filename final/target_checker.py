from target_invoker import JSON_target_invoker
from target_identifier import Target_identifier

class target_checker:
    def __init__(self):
        self.target_identifier = Target_identifier()
        self.json_targets = self.target_identifier.JSON_targets
        self.makefile_targets = self.target_identifier.targets
        self.found_targets = self.check_targets(self.json_targets, self.makefile_targets)
    def check_targets(self, json_targets, makefile_targets):
        match = [x for x in json_targets if x in makefile_targets]
        return match

#class usage
TC = target_checker()
targets_matched = TC.found_targets
print(targets_matched)
