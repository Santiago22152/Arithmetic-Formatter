

def arithmetic_arranger(problems, results=False):
    #Error handling / Border cases
    if len(problems) > 5:
       
        return "Error: Too many problems."

    problems_array=[];
    for values in problems:
         operations = values.split(" ");
         if operations[1] not in "+-":
          
             return "Error: Operator must be '+' or '-'.";
         else:
             if operations[0].isdigit() and operations[2].isdigit():
                 #Append splited operations if there is no errors
                 if len(operations[0]) < 5 and len(operations[2]) < 5:
                     problems_array.append(operations);
                 else:
                   
                     return "Error: Numbers cannot be more than four digits.";
             else:
                  
             
                  return "Error: Numbers must only contain digits.";
    

    #Space between problems.
    spaces_between= " "*4;
    dash="-";
    #Storage the results.
    arranged_problems=["","","",""];
    #Main for loop
    for operations in problems_array:
        #Calc the necessary width for operations.
        max_width = max(len(operations[0]),len(operations[2]))+2;
        if (operations != problems_array[-1]):
            #Each index is a new line
            arranged_problems[0] += f"{operations[0]:>{max_width}}" + spaces_between;
            arranged_problems[1] += f"{operations[1]}{operations[2]:>{max_width-1}}" + spaces_between;
            arranged_problems[2] += f"{dash*max_width}" + spaces_between;
            #Control if need to show the results or not
            if(results==True):
                if (operations[1] == "+"):
                    arranged_problems[3] += f"{(int(operations[0]) + int(operations[2])):>{max_width}}" + spaces_between;
                else:
                    arranged_problems[3] += f"{(int(operations[0]) - int(operations[2])):>{max_width}}" + spaces_between;
        else:
            arranged_problems[0] += f"{operations[0]:>{max_width}}";
            arranged_problems[1] += f"{operations[1]}{operations[2]:>{max_width-1}}";
            arranged_problems[2] += f"{dash*max_width}";
            if(results==True):
                if (operations[1] == "+"):
                 arranged_problems[3] += f"{(int(operations[0]) + int(operations[2])):>{max_width}}"
                else:
                    arranged_problems[3] += f"{(int(operations[0]) - int(operations[2])):>{max_width}}"
    if(results==True):
        formatted_problems=f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}\n{arranged_problems[3]}";
    else:
        formatted_problems=f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}";
    

    return formatted_problems;

print(arithmetic_arranger(["18 + 25", "33 - 2", "12 + 44"],True));