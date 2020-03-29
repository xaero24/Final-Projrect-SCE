import time
import picamera

frames = 12

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.framerate = 60
    # Give the camera some warm-up time
    time.sleep(2)
    try:
        while True:
            camera.capture_sequence([
                'image%02d.jpg' % (i+1)
                for i in range(frames)
                ], use_video_port=True)
    except KeyboardInterrupt:
        pass

camera.close()
