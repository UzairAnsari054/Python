alphabets = ["a","b","c","d"]
def linear_search_3(alphabets):
    for alphabet in range(len(alphabets)):
        print(alphabet)
    
def linear_search_4(alphabets):
    for alphabet in alphabets:
        print(alphabet)
        
linear_search_3(alphabets)
linear_search_4(alphabets)

# Findings:
# for alphabet in range(len(alphabets)):
#     This will return the indexes starting from 0 to lengtg of alphabets

# for alphabet in alphabets:
#     This will return the alphabets from start to end