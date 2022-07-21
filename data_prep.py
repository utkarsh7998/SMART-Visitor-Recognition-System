#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 00:00:52 2021

@author: sharanya
"""
# TODO face detect
import cv2
import os
import json
from datetime import time
from training import training_knn
import numpy as np
from skimage import io, img_as_ubyte
from skimage import transform as tf
from skimage.transform import rotate

def sheer_image(name, frame_num, sheer_factor, filename,ind=1):
    image = io.imread(filename)
    # Create Afine transform
    afine_tf = tf.AffineTransform(shear=sheer_factor)
    # Apply transform to image data
    modified = tf.warp(image, inverse_map=afine_tf)
    #modified = modified.astype(np.uint8)
    # save the result
    sheer_filename = f"image dataset/{name}/img{frame_num}sheer{ind}.jpg"
    io.imsave(sheer_filename, img_as_ubyte(modified))

def rotate_image(name, frame_num, rotate_factor,filename,ind=1):
    image = io.imread(filename)
    new_pic = rotate(image, rotate_factor)
    #new_pic = new_pic.astype(np.uint8)

    rotate_filename = f"image dataset/{name}/img{frame_num}rotate{ind}.jpg"

    io.imsave(rotate_filename,img_as_ubyte(new_pic))


def capture_and_save_image(name, frame_num, webcam):
    print(f"{name} {frame_num} img")
    ret, frame = webcam.read()
    key = cv2.waitKey(1)

    filename = f"image dataset/{name}/img{frame_num}.jpg"
    if not os.path.exists(f"image dataset/{name}"):
        os.makedirs(f"image dataset/{name}")

    cv2.imwrite(filename=filename, img=frame)

    sheer_image(name, frame_num, 0.1,filename)
    rotate_image(name, frame_num, -5,filename)
    rotate_image(name, frame_num, 5,filename,2)

    return filename




def wait_for_some_time(webcam, text, frame_wait=100):
    for i in range(frame_wait):
        ret, frame = webcam.read()
        cv2.putText(frame, text, (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 3)
        cv2.imshow("cap", frame)
        key = cv2.waitKey(1)


def collect_images(name, num_of_frames=4, unknown=False):
    webcam = cv2.VideoCapture("utkarsh.mp4")
    counter = 0
    frames = 0
    wait_for_some_time(
        webcam, "Starting process to add image to dataset.", 100)
    try:
        while True:

            # Show Frame
            ret, frame = webcam.read()
            cv2.putText(frame, "Please wait while, adding your image to database",
                        (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 3)
            cv2.imshow("cap", frame)
            key = cv2.waitKey(1)
            #
            if key == ord('q'):
                break
            if counter % 40 == 0:
                capture_and_save_image(name, frames, webcam)
                frames += 1

            if frames == num_of_frames:
                wait_for_some_time(
                    webcam, "Image added successfully. Closing now.", 150)
                break

            counter += 1
        print("DONE")
    except Exception as e:
        print("Exception occured", e)
        pass

    print("Turning off camera.")
    webcam.release()
    print("Camera off.")
    print("Program ended.")
    cv2.destroyAllWindows()


def register_person(name, role, start, end):

    json_file = "roles.json"
    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            roles_dict = json.load(f)

    else:
        roles_dict = {}

    roles_dict[name] = [role, start, end]

    with open(json_file, "w") as f:
        json.dump(roles_dict, f)


def process_person(name, role, start_hr, end_hr):

    collect_images(name)
    register_person(name, role, start_hr, end_hr)

    print("Training KNN classifier")
    classifier = training_knn(
        "image dataset", model_dest_path="trained_knn_model.clf", n_neighbors=2)
    print("Training complete!")


def main():
    name = input("Enter Person Name:")
    role = input("Enter person role:")
    print("Enter start hr.")
    start_hr = int(input())
    print("Enter end hr.")
    end_hr = int(input())

    process_person(name, role, start_hr, end_hr)


if __name__ == "__main__":
    main()
