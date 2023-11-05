def arithmetic_arranger(problems, *show_answer):
    #with *arg you can input an optional parameter in the function
    # Error Handling
    if len(problems) > 5:
        return "Error: Too many problems."
    
    arranged_problems = [] 

    # Parsing the string
    for index, value in enumerate(problems):
        problems_parsed = value.split(" ")  # ["32", "+", "8", ...]
        if problems_parsed[1] != "+" and problems_parsed[1] != "-":
        #if problems_parsed[1] not in "-+":
            return "Error: Operator must be '+' or '-'."
        
        if len(problems_parsed[0]) > 4 or len(problems_parsed[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        try:
            operand_1 = int(problems_parsed[0])
            operator = problems_parsed[1]
            operand_2 = int(problems_parsed[2])
        except ValueError:
            return "Error: Numbers must only contain digits."
        

        # String formatting
        # Calculate the length of each operator/line, and compute the necessary space in each line, at the end generate the necesary number of dashes (3 to 5);
        # Append the answer if show_answer exists

        # Calculate the longest value, operator +- is always one space apart from the longest value, always at second line;
        longest_str = max(len(str(operand_1)), len(str(operand_2)))
        problems_width = longest_str + 2  # longest operator + " " + the operation itself!


        #output = f"{problems_parsed[0]:>{problems_width}}\n{f'{problems_parsed[1]} {problems_parsed[2]}':>{problems_width}}\n{'-'*{problems_width}}"
        # the {aa:>{bb}} bb justifies the content of aa to the right!
        # if bb is a variable => second set of {}!!
        # the aa has to be in the same curly brackets as bb!!!

        # Trying to output in splitted lines
        line_1 = f"{problems_parsed[0]:>{problems_width}}"
        #line_2 = f"{f'{problems_parsed[1]} {problems_parsed[2]}':>{problems_width}}" # returns incorrectly because everything is pushed to the right, with one space separating the operation from the second element, while the operation should stay at the very left!
        line_2 = operator + f"{problems_parsed[2]:>{problems_width-1}}"
        dash = '-'*problems_width


        try:
            arranged_problems[0] += " "*4 + line_1
        except IndexError:
            arranged_problems.append(line_1)
        try:
            arranged_problems[1] += " "*4 + line_2
        except IndexError:
            arranged_problems.append(line_2)
        try:
            arranged_problems[2] += " "*4 + dash
        except IndexError:
            arranged_problems.append(dash)

        # Answer row
        if show_answer: # if the second parameter True is passed
            calc = (operand_1 + operand_2) if problems_parsed[1] == "+" else (operand_1 - operand_2)
            line_answer = f"{str(calc):>{problems_width}}"

            try:
                arranged_problems[3] += " "*4 + line_answer
            except IndexError:
                arranged_problems.append(line_answer)

    #arranged_problems.append(output)
    print(arranged_problems)

    final = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"


    if show_answer:
        final_2 = final + f"\n{arranged_problems[3]}"
        return final_2
    else:
        return final

arithmetic_arranger(['1 + 2', '1 - 9380'])
