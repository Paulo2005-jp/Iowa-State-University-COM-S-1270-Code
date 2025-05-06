# Paulo
# April 2, 2025
# Lab 11



def analyzeBook(filename):
    count = {}
    
    with open(filename, encoding="utf-8", errors="ignore") as f:  
        for line in f:
            for word in line.split():
                
                word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
                word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
                word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
                word = word.replace(']', '').replace(';', '')

                word = word.lower()  

                if word.isalpha():  
                    if word in count:
                        count[word] += 1
                    else:
                        count[word] = 1
    return count
    

def outputAnalysis(count, filename):
    keys = list(count.keys())
    keys.sort()

    
    if filename.endswith(".txt"):
        base_name = filename[:-4]
    else:
        base_name = filename

    output_filename = base_name + "_analysis.txt"

    with open(output_filename, 'w') as out:
        for word in keys:
            out.write(word + " " + str(count[word]) + "\n")
    
    print(f" Results saved to {output_filename}")

def main():
    filename = "bookFile.txt"  
    print(f" Analyzing the file: {filename}")
    count = analyzeBook(filename)
    outputAnalysis(count, filename)


if __name__ == "__main__":
    main()
 