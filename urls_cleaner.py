# Import necessary modules
import re
import time

# Begining of time calculation for task performing
start = time.perf_counter()

def check_urls(input_file):

    count_total = 0
    count_duplicate = 0
    count_incorrect_urls = 0
    count_correct_urls = 0

    with open(input_file, 'r') as rf: # Open the file with list of URLs in read mode
        with open('final.txt', 'w') as wf: # Open/create the output file in write mode
            repeated_urls = set() # Choose the set to check for repeated URLs because set has add() method
            for url in rf: # Iterate through each line in the file
                count_total += 1
                if url not in repeated_urls: # Check if the URL not repeats
                    repeated_urls.add(url) # Add URL into the set
                    # Describe the pattern for our URLs: https://www.xxxxx.xxx/xxxxxxx/xxxxxxxx
                    pattern = "(https://www[.])[a-zA-Z0-9-]+[.][a-zA-Z]+[/][a-zA-Z0-9-]*[/]([-a-zA-Z0-9@:%_+.~#?&//=]*)"
                    if re.search(pattern, url): # Check if URL match with our pattern
                        wf.write(url) # Write correct URL into the output file
                        count_correct_urls += 1
                    else:
                        count_incorrect_urls += 1
                        continue
                else:
                    count_duplicate += 1
                    continue
    
    # Summary of calculations
    print(f'Total URLs in the file found: {count_total}')
    print(f'Total not duplicated URLs that meet pattern in the file found: {count_correct_urls}')
    print(f'Total not duplicated URLs that do not meet pattern in the file found: {count_incorrect_urls}')
    print(f'Total duplicate URLs in the file found: {count_duplicate}')

# Call the function with file name as argument
check_urls('tt_urls.txt')

# End of time calculation for task performing
finish = time.perf_counter()

# Time to perform the task
print(f'Finished in {round(finish-start, 2)} second(s)')
