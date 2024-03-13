import cv2
import mediapipe as mp

def main():
    # Initializing the MediaPipe Hands
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    # Opening the webcam
    cap = cv2.VideoCapture(0)

    # Initializing the hands module
    hands = mp_hands.Hands()

    while True:
        # continuously Reading frame from the webcam
        success, image = cap.read()
        if not success:
            print("Failed to read from webcam. Exiting...")
            break

        # Convert the image to RGB
        # Because the media pipe lib accepts the rgb format
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image to detect hands
        results = hands.process(image_rgb)

        # Convert the image back to BGR
        image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
        #converted the image to bgr because open cv works in bgr foramt

        # For Drawing the landmarks if hands are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image_bgr,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())


        cv2.imshow('MediaPipe Hands', image_bgr)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
