
class Camera:
    def take_picture(self):
        import subprocess
        subprocess.run(['raspistill', '-w', '256', '-h', '256', '-o', '/tmp/picture.jpg'])

# raspistill -o /tmp/picture.jpg -hf -vf -w 256 -h 256 -t 1000

