"""Module for working with socionic types."""

socionic_types = [
    'INTj', 'INTp', 'ENTj', 'ENTp',
    'INFj', 'INFp', 'ENFj', 'ENFp',
    'ISTj', 'ISTp', 'ESTj', 'ESTp',
    'ISFj', 'ISFp', 'ESFj', 'ESFp'
]

class SocionicsType:
    """Class representing a socionic type."""
    
    def __init__(self, code):
        """Initialize a new socionic type with the given code."""
        self.code = code

    def __str__(self):
        """Return the code of the socionic type as a string."""
        return self.code

    @property
    def is_rational(self):
        """Return True if this socionic type is rational, False otherwise."""
        return self.code.endswith(('j', 'p'))

    @property
    def is_introverted(self):
        """Return True if this socionic type is introverted, False otherwise."""
        return self.code.startswith('I')

    @property
    def is_ethical(self):
        """Return True if this socionic type is ethical, False otherwise."""
        return self.code.endswith('F')

    def get_relation(self, other):
        """Return the relationship between this socionic type and another."""
        relations = {
            # Identity
            ('Identical', 'Complete comfort'): lambda self, other: self.code == other.code,
            
            # Duality
            ('Duality', 'Complete comfort'): lambda self, other: (
                self.is_rational != other.is_rational and
                self.is_introverted != other.is_introverted and
                self.is_ethical != other.is_ethical
            ),
            
            # Activity
            ('Activity', 'Comfortable'): lambda self, other: (
                self.is_rational != other.is_rational and
                self.is_introverted == other.is_introverted and
                self.is_ethical != other.is_ethical
            ),
            
            # Mirror
            ('Mirror', 'Comfortable'): lambda self, other: (
                self.is_rational == other.is_rational and
                self.is_introverted != other.is_introverted and
                self.is_ethical != other.is_ethical
            ),
            
            # Kindred
            ('Kindred', 'Slightly comfortable'): lambda self, other: (
                self.is_rational != other.is_rational and
                self.is_introverted != other.is_introverted and
                self.is_ethical != other.is_ethical
            ),
            
            # Quasi-Identical
            ('Quasi-Identical', 'Slightly comfortable'): lambda self, other: (
                self.is_rational == other.is_rational and
                self.is_introverted != other.is_introverted and
                self.is_ethical == other.is_ethical
            ),
            
            # Super-Ego
            ('Super-Ego', 'Uncomfortable'): lambda self, other: (
                self.is_rational != other.is_rational and
                self.is_introverted == other.is_introverted and
                self.is_ethical != other.is_ethical
            ),
            
            # Benefit
            ('Benefit', 'Uncomfortable'): lambda self, other: (
                self.is_rational != other.is_rational and
                self.is_introverted == other.is_introverted and
                self.is_ethical == other.is_ethical
            ),
            
            # Supervision
            ('Supervision', 'Very uncomfortable'): lambda self, other: (
                self.is_rational == other.is_rational and
                self.is_introverted == other.is_introverted and
                self.is_ethical != other.is_ethical
            ),
            
            # Extinguishment
            ('Extinguishment', 'Very uncomfortable'): lambda self, other: (
                self.is_rational == other.is_rational and
                self.is_introverted == other.is_introverted and
                self.is_ethical == other.is_ethical
            ),
            
            # Contrary
            ('Contrary', 'Complete discomfort'): lambda self, other: (
                self.is_rational != other.is_rational and
                self.is_introverted != other.is_introverted and
                self.is_ethical != other.is_ethical
            )
        }

        for rel, level in relations.items():
            if level(self, other):
                return rel

        return None, None