This repo is used to hold two functions I wrote for CH545 HW1, an MIT license, and this README file. 



extract_parameter_fxn.py holds the extract_parameter function, which takes 
(unit_name) , (parameter_name) , and (index) as arguments.

It searches in unit_operations_data for a given specified unit, a given
parameter associated with that unit, and a value for an index within that
parameter. Example units include "disillation column" and "reactor". Example
parameters include "temperature" and "pressure". Inidices in the example data
set are between 0 and 2.

The function returns the value associated with a given unit, parameter, and
index if possible, and returns error messages if one of the given arguments is
not in the data set.



calculate_solution_weights_fxn.py holds the calculate_solution_weights function 
which takes (molecular_weights) and (solutions_needed) as arguments.

(molecular_weights) is a dictionary with keys which are chemical compositions
such as 'NaCl' and values which should be the molecular weight of the
associated chemical composition. (solutions_needed) should be a list of
solutions needed with their desired concentrations in Molar, for example
['NaCl-0.5M']. Take care to replicate the formatting in the example.

The function calculates and returns the dry weight of each componenet needed to 
produce a 1 Liter solution at the desired molarity.
