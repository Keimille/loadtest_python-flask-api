from faker import Faker
import requests
import time
import random 


#test POST Method
def main():
  test = input('Enter type of test you would like to perform. Options: post, put, delete, get. ')
  test_type = test.lower()
  try:
      if test_type == "post":
          post_test()
      elif test_type == "get":
          get_test()
      elif test_type == "delete":
          delete_test()
      elif test_type == "put":
          put_test()
      else:
          print('Oops! Something went wrong!')
  except:
      print('Oops! Something went wrong!')


def post_test():
    fake = Faker()
    id = int(input("Enter id to start testing from: "))
    messages = int(input('Enter number of messages to generate: '))
    next_send = float(input('Enter interval (in seconds) to send each message: '))
    
    for i in range(messages):
        url = 'http://127.0.0.1:5000/author-quotes/' + str(id)
        params ={'author': fake.name(), 'quote': fake.text()}
        post_message = requests.post(url, data = params)
        print(url)
        print(post_message.text)
        id += 1
        time.sleep(next_send)

def put_test():
    fake = Faker()
    id = int(input("Enter id to start testing from: "))
    messages = int(input('Enter number of messages to generate: '))
    next_send = float(input('Enter interval (in seconds) to send each message: '))
    
    for i in range(messages):
        url = 'http://127.0.0.1:5000/author-quotes/' + str(id)
        params ={'author': fake.name(), 'quote': fake.text()}
        put_message = requests.put(url, data = params)
        print(url)
        print(put_message.text)
        id += 1
        time.sleep(next_send)

def get_test():
    messages = int(input('Enter number of messages to generate: '))
    next_send = float(input('Enter interval (in seconds) to send each message: '))

    for i in range(messages):
        url = 'http://127.0.0.1:5000/author-quotes/'
        get_message = requests.get(url)
        print(url)
        print(get_message.text)
        time.sleep(next_send)

def delete_test():
    messages = int(input('Enter number of messages to generate: '))
    print('Pick a range of ids to delete at random ')
    id_start = int(input('Enter starting range: '))
    id_end = int(input('Enter end range: '))
    next_send = float(input('Enter interval (in seconds) to send each message: '))
    
    for i in range(messages):
        url = 'http://127.0.0.1:5000/author-quotes/' + str(random.randint(id_start, id_end))
        delete_message = requests.delete(url)
        print(url)
        print(delete_message.text)
        time.sleep(next_send)

main()
