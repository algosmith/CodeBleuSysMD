from lark import Lark, Transformer, v_args

car_parts_grammar = """
    start: statement*

    statement: entity "hasA" attribute*

    entity: "CarBodyParts::" car_part_name

    car_part_name: IDENTIFIER

    attribute: "Value" attribute_name ":" attribute_type "=" attribute_value ","

    attribute_name: IDENTIFIER

    attribute_type: "String" | "Boolean" | "Real(" range ")" "[" UNIT "]"

    range: NUMBER ".." NUMBER

    attribute_value: STRING | BOOLEAN | NUMBER

    IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
    UNIT: /[a-zA-Z_][a-zA-Z0-9_]*/
    STRING: /"[^"\\\\]*"|\\\\.*/ 
    NUMBER: /\d+/ 
    BOOLEAN: "true" | "false" 

    %import common.WS 
    %ignore WS

"""

class CarPartsTransformer(Transformer):
    pass
    # implement transformation methods here

car_parts_parser = Lark(car_parts_grammar, parser='lalr', transformer=CarPartsTransformer())

print (car_parts_parser)

g = car_parts_parser.parse ('CarBodyParts::RoofRack hasA\nValue capacity: String = \"new value\",\nValue material: String = \"Aluminum\",\nValue attachmentMethod: String = \"Clamp-on\",')

print ("parser", g)