import sqlite3

# Initialize Database
conn = sqlite3.connect('youtube_manager.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        duration TEXT NOT NULL,
        channel TEXT NOT NULL
    )
''')

def list_all_videos():
    print("\n" + "=" * 70)
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("No videos found in the database.")
    for row in rows:
        print(f"ID: {row[0]} | Title: {row[1]} | Duration: {row[2]} | Channel: {row[3]}")
    print("=" * 70)

def add_video():
    title = input("Enter video title: ")
    duration = input("Enter video duration: ")
    channel = input("Enter video channel: ")
    cursor.execute("INSERT INTO videos (title, duration, channel) VALUES (?, ?, ?)", (title, duration, channel))
    conn.commit()
    print("Video added successfully!")

def update_video():
    list_all_videos()
    video_id = input("Enter the ID of the video to update: ")
    new_title = input("Enter new video title: ")
    new_duration = input("Enter new video duration: ")
    new_channel = input("Enter new video channel: ")
    
    cursor.execute("UPDATE videos SET title = ?, duration = ?, channel = ? WHERE id = ?", 
                   (new_title, new_duration, new_channel, video_id))
    conn.commit()
    print("Video updated successfully!")

def delete_video():
    list_all_videos()
    video_id = input("Enter the ID of the video to delete: ")
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    print("Video deleted successfully!")

def main():
    while True:
        print("\n--- YouTube Manager (SQLite3) ---")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1": list_all_videos()
            case "2": add_video()
            case "3": update_video()
            case "4": delete_video()
            case "5": break
            case _: print("Invalid choice:")

    conn.close()

if __name__ == "__main__":
    main()