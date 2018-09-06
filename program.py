#! python3
import service

__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

def main():
    service.download_info()

    for show_id in range(80, 145):
        info = service.get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))

def show_header():
    print("Welcome to the talk python downloader")
    print()

if __name__ == '__main__':
    main()