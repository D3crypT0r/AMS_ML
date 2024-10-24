import cv2
import pandas as pd

# Load the dataset containing IDs (CSV format)
# The dataset should have a column named 'ID' for matching purposes
dataset_path = 'R:\AMS\student_data.csv'  # Change this to your actual dataset path
attendance_data = pd.read_csv(dataset_path)

def scan_qr_code():
    # Create a QRCodeDetector object
    detector = cv2.QRCodeDetector()

    # Start capturing video from the camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image from camera")
            break

        # Detect and decode the QR code
        data, bbox, _ = detector.detectAndDecode(frame)

        # Draw the bounding box around the detected QR code
        if bbox is not None:
            # Ensure bbox has 4 points
            if bbox.shape[0] == 4:
                for i in range(len(bbox)):
                    cv2.line(frame, tuple(bbox[i][0]), tuple(bbox[(i + 1) % 4][0]), (0, 255, 0), 2)

            # Check if data is not empty
            if data:
                print("Scanned QR Code Data:", data)

                # Check attendance against the dataset
                if check_attendance(data):
                    print(f"Attendance marked for ID: {data}")
                else:
                    print(f"ID: {data} not found in attendance records.")

        else:
            print("No QR code found.")

        # Display the frame
        cv2.imshow('QR Code Scanner', frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

def check_attendance(qr_id):
    """Check if the scanned QR ID exists in the attendance dataset."""
    # Check if the ID exists in the 'ID' column of the dataframe
    if qr_id in attendance_data['ID'].values:
        return True
    return False

if __name__ == "__main__":
    scan_qr_code()
