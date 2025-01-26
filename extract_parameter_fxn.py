# The function takes inputs unit_name, parameter_name, and index
def extract_parameter(unit_name, parameter_name, index):

  # First the function searches in unit_operations_data for the supplied unit_name 
  # If the value is present the associated dictionary is stored as unit_data
    try:
        unit_data = unit_operations_data[unit_name]
  # If the unit name is not found an error message returns
    except:
        return "Invalid input, unit_name not found"
    
  # Next the function searches in unit_data for a key matching parameter_name
  # If the parameter_name is present, the associated list is stored as parameter_list
    try:
        parameter_list = unit_data[parameter_name]
  # If the parameter name is not found an error message returns
    except:
        return "Invalid input, parameter_name not found"

  # Next the function searches in parameter_list for the index item matching the input index
  # If the index is in range, the associated value is stored as parameter_value
  # Finally the function returns the unit name, parameter name, and parameter value neatly in an f-string
    try:
        parameter_value = parameter_list[index]
        return f"{unit_name}_{parameter_name}_{parameter_value}"
  # If the index provided is not in the range of parameter_list, an error message returns 
    except:
        return "Invalid input, index out of range"
