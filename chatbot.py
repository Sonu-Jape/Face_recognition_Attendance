from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")

        main_frame = Frame(self.root, bd=4, bg='powder blue', width=610)
        main_frame.pack()

        img_chat = Image.open('chat.jpg')
        img_chat = img_chat.resize((200, 70), Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730, image=self.photoimg,
                            text='CHAT ME', font=('arial', 30, 'bold'), fg='green', bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('arial', 14),
                         yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, bd=4, bg='white', width=730)
        btn_frame.pack()

        label_1 = Label(btn_frame, text='Type Something', font=('arial', 14, 'bold'), fg='green', bg='white')
        label_1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=40, font=('arial', 16, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)

        self.send = Button(btn_frame, text="Send>>", font=('arial', 15, 'bold'), width=8, bg='green', command=self.send_message)
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear = Button(btn_frame, text="Clear Data", command=self.clear, font=('arial', 15, 'bold'), width=8, bg='red', fg='white')
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label_11 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), bg='white', fg='red')
        self.label_11.grid(row=1, column=1, padx=5, sticky=W)

        self.entry1.bind("<Return>", self.enter_func)

    def enter_func(self, event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0', END)
        self.entry.set('')

    def send_message(self):
        send = '\t\t\t' + 'You: ' + self.entry.get()
        self.text.insert(END, '\n' + send)
        self.text.yview(END)

        if self.entry.get() == '':
            self.msg = 'Please enter some input'
            self.label_11.config(text=self.msg, fg='red')
        else:
            self.msg = ''
            self.label_11.config(text=self.msg, fg='red')

        response = self.get_bot_response(self.entry.get())
        self.text.insert(END, '\n\n' + 'Bot: ' + response)

    def get_bot_response(self, message):
        if message.lower() == 'hello':
            return 'Hi'
        elif message.lower() == 'hi':
            return 'Hello'
        elif message.lower() == 'how are you?':
            return 'fine and you'
        elif message.lower() == 'fantastic':
            return 'Nice To Hear'
        elif message.lower() == 'who created you?':
            return 'Deepak'
        elif message.lower() == 'what is your name?':
            return 'Mr. Hacker'
        elif message.lower() == 'bye':
            return 'Thank You For Chatting'
        elif message.lower() == 'can you speak marathi?':
            return "I'm still learning it..."
        elif message.lower() == 'what is machine learning?':
            return 'Machine learning (ML) is the science of developing statistical models and algorithms that computer systems use to perform tasks without explicit instructions. ML relies on patterns and inference'
        elif message.lower() == 'how does face recognition work?':
            return "Facial recognition software uses an image or video to identify a person's face and create a map of their facial features, called a facial signature. This signature includes information like the eyes' location, scars, and other facial differences. The software then compares the facial signature to its database of known faces to determine if it's a match"
        elif message.lower() == 'what is python programming':
            return "Python is a general-purpose programming language that's often used to build websites and software, automate tasks, and analyze data. It's considered one of the easiest programming languages for beginners to learn. Python is widely used in web applications, software development, data science, and machine learning (ML)"
        elif message.lower() == 'what is chatbot?':
            return 'A chatbot is a computer program that simulates human conversation with an end user. Chatbots can be used to perform routine tasks efficiently, allowing people to focus on higher-level activities. Modern chatbots use conversational AI techniques, such as natural language processing (NLP), to understand user questions and automate responses.'
        else:
            return "Sorry I didn't get it"


if __name__ == "__main__":
    root = Tk()
    app = ChatBot(root)
    root.mainloop()
