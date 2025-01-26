# The function takes molecular weights and the requested soltions as arguments
def calculate_solution_weights(molecular_weights, solutions_needed):

  # This declares an empty list which will be populated with formatted output entries as each weight is calculated
    output_list = []

  # The function iterates through each item in soltions_needed
    for i in solutions_needed:
   
    # For each list item it first stores the solution name as solution_name and desired concentration by splitting the solution name from its desired concentration
      solution_name = i.split('-')[0]
    # I include an additional step stripping the Molar unit from the concentration because it will be used in multiplication later
      concentration = i.split('-')[1].strip('M')

    # Next it tries to find the molecular weight for each solution name in molecular_weights
      # if it finds the value it simply stores the value as molecular_weight
    # Second it tries to find the molecular weight for each solution name in molecular_weights
      # if it finds the value it simply stores the value as molecular_weight
      try: 
        molecular_weight = molecular_weights[solution_name]
      # otherwise it sets molecular_weight to 'unknown'
      except:
        molecular_weight = 'unknown'

    # Third it tries to multiply the molecular weight by the desired molarity to identify the weight of solution required for 1 L of solution
    # Because this section already has output conditioned on whether the molecular weight was known, the output is also appended to a list within these try/except statements.
      # if the molecular weight value was known it stores the product as weight 
      try:
        weight = molecular_weight * float(concentration)
        # if the weight was known then the output can be formatted in an f-string and appended to the output list here
        output_list.append(f'{i}-{weight}g')
      # if the molecular weight was unknown it appends 'unknown' to the output list
      except:
        output_list.append('unknown')
    
  # Finally the function returns the output list
    return output_list
