import requests
import sys

def callReq():

    """ callReq collects all of the API requests
    Does not return a value, void method"""

    nameFunc = requests.get('http://vcm-3579.vm.duke.edu:5000/name')
    name = nameFunc.json()
    sys.stdout.write(str(name) + '\n')

    hello = requests.get('http://vcm-3579.vm.duke.edu:5000/hello/AlexSheu')
    hello = hello.json()
    sys.stdout.write(str(hello) + '\n')

    dist = requests.post('http://vcm-3579.vm.duke.edu:5000/distance', json={'a':[4,5], 'b':[3,4]} )
    dist = dist.json()
    sys.stdout.write(str(dist) + '\n')

if __name__ == "__main__":
	callReq()




