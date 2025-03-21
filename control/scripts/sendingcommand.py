#!/usr/bin/env python3

import speech_recognition as sr
import rospy
from std_msgs.msg import String


def recognize(duration = 3):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Listening for {duration} seconds...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.record(source, duration=duration)

    try:
        text = recognizer.recognize_google(audio)
        print("Command: ", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError:
        print("Check your internet connection.")


if __name__ == "__main__":
    rospy.init_node("speaker_node", anonymous=False)

    pub = rospy.Publisher("command_control", String, queue_size=1)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        str = recognize()
        pub.publish(str)
        rate.sleep()