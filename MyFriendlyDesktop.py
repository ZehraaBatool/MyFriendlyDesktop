import cv2
import time
from deepface import DeepFace
import ctypes
from tkinter import Tk, PhotoImage, Label
from random import choice
import pathlib
class MoodAnalyzer:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.video = cv2.VideoCapture(0)
        self.timeout = time.time() + 10
        self.most_common_mood = ''

    def detect_mood(self):
        mood_list = []
        while self.video.isOpened() and time.time() < self.timeout:
            _, frame = self.video.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.04, minNeighbors=6)
            mood = None
            for x, y, w, h in faces:
                image = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                try:
                    analyze = DeepFace.analyze(frame, actions=['emotion'])
                    mood = analyze['dominant_emotion']
                except:
                    print("No Face detected")

            if mood:  # Check if mood is not None before appending to the list
                mood_list.append(mood)
            cv2.imshow("video", frame)
            cv2.waitKey(1)
            print(mood_list)
        if mood_list:  # Check if mood_list is not empty before calling max()
            self.most_common_mood = max(mood_list, key=mood_list.count)
            print("MOST COMMON EMOTION : ", self.most_common_mood)
        else:
            print("No emotions detected.")

    def set_wallpaper_and_display_quote(most_common, frame_path, image_paths, quote_category):
        if image_paths and len(image_paths) > 0:
            # Set wallpaper
            wallpaper_path = str(choice(image_paths))
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 3)

            # Create the Tkinter window
            m = Tk(className='Your mood today')
            m_width, m_height = 1107, 673
            screen_width, screen_height = m.winfo_screenwidth(), m.winfo_screenheight()
            x, y = (screen_width / 2) - (m_width / 2), (screen_height / 2) - (m_height / 2)
            m.geometry("%dx%d+%d+%d" % (m_width, m_height, x, y))
            m.resizable(False, False)

            # Set frame photo
            frame_photo = PhotoImage(file=frame_path)
            frame_label = Label(m, border=0, image=frame_photo)
            frame_label.pack()

            # Display "CoderaXia"
            Label(m, text="Codera", fg='black', bg='white', font=("Game of Squids", 10, "italic")).place(x=855, y=68)
            Label(m, text="X", fg='red', bg='white', font=("Game of Squids", 17, " italic")).place(x=923, y=63)
            Label(m, text="ia", fg='black', bg='white', font=("Game of Squids", 10, "italic")).place(x=945, y=68)

        # Display quote
            quote = choice(quote_category)
            Label(m, text="\t\t\tHEY THERE!!", fg='black', bg='white',
            font=("Lexend", 14)).place(x=131, y=355)
            Label(m, text=quote, fg='black', bg='white', font=("Lexend", 14, "italic")).place(x=120, y=429)
            m.mainloop()

