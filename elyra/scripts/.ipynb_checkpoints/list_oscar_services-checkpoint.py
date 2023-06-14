import json
from oscar_python.client import Client

def read_credentials(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def create_oscar_client(credentials):
    return Client(
        id=credentials['id'],
        endpoint=credentials['endpoint'],
        user=credentials['user'],
        password=credentials['password'],
        ssl=credentials['ssl']
    )


def write_services_to_file(services, file_path):
    with open(file_path, 'w') as file:
        for service in services:
            file.write(service + '\n')


def main():
    credentials = read_credentials('credentials.json')
    oscar_client = create_oscar_client(credentials)
    services = oscar_client.list_services()

    if services:
        write_services_to_file(services, 'services_list.txt')
        print("Services list saved to 'services_list.txt'.")
    else:
        print("No services found.")


if __name__ == '__main__':
    main()
