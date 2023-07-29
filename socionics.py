# Intertype relations between types (0 - Identity, 1 - Duality, etc.)
relation_names = [
    'Identity', 'Duality', 'Activation', 'Mirror', 'Benefactor', 'Supervisee',
    'Business', 'Mediator', 'Quasi-identity', 'Extinguishment', 'Conflict',
    'Beneficiary', 'Supervisor', 'Kindred', 'Semi-duality', 'Activation']

# Descriptions of Intertype relationships
type_description = [
    'These partners are very similar in their abilities and the way they look at the world as many of the same traits are shared. This relationship is the easiest to form and will succeed when there is a need to transfer accumulated knowledge and experience back and forth. Both will have complete understanding but due to similarities will be largely unable to help the other with identical problems.',
    'Interaction is generally rewarding and satisfying for both, providing each other with inspiration and support. This is often considered the most beneficial relation as all interactions are complementary, providing an “other half” effect.',
    'Partners raise the overall energy level, serve to mobilize one another. However, these partners tend to overactivate each other over time and can do with breaks in order to cool down.',
    'Partners will feel as though they are looking in the mirror, seeing a reflection of their motives; will have similar actions and motivations, and can reach mutual understanding quite easily. However, levels of energy and discipline will be reversed, resulting in different lifestyles. They are likely to have slightly different takes on the same issue and may mutually correct each other. While mostly affable, sometimes, this can result in minor clashes.',
    'Both partners greatly admire each other. However, there is an asymmetry: the benefactor is able to help the beneficiary but not the other way around. As a result, these relations are often temporary, with a sense of unfairness being felt over time by the benefactor and a sense of uselessness being felt by the beneficiary.',
    'This is an asymmetric relationship, in which one partner is constantly seen as lacking in some required area by the other. As a result, the supervisee feels somewhat wary or careful about their words and actions around the supervisor, feeling that they could be corrected in an area they feel insecure about.',
    'Both partners understand each other very well and are usually happy to interact. But, in general, this is a pair of people with very different goals.',
    'These relationships are usually pleasant, but only for mutual leisure time. It is difficult to accomplish something serious together because their individual goals continually undo each other.',
    'These are relationships built on mutual respect. Each partner sees qualities in the other that are desired. But they must maintain some psychological distance, because one-on-one, they can start to annoy one another. Although having very similar energy levels and lifestyles, they have very different abilities and life values, leading to misunderstanding.',
    'These partners have many common interests, but are often confused by each other`s seemingly counter-intuitive insights. Their thinking styles are very different despite being good at similar things. Each may often feel that they other is deliberately trying to undermine or extinguish their approach, but this is not intentionally the case.',
    'Partners` interests are aligned, but at a closer distance misunderstandings arise. Collaborative work with ample room to move, regarding process and approach, is necessary for success in this pair. Working in close contact will lead to confusion due to the very different values and attitudes these partners have. They will not take each other`s advice as they each perceive themselves as doing the same as the other, only better.',
    'Misunderstandings arise very easily in this type of relationship. The two partners are exact opposites in abilities, temperament and life values, resulting in there being very little in common. Despite being initially attracted to each other due to them providing in certain amounts what the other partner needs in their life, they soon realise that the value dissonance makes relations mutually painful, with each putting pressure upon the other`s points of insecurity rather than protecting and helping those points.',
    'Both partners greatly admire each other. However, there is an asymmetry: the benefactor is able to help the beneficiary but not the other way around. As a result, these relations are often temporary, with a sense of unfairness being felt over time by the benefactor and a sense of uselessness being felt by the beneficiary. ',
    'This is an asymmetric relationship, in which one partner is constantly seen as lacking in some required area by the other. As a result, the supervisee feels somewhat wary or careful about their words and actions around the supervisor, feeling that they could be corrected in an area they feel insecure about.',
    'Partners like to discuss similar topics and often have many common interests. But when they come to practical implementation of their mutual goals and projects, each finds that the other acts in contrary ways.',
    'Relationships of semi-duality can become very close for moderate periods of time. Often these relations lead to friendship and fruitful cooperation at work. But very close relationships can lead to disappointments.']

# Dictionary mapping type abbreviations to their index in the type_name and type_abbr lists
type_abbr = {
    'ILE': 0, 'SEI': 1, 'ESE': 2, 'LII': 3, 'EIE': 4, 'LSI': 5, 'SLE': 6, 'IEI': 7,
    'SEE': 8, 'ILI': 9, 'LIE': 10, 'ESI': 11, 'LSE': 12, 'EII': 13, 'IEE': 14, 'SLI': 15
}

# Dictionary mapping type index to their name
type_name = {
    0: 'Innovator', 1: 'Mediator', 2: 'Enthusiast', 3: 'Analyst', 4: 'Mentor', 5: 'Inspector',
    6: 'Marshal', 7: 'Romantic', 8: 'Leader', 9: 'Critic', 10: 'Entrepreneur', 11: 'Moralist',
    12: 'Pragmatist', 13: 'Humanist', 14: 'Networker', 15: 'Ergonomist'
}

# Function to calculate and display the relationship between two types
def calculate_relationship(type1, type2):
    code1, code2 = type_abbr[type1.upper()], type_abbr[type2.upper()]
    relation_index = abs(code1 - code2) % 16
    relation_name = relation_names[relation_index]
    print(f"\nIntertype relationship between {type1.upper()} ({type_name[code1]}) and "
          f"{type2.upper()} ({type_name[code2]}) - {relation_name} Relationship")
    print("Description:", type_description[relation_index])

# Main function
def main():
    print("Welcome to the Socionics Intertype Relationship Calculator!")

    while True:
        type1 = input("\nEnter the first type (e.g., 'SEI' or 'Mediator'): ").upper()
        if type1 in type_abbr:
            type2 = input("Enter the second type (e.g., 'SEI' or 'Mediator'): ").upper()
            if type2 in type_abbr:
                calculate_relationship(type1, type2)
            else:
                print("Invalid type abbreviation. Please enter a valid type abbreviation.")
        else:
            print("Invalid type abbreviation. Please enter a valid type abbreviation.")
            continue

        exit_choice = input("Do you want to calculate another relationship? (yes/no): ").lower()
        if exit_choice == 'no':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
