

from datetime import date,datetime
import json

d = {'name':'chao','birthday':datetime.now()}
# json_str = json.dumps(d)
# print(json_str)
class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):
        if isinstance(field,datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field,date):
            return field.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self,field)

json_str = json.dumps(d,cls=JsonCustomEncoder)
print(json_str)
