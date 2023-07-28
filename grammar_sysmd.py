from lark import Lark, Transformer, v_args, Visitor, Tree

grammar = '''
    start: sysmd "EOF"

    sysmd: (element | triple | package)*

    element: "define" definition
           | "attribute" attribute
           | "assoc" association

    triple: identification triple_types

    definition: identification "isA" (qualified_name | relationship_definition)

    attribute: ("Value"? qualified_name ":")? multiplicity? qualified_name ("=" STRING)?

    association: identification "hasA" qualified_name_list

    triple_types: "isA" qualified_name
                | "hasA" qualified_name_list
                | "uses" qualified_name_list
                | "imports" qualified_name_list
                | "defines" definition_list

    relationship_definition: CNAME qualified_name "from" qualified_name multiplicity "to" qualified_name multiplicity

    package: "Package" CNAME "{" element* "}"

    identification: simple_name*
                  

    simple_name: CNAME

    qualified_name: CNAME ("::" CNAME)* | CNAME ":" CNAME

    multiplicity: "[" (SIGNED_INT | FLOAT) ("," (SIGNED_INT | FLOAT))? "]"

    integer_literal: SIGNED_INT

    real_literal: FLOAT

    element_list: element ("," element)*

    qualified_name_list: qualified_name ("," qualified_name)*

    definition_list: definition (";" definition)*

    STRING: /".*?"/

    %import common.CNAME
    %import common.SIGNED_INT
    %import common.FLOAT
    %import common.WS
    %ignore WS
'''


class SysMDTransformer(Transformer):
    pass
    # implement transformation methods here

lark_parser = Lark(grammar, start='start', parser='lalr', transformer=SysMDTransformer())

#tree = lark_parser.parse("your_string_here")



def syntax_match():
    pass


#g = lark_parser.parse ('CarBodyParts::RoofRack hasA\nValue capacity: String = \"new value\",\nValue material: String = \"Aluminum\",\nValue attachmentMethod: String = \"Clamp-on\",')

g1 = lark_parser.parse ("Vehicle isA Any\nPassengerCar isA Vehicle\nSportsCar isA PassengerCar\nLuxuryCar isA PassengerCar\nFamilyCar isA PassengerCar\nSmallCars isA PassengerCar\nSUV isA PassengerCar\nPetrolCar isA PassengerCar\nDieselCar isA PassengerCar\nBEV isA PassengerCar\nCNGCar isA PassengerCar\nHEV isA PassengerCar\nPHEV isA PassengerCar\nAlternateFuelCar isA PassengerCar\nPassengerCar imports Drivetrains, Frame, Chassis, LubricationSystems, Sensors\nPassengerCar hasA\nnoAutomation: NoAutomation,\ndriverAssistance: DriverAssistance,\npartialAutomation: PartialAutomation,\nconditionalAutomation: ConditionalAutomation,\nhighAutomation: HighAutomation,\nfullAutomation: FullAutomation EOF")



#print ("parser", g1)

class TreeVisitor(Visitor):
    def __init__(self):
        self.subtrees = []

    def __default__(self, tree):
        #subtree = Tree(data, children)
        self.subtrees.append(tree)

tree_visitor = TreeVisitor()
tree_visitor.visit(g1)

# Now tree_visitor.subtrees contains all the subtrees
for subtree in tree_visitor.subtrees:
    print("subtree: ", subtree, "\n")
