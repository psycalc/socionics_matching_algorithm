from socionics_translation import translations
def generate_model_a_description(type_abbreviation, lang='en'):
    # Define the functions and their versions
    functions = ['S', 'I', 'L', 'E']
    versions = ['e', 'i']
    
    # Define the blocks
    blocks = {'Ego': [None, None], 'Super-Ego': [None, None], 'Id': [None, None], 'Super-Id': [None, None]}
    
    # Extract the first and second functions from the type abbreviation
    first_function = type_abbreviation[0]
    second_function = type_abbreviation[1]
    
    # Determine the version of the first function based on the last letter of the type abbreviation
    first_function_version = versions[0] if type_abbreviation[-1] == 'E' else versions[1]
    
    # The second function has the opposite version of the first function
    second_function_version = versions[1] if first_function_version == versions[0] else versions[0]
    
    # Build the Ego block
    blocks['Ego'][0] = first_function + first_function_version
    blocks['Ego'][1] = second_function + second_function_version
    
    # Build the Super-Id block by swapping the versions of the first and second functions
    blocks['Super-Id'][0] = first_function + second_function_version
    blocks['Super-Id'][1] = second_function + first_function_version
    
    # Build the Super-Ego block by crossing the functions and keeping their versions
    blocks['Super-Ego'][0] = functions[(functions.index(second_function) + 2) % 4] + second_function_version
    blocks['Super-Ego'][1] = functions[(functions.index(first_function) + 2) % 4] + first_function_version
    
    # Build the Id block by copying the Ego block and swapping the versions of the functions
    blocks['Id'][0] = first_function + second_function_version
    blocks['Id'][1] = second_function + first_function_version
    
    # Define translations for each language

    
    # Generate a description of Model A based on the given type abbreviation and language
    description = f"Model A for type {type_abbreviation} consists of the following blocks:\n"
    
    for block_name, block_functions in blocks.items():
        translated_block_name = translations[lang][block_name]
        translated_block_functions = [translations[lang][function] for function in block_functions]
        
        description += f"- {translated_block_name}: {translated_block_functions[0]} (1), {translated_block_functions[1]} (2)\n"
    
    return description