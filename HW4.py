import ntpath
def path_leaf(path):
    #A function that extacts file name on all platforms for all path
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

import urllib3
import certifi
import os

def get_data(url):
    #A function that downloads the data if it is not present locally
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    r = http.request('GET', url, retries=False, preload_content=False)
    print(r.status)
    if r.status != 200:
        #check if the request is OK, AKA. whether the url is valid
        status = r.status
        print('Please provide valid url')
        return(status)
        raise Exception
    else:
        filename = path_leaf(url)#extracts name from the url
        if os.path.exists(filename):
            #check if the file already exists in the local directory, pass if it does
            print('Please check for it in your working directory: ' + os.getcwd())
            pass
        else:
            #download the file if not exists
            with open(filename, 'wb') as f:
                #write the data content of the url to a local file if the url is valid
                f.write(r.data)
            print('Downloaded')

def remove_data(url):
    #A function that remove the data if it is present locally
    filename = path_leaf(url)#extracts name from the url
    if os.path.exists(filename):
        #check if the file already exists in the local directory, remove it if it does exists
        os.remove(filename)
        print(filename + ' exists.' + ' It has been removed from your working directory: ' + os.getcwd())
    else:
              pass