happy_images = [pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\happy1.jpg'),
                pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\happy2.jpg'),
                pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\happy3.jpg'),
                pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\happy4.jpg'),
                pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\happy5.jpg')]

sad_images = [pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\sad1.png'),
              pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\sad2.png'),
              pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\sad3.jpg'),
              pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\sad4.jpg'),
              pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\sad5.png')]

fear_images = [pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\fear1.png'),
               pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\fear2.jpg'),
               pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\fear3.jpg'),
               pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\fear4.jpg')]

disgust_images = [pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\disgusting.png')]

surprise_images = [pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\surprise1.jpg'),
                   pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\surprise2.jpg'),
                   pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\surprise3.jpg')]

angry_images = [pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\angry1.png'),
                pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\angry2.jpg')]

neutral_images = [pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\neutral1.jpg'),
                  pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\neutral2.jfif'),
                  pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\neutral3.jpg'),
                  pathlib.Path('C:\\Users\\lenovo\\Desktop\\Wallpapers\\neutral4.png')]

frame_happy = pathlib.Path('C:\\Users\\lenovo\\Desktop\\GUIs\\frame happy.png')
frame_sad = pathlib.Path('C:\\Users\\lenovo\\Desktop\\GUIs\\frame sad.png')
frame_fear = pathlib.Path('C:\\Users\\lenovo\\Desktop\\GUIs\\frame fear.png')
frame_disgust = pathlib.Path('C:\\Users\\lenovo\\Desktop\\GUIs\\frame disgust.png')
frame_surprise = pathlib.Path('C:\\Users\\lenovo\\Desktop\\GUIs\\frame surprise.png')
frame_angry = pathlib.Path('C:\\Users\\lenovo\\Desktop\\GUIs\\frame angry.png')
frame_neutral = pathlib.Path('C:\\Users\\lenovo\\Desktop\\GUIs\\frame neutral.png')

happy_quotes = ["\t\tHappiness depends upon your own self", "\t\tThe only joy in the world is to begin",
                "\t\tOptimism is a happiness magnet. If you stay positive,\n good things and"
                "good people will be drawn to you.", "\t\tTrue happiness is…to enjoy the present", "\t\tSuccess is not the key"
                " to happiness.\n Happiness is the key to success.","\t\tHappiness consists of living each day as if it were the first\n"
                "day of your honeymoon and the last day of your vacation.","\t\tSometimes your joy is the source of your smile,\n"
                "but sometimes your smile can be the source of your joy."]
sad_quotes = ["\t\tSadness flies away on the wings of time.", "\t\tBe strong now because things will get better.",
              "\t\tIt might be stormy now, but it can’t rain forever", "\t\tyou’re stronger than anything life throws \nyour"
                "way.", "\t\tYou will find your courage eventually.\n Don’t give up on yourself just yet."]
fear_quotes = ["\t\tWhat is needed, rather than running away or controlling\n "
               "or suppressing or any other resistance,\n is understanding fear; that means, watch it, learn about it",
               "\t\tCome to terms with this by looking deeply into whatever makes you fearful\n"
               "what are the key elements that get the hairs up on the back of your neck\n'"
               "and then figuring out what you can do about it."]
disgust_quotes = ["\t\tI had forgotten. Disgust shadows desire. \n"
                "Another life is never safely envied.", "\t\tDisgust is often more deeply buried than envy and anger,\n"
                "but it compounds and intensifies the other negative emotions"]
surprise_quotes = ["\t\tOh what has taken you by surprise?!"]
angry_quotes = ["\t\tAnger\nit is a paralyzing emotion ...it is helpless ... it is absence of control", "\t\tAnger is an acid\n"
                "that can do more harm to the vessel\n in which it is stored than to anything on which it is poured.”\n'"]
neutral_quotes = ["\t\tLearn as if you will live forever, live like you will die\n tomorrow.",
                  "\t\tIt is only when we take chances, when our lives improve.\n "
                  "The initial and the most difficult risk that we need to\n "
                  "take is to become honest."]

if __name__ == "__main__":
    mood_analyzer = MoodAnalyzer()
    mood_analyzer.detect_mood()
    pathframe = None
    imagepaths = None
    quotecategory = None
    if mood_analyzer.most_common_mood:
        # Choose the appropriate frame and quotes based on the detected mood
        if mood_analyzer.most_common_mood == "happy":
            pathframe = frame_happy
            imagepaths = happy_images
            quotecategory = happy_quotes
        elif mood_analyzer.most_common_mood == "sad":
            pathframe = frame_sad
            imagepaths = sad_images
            quotecategory = sad_quotes
        elif mood_analyzer.most_common_mood == "fear":
            pathframe = frame_fear
            imagepaths = fear_images
            quotecategory = fear_quotes
        elif mood_analyzer.most_common_mood == "disgust":
            pathframe = frame_disgust
            imagepaths = disgust_images
            quotecategory = disgust_quotes
        elif mood_analyzer.most_common_mood == "neutral":
            pathframe = frame_neutral
            imagepaths = neutral_images
            quotecategory = neutral_quotes
        elif mood_analyzer.most_common_mood == "surprise":
            pathframe = frame_surprise
            imagepaths = surprise_images
            quotecategory = surprise_quotes
        elif mood_analyzer.most_common_mood == "angry":
            pathframe = frame_angry
            imagepaths = angry_images
            quotecategory = angry_quotes
    mood_analyzer.set_wallpaper_and_display_quote(pathframe, imagepaths, quotecategory)