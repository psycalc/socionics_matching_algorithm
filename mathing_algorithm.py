from socionics import SocionicsType

type1 = SocionicsType('INTj')
type2 = SocionicsType('ESFp')

relation = type1.relation_to(type2)

print(f"The intertype relation between {type1} and {type2} is {relation}.")
