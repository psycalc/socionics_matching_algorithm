socionic_types = [
    'INTj', 'INTp', 'ENTj', 'ENTp',
    'INFj', 'INFp', 'ENFj', 'ENFp',
    'ISTj', 'ISTp', 'ESTj', 'ESTp',
    'ISFj', 'ISFp', 'ESFj', 'ESFp'
]

intertype_relations = [
    ('Duality', 5), ('Activity', 4), ('Mirror', 3), ('Identical', 2),
    ('Kindred', 1), ('Semi-Duality', 0), ('Look-a-like', -1), ('Super-Ego', -2),
    ('Quasi-Identical', -3), ('Contrary', -4), ('Benefit', -5), ('Supervision', -6),
    ('Extinguishment', -7), ('Conflict', -8)
]

class SocionicsType:
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return self.code

    def relation_to(self, other):
        relation = None
        if self.code == other.code:
            relation = 'Identical'
        elif self.is_rational() == other.is_rational() and self.is_introverted() != other.is_introverted():
            if self.is_ethical() == other.is_ethical():
                relation = 'Duality'
            else:
                relation = 'Quasi-Identical'
        elif self.is_rational() != other.is_rational() and self.is_introverted() == other.is_introverted():
            if self.is_ethical() == other.is_ethical():
                relation = 'Activity'
            else:
                relation = 'Mirror'
        elif self.is_rational() == other.is_rational() and self.is_introverted() == other.is_introverted():
            if self.is_ethical() != other.is_ethical():
                relation = 'Kindred'
            else:
                relation = None
        elif self.is_rational() != other.is_rational() and self.is_introverted() != other.is_introverted():
            if self.is_ethical() == other.is_ethical():
                relation = None
            else:
                if self.code[0] == other.code[0]:
                    relation = None
                elif (self.code[0] == "I" and other.code[0] == "E") or (self.code[0] == "E" and other.code[0] == "I"):
                    if (self.code[2] == "T" and other.code[2] == "F") or (self.code[2] == "F" and other.code[2] == "T"):
                        if (self.code[3] == "j" and other.code[3] == "p") or (self.code[3] == "p" and other.code[3] == "j"):
                            relation = "Super-Ego"
                        else:
                            relation = "Benefit"
                    else:
                        if (self.code[3] == "j" and other.code[3] == "p") or (self.code[3] == "p" and other.code[3] == "j"):
                            relation = "Supervision"
                        else:
                            relation = "Extinguishment"
                else:
                    if (self.code[2] == "T" and other.code[2] == "F") or (self.code[2] == "F" and other.code[2] == "T"):
                        if (self.code[3] == "j" and other.code[3] == "p") or (self.code[3] == "p" and other.code[3] == "j"):
                            relation = "Contrary"
                        else:
                            relation = None
                    else:
                        if (self.code[3] == "j" and other.code[3] == "p") or (self.code[3] == "p" and other.code[3] == "j"):
                            relation = None
                        else:
                            relation = None
        else:
            relation = None

        comfort_level = None
        for rel, level in intertype_relations:
            if rel == relation:
                comfort_level = level
                break

        return relation, comfort_level

    # is rational or irrational
    def is_rational(self):
        if self.code[-1].lower() in ['J','j']:
            return True
        else:
            return False

    # is introverted or extroverted
    def is_introverted(self):
        if self.code[:1]=='I':
            return True
        else:
            return False

    # is ethical or logical
    def is_ethical(self):
        if self.code[-2]=='F':
            return True
        else:
            return False
