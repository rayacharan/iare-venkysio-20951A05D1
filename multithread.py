#multi-threading in python
import threading

def rev_word(word, results):
        
    results.append(word[::-1])
    #print(results)

def reverse_para(para):
    words = para.split()
    results = []
    threads = []
    for word in words:
        t = threading.Thread(target=rev_word, args=(word, results))   
        t.start()
        threads.append(t)    
    for t in threads:
        t.join()        
        
    reversed_para = ' '.join(results)
    return reversed_para

paragraph = input("Enter a para: ")
reversed_paragraph = reverse_para(paragraph)
print(reversed_paragraph)
