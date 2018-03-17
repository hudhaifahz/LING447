import os

def load_file(path, ignore_header=True, delimiter=','):
    """
    This function opens a file, strips white space off each line,
    then splits the lines by the delimiter argument.
    It returns a list of lists representing lines from the file.

    If ignore_header is True, then the first line of the file is not returned.
    """
    with open(path, mode='r', encoding='utf-8-sig') as file:
        if ignore_header:
            file.readline()

        lines = list()
        for line in file:
            line = line.strip()
            line = line.split(delimiter)
            lines.append(line)
        file.close()
    return lines

def load_local_file(filename, ignore_header=True, delimiter=','):
    path = os.path.join(os.getcwd(), filename)
    return load_file(path, ignore_header, delimiter)

def load_hayes():
    hayes = load_local_file('ipa2hayes.txt',ignore_header=False,delimiter='\t')
    features = dict()
    feature_names = hayes[0][1:]
    #hayes[0] is the header, the header from 1 onward is all the feature names
    for line in hayes[1:]:
        #we take a slice from the first element onward because we don't want
        #to read from the header line
        if not line[0]:
            #some lines contain empty strings, which evaluate to False
            #not False is True, so if the line is empty, then continue
            continue
        segment = line[0]
        features[segment] = list()
        values = line[1:]
        for value,name in zip(values, feature_names):
            features[segment].append(value+name)

    return features

if __name__ == '__main__':
    #if you run filefunctions, then the code inside this block will run
    #if you import filefunctions, then the code in this block will be skipped
    print('Hello World!')
