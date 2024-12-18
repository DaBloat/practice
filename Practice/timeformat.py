def format_duration(sec):
    lookup = {'y':365, 'd':24, 'h':60, 'm':60, 's':1}
    word = ['year', 'day', 'hour', 'minute', 'second']
    out = []
    if sec == 0:
        return 'now'
    else:
        date = {}
        struct = list(lookup.keys())
        for i in reversed(range(len(struct))):
            if i - 4 == 0:
                date[struct[i]] = sec
            else:
                date[struct[i]] = int(date[struct[i+1]] / lookup[struct[i]])
                date[struct[i+1]] -= lookup[struct[i]] * date[struct[i]]
    
    dates = list(date.values())[::-1]
    for times in range(len(dates)):
        try:
            format = word[times]
            if dates[times] > 1:
                format = word[times]+'s'
            if dates[times] == 0:
                continue
        
            put = f"{dates[times]} {format}"
            out.append(put)
        except:
            pass
    
    output = []
    for i in range(len(out)):
        output.append(out[i])
        if i+1 == len(out) - 1:
            output.append(' and ')
        elif out[i] != out[-1]:
            output.append(', ')
        

    return ''.join(output)


print(format_duration(132030240))

