def create_file(outputlocation, write_mode, textfile, replace_func):
    with open(outputlocation, write_mode) as output:
      with open(textfile, 'r') as f:
          for line in f:
              line = line.strip()
              line = replace_func(line)
              output.write(line)
    print('Output to:', outputlocation)
