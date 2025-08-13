import sqlite3

con = sqlite3.connect('youtube_videos.db')

cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
            )
''')

def list_all_videos():
    cur.execute("SELECT * FROM videos")
    rows = cur.fetchall()
    if not rows:
        print("No video found")
    else:
        print("\n")
        print("*"*70)
        count = 1
        for row in rows:
            print(f"{count}.  Title: {row[1]},  Duration: {row[2]}")
            count+=1
        print("\n")
        print("*"*70)

def add_video(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(id, name, time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, id))
    con.commit()

def delete_video(id):
    cur.execute("DELETE FROM videos WHERE id = ?", (id,))
    con.commit()

def main():
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
                list_all_videos()
            case '2':
                name = input("Enter video title: ")
                time = input("Enter video time: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter the ID of video you want to update: ") 
                name = input("Enter video title: ")
                time = input("Enter video time: ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter the ID of video you want to delete: ") 
                delete_video(video_id)
            case '5':
                break
            case _ :
                print("Invalid input!")

    con.close()

if __name__ == "__main__":
    main()