import pandas as pd
from datetime import datetime

def log_attendance(student_id, student_name):
    try:
        now = datetime.now()
        current_date = now.strftime("%d-%m-%Y")
        current_time = now.strftime("%H:%M:%S")

        data = {'ID': [student_id],
                'Name': [student_name],
                'Date': [current_date],
                'Time': [current_time]}

        df = pd.DataFrame(data)

        # Append to the existing Excel file or create a new one if it doesn't exist
        file_name = 'attendance.xlsx'
        with pd.ExcelWriter(file_name, mode='a' if pd.io.common.file_exists(file_name) else 'w', engine='openpyxl') as writer:
            df.to_excel(writer, index=False, header=not writer.sheets)

    except Exception as e:
        print(f"Error logging attendance: {str(e)}")
