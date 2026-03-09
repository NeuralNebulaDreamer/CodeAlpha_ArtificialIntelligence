

# import cv2
# from ultralytics import YOLO
#
# # load model
# model = YOLO("yolov8n.pt")
#
# # load video
# cap = cv2.VideoCapture("Video.mp4")
#
# while True:
#
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     results = model.track(frame, persist=True)
#
#     annotated = results[0].plot()
#
#     cv2.imshow("Detection + Tracking", annotated)
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()
import streamlit as st
import cv2
import tempfile
import os
from ultralytics import YOLO

st.title("AI Object Detection & Tracking")

uploaded_file = st.file_uploader("Upload Video", type=["mp4","avi","mov","mkv"])

if uploaded_file is not None:

    # keep original extension
    suffix = os.path.splitext(uploaded_file.name)[1]

    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    temp_video.write(uploaded_file.read())
    temp_video.close()

    cap = cv2.VideoCapture(temp_video.name)

    if not cap.isOpened():
        st.error("❌ Could not open video file")
    else:

        model = YOLO("yolov8n.pt")
        frame_window = st.empty()

        while cap.isOpened():

            ret, frame = cap.read()
            if not ret:
                break

            results = model.track(frame, persist=True)
            annotated = results[0].plot()

            annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

            frame_window.image(annotated)

        cap.release()

        st.success("✅ Video processing finished")