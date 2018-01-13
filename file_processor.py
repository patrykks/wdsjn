def process_file_by_line(input_filename, fn, output_filename):
    output_file = open(output_filename,"w")
    with open(input_filename) as input_file:
        for line in input_file:
            output_file.write(fn(line))
    output_file.close()

def process_file_by_word(input_filename, fn, output_filename):
    output_file = open(output_filename,"w")
    with open(input_filename) as input_file:
        for line in input_file:
            str_list = []
            for word in line.split():
                str_list.append(fn(word))
            str_list.append('\n')
            output_file.write(fn(' '.join(str_list)))
            del str_list
    output_file.close()
