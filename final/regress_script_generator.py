from target_builder import Target_builder

class RegressGenerator:
    def __init__(self):
        self.TB = Target_builder()
        self.targets_built = self.TB.build
        print(f"*****Targets successfully built are: {self.targets_built}*****")
    def generate_regress(self, built_targets)
#class usage
RG =RegressGenerator()

