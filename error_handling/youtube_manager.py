'''
def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
'''

import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test =  json.load(file)
            #print(type(test))#list (json list)
            return test
    except FileNotFoundError:
        print("Error: File not found. Returning an empty list.")
        return []
    except json.JSONDecodeError:
        print("Error: File content is invalid or empty. Returning an empty list.")
        return []


def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    
    # for vid in videos:
    #     print(f"{vid}. ")
    
    print("\n")
    print("*"*70)
    
    for index, video in enumerate(videos, start=1): # add the indexing in the data with help of we can decided ,which video we have to delete
        print(f"{index}. {video['name']} , Duration: {video['time']} ")
    
    print("\n")
    print("*"*70)

def add_video(videos):
    name = input("Enter video name :")
    time = input("Enter video time: ")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update : "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name : ")
        time = input("Enter the new video time : ")
        videos[index-1] = {'name':name, 'time':time}
        save_data_helper(videos)

    else:
        print("Invalid index selected")



def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be delete : "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Successfully deleted")
    else:
        print("Invalid video index selectd")



def main():
    videos = load_data()  
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        #print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":  
    main()