import subprocess

def play_fullscreen_video(video_path, repeat_count=3):
    for _ in range(repeat_count):
        # Build the command to run GStreamer with video and audio
        cmd = ['gst-launch-1.0', 'playbin', 'uri=file://' + video_path]

        # Run the command
        subprocess.call(cmd)

if __name__ == "__main__":
    video_path = "/home/jetson/Desktop/r2d2/videos/leia-only-hope.mp4"
    repeat_count = 3
    play_fullscreen_video(video_path, repeat_count)
