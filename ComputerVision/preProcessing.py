import cv2
import numpy as np

def crop_frame(frame, boundries):
    """
    Crop the frame using the specified boundaries.

    Parameters:
    frame (numpy.ndarray): The input frame to be cropped.
    boundries (dict): A dictionary containing the top, bottom, left, and right boundaries.

    Returns:
    numpy.ndarray: The cropped grayscale frame.
    """
    cropped_frame = frame[boundries['top']:boundries['bottom'], boundries['left']:boundries['right']]
    gray_frame = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2GRAY)

    return gray_frame

def get_frame_ball_position(frame):
    """
    Get the position of the ball in a given frame using computer vision.

    Parameters:
    frame (numpy.ndarray): The input frame.

    Returns:
    tuple: The x and y coordinates of the ball's position.
    """
    pass
    # TODO: apply this model:
    # https://arxiv.org/pdf/2012.09393.pdf
    return x, y

def get_video_ball_boundries(video_path):
    """
    Get the boundaries of the ball in a video.

    Args:
        video_path (str): The path to the video file.

    Returns:
        tuple: A tuple containing the minimum and maximum x and y coordinates of the ball's position.
    """
    max_x, max_y = 0, 0
    min_x, min_y = float('inf'), float('inf')
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        ball_position_x, ball_position_y = get_frame_ball_position
        max_x = max(max_x, ball_position_x)
        max_y = max(max_y, ball_position_y)
        min_x = min(min_x, ball_position_x)
        min_y = min(min_y, ball_position_y)
    cap.release()
    return min_x, max_x, min_y, max_y

# Function to classify the preprocessed frames
def video_to_cropped_frames(video_path):
    """
    Converts a video into a list of cropped frames based on the ball boundaries in the video.

    Args:
        video_path (str): The path to the video file.

    Returns:
        list: A list of cropped frames.

    """
    cropped_frames = []
    min_x, max_x, min_y, max_y = get_video_ball_boundries(video_path)
    boundries = {
            'left': min_x,
            'right': max_x,
            'top': min_y,
            'bottom': max_y
        }
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cropped_frame = crop_frame(frame, boundries)
        cropped_frames.append(cropped_frame)
    cap.release()
    return cropped_frames

def cropped_frames_to_coordinates(cropped_frames):
    """
    Converts a list of cropped frames into a list of coordinates representing the position of the ball in each frame.

    Parameters:
    cropped_frames (list): A list of cropped frames.

    Returns:
    list: A list of coordinates representing the position of the ball in each frame.
    """
    coordinates = []
    for frame in cropped_frames:
        x, y = get_frame_ball_position(frame)
        coordinates.append((x,y))
    return coordinates

def video_to_coordinates(video_path):
    """
    Converts a video file to a list of coordinates.

    Args:
        video_path (str): The path to the video file.

    Returns:
        list: A list of coordinates representing the frames in the video.
    """
    cropped_frames = video_to_cropped_frames(video_path)
    coordinates = cropped_frames_to_coordinates(cropped_frames)
    return coordinates