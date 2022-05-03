import os
import getpass

def resizeEmote():
    user = getpass.getuser()
    x = 46
    y = 46
    try:
        path = f"/home/{user}/Pictures"
        # Check Directory
        try:
            if not os.path.exists(path):
                os.mkdir(f"{path}")
            elif not os.path.exists(f"{path}/Emotes"):
                os.mkdir(f"{path}/Emotes")
            elif not os.path.exists(f"{path}/Discord-Emotes"):
                os.mkdir(f"{path}/Discord-Emotes")
        except OSError as ose:
            print(f"The creation of the directory failed : {ose}")

        # Resize, delete and make to .gif in needd
        files = os.listdir(f"/home/{user}/Pictures/Emotes")
        for file in files:
            os.system(f"ffmpeg -i {path}/Emotes/{file} -vf scale={x}:{y} {path}/Discord-Emotes/{file}")
            if file[-3:] != "gif":
                fileName = file[-3:]
                os.system(f"mv {path}/Discord-Emotes/{file} {path}/Discord-Emotes/{file}.gif")
            os.remove(f"{path}/Emotes/{file}")
    except Exception as e:
        print(f"There was an error : {e}")

if __name__ == "__main__":
    resizeEmote()    
