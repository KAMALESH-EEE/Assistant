from googlesearch import search  
import TextVoice

def get_data(query):
   

    my_results_list = []  
    for i in search(query,lang = 'en',num_results=10,advanced=True,):  
        my_results_list.append(i)  
    d = str(my_results_list[0])
    while '=' in d:
        d=d[d.index('=')+1::]
    print(d+'\nLINKS:\n')
    TextVoice.speech(d+'\nLINKS:\n')
    my_results_list=search(query,lang = 'en',num_results=10,)
    for i in my_results_list:
        print(i)


def find_url():
    import webbrowser
    url=input("Enter URL to open: ") 
    webbrowser.open_new_tab(url)