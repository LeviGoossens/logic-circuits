assembly_program = """
data:
v5 m80
v6 m81

program:
load rA m80
load rB m81

add rA rB rC

store rC m82

HALT
"""

translation = {
    "registers": {
        "rA" : "@00",
        "rB" : "@01",
        "rC" : "@10",
        "rD" : "@11",
        },
    "commands" : {
        "ALU": {
            "add": "0000 0000 aa bb cc __",
            },
        "registers & RAM": {
            "load": "0001 00 aa bbbb bbbb",
            "store": "0001 01 aa bbbb bbbb"
            },
        "jump": {
            "jump": "0010 0000 bbbb bbbb",
            "jump zero": "0010 0001 bbbb bbbb",
            "jump neg": "0010 0010 bbbb bbbb",
            },
        "high-level": {
            "HALT": "0011 0000 ____ ____"
            }
        }
    }
def address_to_bin(memory_address: str):
    a = bin(int(memory_address, 16))[2:].rjust(8, "0")
    return f"@{a[:4]} {a[4:8]} {a[8:12]} {a[12:16]}"

def value_to_bin(data_value: str):
    a = bin(int(data_value, 16))[2:].rjust(16, "0")
    return f"v{a[:4]} {a[4:8]} {a[8:12]} {a[12:16]}"

def my_translate(program: str):
    translated_program = ""
    for line in program.split("\n"):
        print(line)
        translated_line = None
        if line == "":
            translated_line = ""
        if "program:" in line or "data:" in line:
            translated_line = line

        if line.startswith("v"):
            args = line.split(" ")

            value = value_to_bin(args[0][1:])
            address = address_to_bin(args[1][1:])

            translated_line = f"{value} {address}"

        for key in translation["commands"]["ALU"]:
            if line.startswith(key):
                translated_line = translation["commands"]["ALU"][key]

        for key in translation["commands"]["registers & RAM"]:
            if line.startswith(key):
                translated_line = translation["commands"]["registers & RAM"][key]

        for key in translation["commands"]["jump"]:
            if line.startswith(key):
                translated_line = translation["commands"]["jump"][key]

        for key in translation["commands"]["high-level"]:
            if line.startswith(key):
                translated_line = translation["commands"]["high-level"][key]



        if translated_line != None:
            translated_program += translated_line + "\n"
        else:
            translated_program += line + "...\n"
    translated_program = translated_program.replace("_", "0")

    return translated_program


assembled_program = my_translate(assembly_program)

print("\n\n\nassembled program")
print(assembled_program)
