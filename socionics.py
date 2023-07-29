from socionics_relationships import RELATIONSHIP_NAMES, RELATIONSHIP_DESCRIPTIONS
from socionics_types import TYPE_ABBREVIATIONS, TYPE_NAMES

def get_relation_index(code1, code2):
    """Calculate the index of the relationship between two socionic types."""
    return abs(code1 - code2) % len(RELATIONSHIP_NAMES['en'])

def get_relation_name(code1, code2, lang='en'):
    """Calculate the name of the relationship between two socionic types."""
    relation_index = get_relation_index(code1, code2)
    return RELATIONSHIP_NAMES[lang][relation_index]

def get_relation_description(code1, code2, lang='en'):
    """Get the description of the relationship between two socionic types."""
    relation_index = get_relation_index(code1, code2)
    return RELATIONSHIP_DESCRIPTIONS[lang][relation_index]

def calculate_type_relationship(first_type, second_type, lang='en'):
    """Calculate and display the relationship between two socionic types."""
    code1, code2 = TYPE_ABBREVIATIONS[first_type.upper()], TYPE_ABBREVIATIONS[second_type.upper()]
    relation_name = get_relation_name(code1, code2, lang)
    relation_description = get_relation_description(code1, code2, lang)
    type_name1, type_name2 = TYPE_NAMES[code1][lang], TYPE_NAMES[code2][lang]
    print(f"\nIntertype relationship between {first_type.upper()} ({type_name1}) and "
          f"{second_type.upper()} ({type_name2}) - {relation_name} Relationship")
    print("Description:", relation_description)

if __name__ == "__main__":
    lang = input("Choose a language (en/es/uk): ").lower()
    if lang not in RELATIONSHIP_NAMES:
        print("Invalid language choice. Defaulting to English (en).")
        lang = 'en'

    print(f"Welcome to the Socionics Intertype Relationship Calculator! (Language: {lang})")
    while True:
        first_type = input("\nEnter the first type (e.g., 'SEI' or 'Mediator'): ").upper()
        if first_type in TYPE_ABBREVIATIONS:
            second_type = input("Enter the second type (e.g., 'SEI' or 'Mediator'): ").upper()
            if second_type in TYPE_ABBREVIATIONS:
                calculate_type_relationship(first_type, second_type, lang)
            else:
                print("Invalid type abbreviation. Please enter a valid type abbreviation.")
        else:
            print("Invalid type abbreviation. Please enter a valid type abbreviation.")
            continue

        exit_choice = input("Do you want to calculate another relationship? (yes/no): ").lower()
        if exit_choice == 'no':
            print("Exiting...")
            break
