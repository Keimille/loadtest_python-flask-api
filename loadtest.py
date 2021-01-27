from faker import Faker
import requests


#test POST Method
def main():
  post_test()  

def post_test():
    fake = Faker()
    id = int(input("Enter id to start testing from"))
    messages = int(input('Enter number of messages to generate'))
    
    for i in range(messages):
        url = 'http://127.0.0.1:5000/author-quotes/{id}'
        params ={'author': fake.name(), 'quote': fake.text()}
        post_message = requests.post(url, data = params)
        print(post_message.text)
        id += 1
main()
