import os
import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
from PIL import Image, ImageTk
from ffpyplayer.player import MediaPlayer

def get_audio_stream(file):
    """ Helper function to sync video with audio """
    return MediaPlayer(file)

class MediaPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ShellOS Media Player Beta")
        self.root.geometry("640x480")

        self.current_file = None
        self.is_video_playing = False
        self.video_cap = None
        self.video_frame_label = None
        self.audio_player = None

        # Creating the user interface
        self.label = tk.Label(root, text="No file selected", relief="sunken", anchor="w")
        self.label.pack(fill="x", padx=10, pady=5)

        self.load_button = tk.Button(root, text="Load", command=self.load_file)
        self.load_button.pack(side="left", padx=10, pady=10)

        self.play_button = tk.Button(root, text="Play", state="disabled", command=self.play)
        self.play_button.pack(side="left", padx=10, pady=10)

        self.pause_button = tk.Button(root, text="Pause", state="disabled", command=self.pause)
        self.pause_button.pack(side="left", padx=10, pady=10)

        self.stop_button = tk.Button(root, text="Stop", state="disabled", command=self.stop)
        self.stop_button.pack(side="left", padx=10, pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Media Files", "*.mp3 *.wav *.mp4 *.avi")])
        if file_path:
            self.current_file = file_path
            self.label.config(text=os.path.basename(file_path))
            self.play_button.config(state="normal")
            self.pause_button.config(state="normal")
            self.stop_button.config(state="normal")
        else:
            messagebox.showerror("Error", "Failed to load file")

    def play(self):
        if self.current_file:
            if self.current_file.endswith(('.mp3', '.wav')):
                # Play audio
                self.play_audio()
            elif self.current_file.endswith(('.mp4', '.avi')):
                # Play video with audio
                self.play_video()

    def play_audio(self):
        self.audio_player = get_audio_stream(self.current_file)
        self.audio_player.set_pause(False)

    def play_video(self):
        self.is_video_playing = True
        self.video_cap = cv2.VideoCapture(self.current_file)
        self.audio_player = get_audio_stream(self.current_file)

        if self.video_frame_label is None:
            self.video_frame_label = tk.Label(self.root)
            self.video_frame_label.pack(fill="both", expand=True)

        def show_frame():
            if self.is_video_playing and self.video_cap.isOpened():
                ret, frame = self.video_cap.read()
                if ret:
                    # Resize the video frame to fit the tkinter window
                    frame = cv2.resize(frame, (self.root.winfo_width(), self.root.winfo_height()))
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img = Image.fromarray(frame)
                    imgtk = ImageTk.PhotoImage(image=img)

                    self.video_frame_label.imgtk = imgtk
                    self.video_frame_label.config(image=imgtk)

                    # Sync video and audio playback
                    audio_frame, val = self.audio_player.get_frame()
                    if val != 'eof' and audio_frame is not None:
                        self.video_frame_label.after(10, show_frame)
                    else:
                        self.video_frame_label.after(10, show_frame)  # Continue showing frames
                else:
                    self.stop()

        # Start showing video frames
        show_frame()

    def pause(self):
        if self.audio_player:
            self.audio_player.set_pause(True)
        self.is_video_playing = False

    def stop(self):
        if self.video_cap is not None:
            self.is_video_playing = False
            self.video_cap.release()
            self.video_frame_label.config(image='')

        if self.audio_player:
            self.audio_player.close()

# Main loop for the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MediaPlayerApp(root)
    root.mainloop()
