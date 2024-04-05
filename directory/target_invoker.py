from JSONReader import JSONDataReader
import sys
#jsonreader = JSONReader('sys.argv[1]')

class target_invoker:
    def get_targets():
        jsonreader = JSONDataReader(sys.argv[2])
        target_list = jsonreader.extract_values('target')
        return target_list

#usage
TI = target_invoker
target_list = TI.get_targets()
#print(target_list)
