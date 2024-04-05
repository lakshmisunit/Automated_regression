import re 

class Makefile:
    def read(self, fpath):
        data = self.read_data(fpath)
        self.vars = self.get_targets(data)
        return self.vars

    def read_data(self, fpath):
        with open(fpath) as fp:
            return fp.readlines()

    def get_targets(self, data):
        targets = []
        target_pattern = re.compile(r'^([a-zA-Z0-9_]+)\s*:')
        for line in data:
            match = target_pattern.match(line)
            if (match):
                target = match.group(1)
                targets.append(target)
        return targets

#class_usage
#if __name__ == "__main__":
#    make = Makefile()
#    print(make.read('Makefile'))
        
