
class Camera:
    def take_picture(self):
        import subprocess
        subprocess.run(['raspistill', '-o', '/tmp/picture.jpg', '-t', '1000', '-w', '256', '-h', '256'])

