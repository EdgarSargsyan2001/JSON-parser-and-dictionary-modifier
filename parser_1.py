def add_tab(s):
    str = ""
    while s != 0:
        str += "   "
        s -= 1
    return str


def object_to_string(obj={}, tab_level=1):
    ans_string = "{\n" + add_tab(tab_level)

    keys = obj.keys()
    for key in keys:
        ans_string += '"' + key + '"'
        ans_string += ": "
        if type(obj[key]) is dict:
            ans_string += object_to_string(obj[key], tab_level + 1)
            if len(keys) != 1 and list(keys)[-1] != key:
                ans_string += ",\n" + add_tab(tab_level)

        elif type(obj[key]) is str:
            ans_string += '"' + obj[key] + '"'
            if len(keys) != 1 and list(keys)[-1] != key:
                ans_string += ",\n" + add_tab(tab_level)

        elif type(obj[key]) is int:
            ans_string += str(obj[key])
            if len(keys) != 1 and list(keys)[-1] != key:
                ans_string += ",\n" + add_tab(tab_level)
        else:
            print("error")

    ans_string += "\n" + add_tab(tab_level - 1) + "}"
    return ans_string


class JSONParser:
    def __init__(self, file_info):
        self.json_string = self.file_info_make_line(file_info)
        self.pos = 0

    def parse(self):
        if self.json_string[self.pos] != "{":
            print("Invalid JSON")
            return None
        try:
            return self.parse_value()
        except SyntaxError:
            print("Invalid JSON")
            return None

    def parse_value(self):
        if self.json_string[self.pos] == "{":
            return self.parse_object()
        elif self.json_string[self.pos] == '"' or self.json_string[self.pos] == "'":
            return self.parse_string()
        else:
            return self.parse_number()

    def parse_object(self):
        self.pos += 1
        result = {}

        if self.json_string[self.pos] == "}":
            self.pos += 1
            return result

        while True:
            key = self.parse_string()

            if self.json_string[self.pos] != ":":
                raise SyntaxError("Invalid JSON")
            self.pos += 1

            value = self.parse_value()
            result[key] = value

            if self.json_string[self.pos] == ",":
                self.pos += 1
            elif self.json_string[self.pos] == "}":
                self.pos += 1
                break
            else:
                raise SyntaxError("Invalid JSON")

        return result

    def parse_string(self):
        self.pos += 1
        start_pos = self.pos

        while self.pos < len(self.json_string):
            if self.json_string[self.pos] == '"' or self.json_string[self.pos] == "'":
                self.pos += 1
                return self.json_string[start_pos : self.pos - 1]
            else:
                self.pos += 1

        raise SyntaxError("Invalid JSON string")

    def parse_number(self):
        start_pos = self.pos

        while self.pos < len(self.json_string) and self.json_string[self.pos].isdigit():
            self.pos += 1

        number_string = self.json_string[start_pos : self.pos]
        return int(number_string)

    def file_info_make_line(self, file_info):
        str = ""
        for line in file_info:
            str += line.replace("\n", "")
            str = str.replace(" ", "")
        return str
