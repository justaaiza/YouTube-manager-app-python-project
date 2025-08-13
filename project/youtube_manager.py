
import json

filename = 'youtube.txt'

def load_data():
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data(videos):
    with open(filename, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print('\n')
    print("-"*70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}: {video['time']}")
    print('\n')
    print("-"*70)

def add_video(videos):
    name = input("Enter video title: ")
    time = input("Enter video time: ")
    videos.append({'name':name, 'time':time})
    save_data(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of video you want to update: "))

    if 1<= index <= len(videos):
        print("Choose an option:")
        print("1. for updating the title")
        print("2. for updating the time")
        print("3. for updating both")
        choice = input("Enter the option: ")
        video = videos[index-1]

        match choice:
            case '1':
                newtitle = input("Enter the new title: ")
                video['name'] = newtitle
            case '2':
                newtime = input("Enter new time: ")
                video['time'] = newtime
            case '3':
                newtitle = input("Enter the new title: ")
                newtime = input("Enter new time: ")
                video = {'name':newtitle, 'time':newtime}

    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of video you want to delete: "))

    if 1<= index <= len(videos):
        del videos[index-1]
    else:
        print("Invalid index selected")

def main():

    videos = load_data()
    while True:
        print("\nYoutube manager | Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exist the app")
        choice = input("Enter your choice: ")

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
            case _ :
                print("Invalid input!")

if __name__ == "__main__":
    main()
