import streamlit as st
import pandas as pd

def toilet_feedback_app():
    st.title("Toilet Feedback App")

    # Feedback items
    feedback_items = [
        {"name": "Good Job", "image": "https://simpple-resources.s3.ap-southeast-1.amazonaws.com/feedback-items/October2021/GxlYdyumoDYAIjmSayjc.png"},
        {"name": "Urinal", "image": "https://simpple-resources.s3.ap-southeast-1.amazonaws.com/feedback-items/August2021/VLTmai1Tjl5KKGpKdnKp.png"},
        {"name": "Mirror", "image": "https://simpple-resources.s3.ap-southeast-1.amazonaws.com/feedback-items/August2021/yxd7fYZd4ooTaMxICnQQ.png"},
        {"name": "Basin", "image": "https://simpple-resources.s3.ap-southeast-1.amazonaws.com/feedback-items/August2021/dg88RUaKf0ywy921KeBy.png"},
        {"name": "Litter Bin", "image": "https://simpple-resources.s3.ap-southeast-1.amazonaws.com/feedback-items/August2021/eMQDTjnf48vRbZ2TuSm8.png"},
        {"name": "Floor", "image": "https://simpple-resources.s3.ap-southeast-1.amazonaws.com/feedback-items/August2021/XJMqgHyiuK9hh4zdBed0.png"},
        {"name": "Smell", "image": "https://simpple-resources.s3.ap-southeast-1.amazonaws.com/feedback-items/August2021/vRXzkR43rs6yZ0DsEXMQ.png"},
        {"name": "Soap", "image": "https://simpple-resources.s3.ap-southeast-1.amazonaws.com/feedback-items/August2021/bwjRTWyMrCrYv5Pf8Kln.png"},
        {"name": "Wall", "image": "https://simpple-resources.s3.ap-southeast-1.amazonaws.com/feedback-items/August2021/ExIW908QV3U1JDNMszbt.png"},
        {"name": "Toilet Roll", "image": "https://simpple-resources.s3.ap-southeast-1.amazonaws.com/feedback-items/August2021/pw9jKgwgR8SZHYEFdPM4.png"},
        {"name": "Hand Dryer", "image": "https://simpple-resources.s3.ap-southeast-1.amazonaws.com/feedback-items/January2022/odRzC9x8USQpZbiHhGjm.png"},
        {"name": "Toilet Bowl", "image": "https://simpple-resources.s3.ap-southeast-1.amazonaws.com/feedback-items/August2021/6SuBc6H08atZNnf6mkqY.png"}
    ]

    # Display the checkbox list in a 4x3 grid layout
    num_columns = 4
    num_rows = 3
    grid_items = [feedback_items[i:i + num_columns] for i in range(0, len(feedback_items), num_columns)]

    # Add input fields for name and general feedback
    user_name = st.text_input("Your Name")
    general_feedback = st.text_area("General Feedback")

    selected_feedback = {}

    for row in grid_items:
        cols = st.columns(num_columns)
        for col, item in zip(cols, row):
            # Use HTML tags to wrap the checkbox and image in a box
            col.write(
                f'<div style="border: 2px solid #ccc; padding: 10px; text-align: center;">'
                f'<img src="{item["image"]}" alt="{item["name"]}" width="100" height="100">'
                f'<br>'
                f'<label>{item["name"]}</label>'
                f'</div>',
                unsafe_allow_html=True
            )

            # Store the checkbox state
            selected_feedback[item["name"]] = col.checkbox(item["name"], key=item["name"])

    # Button to submit feedback
    if st.button("Submit Feedback"):
        # Here, you can store the feedback in a database or process it differently

        # Display the feedback data after the user clicks "Submit Feedback"
        st.subheader("Feedback Data Submitted:")

        # Get the list of selected feedback items
        selected_items = [item["name"] for item in feedback_items if selected_feedback.get(item["name"])]

        # Create a DataFrame from the selected feedback data
        feedback_data = {
            "Name": [user_name],
            "General Feedback": [general_feedback],
            "Feedback": [", ".join(selected_items)],
        }
        df = pd.DataFrame(feedback_data)

        # Display the DataFrame
        st.table(df)

        st.success("Feedback submitted successfully!")

if __name__ == "__main__":
    toilet_feedback_app()
