def arithmetic_arranger(problems, ans=False):
    frst = ""
    scnd = ""
    thrd = ""
    last = ""

    for problem in problems:
        if len(problems) > 5:
            return "Error: Too many problems."
        if '/' in problem or '*' in problem:
            return "Error: Operator must be '+' or '-'."
        a = problem.split()
        if not (a[0].isnumeric() and a[2].isnumeric()):
            return "Error: Numbers must only contain digits."
        if (len(a[0])>4 or len(a[2])>4):
            return 'Error: Numbers cannot be more than four digits.'
        
        sum = str()
        if a[1]=="+":
            sum = str(int(a[0]) + int(a[2]))
        elif a[1] == "-":
            sum = str(int(a[0]) - int(a[2]))
        
        length = max(len(a[0]), len(a[2])) + 2
        frst_line = str(a[0]).rjust(length)
        scnd_line = a[1] + a[2].rjust(length-1)
        lines = ""
        slvd_line = str(sum).rjust(length)
        for _ in range(length):
            lines += "-"
                
        if problem != problems[-1]:
            frst += frst_line + '    '
            scnd += scnd_line + '    '
            thrd += lines + '    '
            last += slvd_line + '    '
        else:
            frst += frst_line
            scnd += scnd_line
            thrd += lines
            last += slvd_line

    if ans:
        string = frst + "\n" + scnd + "\n" + thrd + "\n" + last
    else:
        string = frst + "\n" + scnd + "\n" + thrd
    return string