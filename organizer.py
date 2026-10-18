import os
import shutil

# Yahan apna target folder ka path dein (jise aapne organize karna hai)
# Misal ke taur par Windows ke liye: r"C:\Users\AapkaNaam\Downloads"
# Linux/Mac ke liye: "/home/aapkanaam/Downloads"
TARGET_DIRECTORY = r"C:\Users\abdul\Downloads"  # Isko apne system ke path se replace kar dein

# Extensions ki mapping (Kaun si file kahan jayegi)
DIRECTORIES = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv", ".doc"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Programs": [".exe", ".msi", ".deb", ".sh", ".dmg"]
}

def organize_folder():
    if not os.path.exists(TARGET_DIRECTORY):
        print(f"Error: Diya gaya path nahi mila -> {TARGET_DIRECTORY}")
        return

    print(f"Organization shuru ho rahi hai: {TARGET_DIRECTORY}")
    
    # Folder ki files ko read karein
    for filename in os.listdir(TARGET_DIRECTORY):
        file_path = os.path.join(TARGET_DIRECTORY, filename)
        
        # Agar yeh khud ek folder hai toh isko skip kar dein
        if os.path.isdir(file_path):
            continue
        
        # File ki extension nikalain
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in DIRECTORIES.items():
            if file_ext in extensions:
                category_folder = os.path.join(TARGET_DIRECTORY, category)
                
                # Agar category folder nahi hai toh bana dein
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                    
                dest_path = os.path.join(category_folder, filename)
                shutil.move(file_path, dest_path)
                print(f"Moved: {filename} ---> {category}/")
                moved = True
                break
        
        # Agar koi extension match na kare toh 'Others' folder mein dal dein
        if not moved:
            other_folder = os.path.join(TARGET_DIRECTORY, "Others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved to Others: {filename}")

    print("Task Complete! Aapka folder organize ho gaya hai.")

if __name__ == "__main__":
    organize_folder()