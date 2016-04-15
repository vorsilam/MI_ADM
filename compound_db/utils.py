
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def load_filter_choices(file, prepend=('All', 'All')):
    ret = list()
    if prepend:
        ret.append(prepend)
    with open(file, 'r', encoding='utf-8') as infile:
        for line in infile:
            line = line.strip().strip("\"")
            if line:
                ret.append((line, line))
    return tuple(ret)

def parse_filters(form, filter_key):
    filter_options = set(form.cleaned_data[filter_key]) | set(form.cleaned_data[filter_key + '_custom'].split(','))
    filter_options.remove('')
    return filter_options