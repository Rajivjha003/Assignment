import streamlit as st
import pandas as pd

# Load data and perform Task 1
@st.cache_data
def task_1_output():
    return pd.read_csv("E:/Assignment/data/task1_output.csv")

# Load data and perform Task 2
@st.cache_data
def task_2_output():
    return pd.read_csv("E:/Assignment/data/task2_output.csv")

# Load data and perform Task 3.1
@st.cache_data
def task_3_output():
    return pd.read_csv("E:/Assignment/data/task3_subtask1_output.csv")

# Load data and perform Task 3.2
@st.cache_data
def task_3_output1():
    return pd.read_csv("E:/Assignment/data/task3_subtask2_output.csv")

# Streamlit App
def main():
    st.title('Data Analysis Tasks')

    tasks = {
        'Task 1': task_1_output,
        'Task 2': task_2_output,
        'Task 3.1': task_3_output,
        'Task 3.2': task_3_output1,
    }

    task = st.sidebar.selectbox('Select Task', list(tasks.keys()))

    st.header(task)

    task_output = tasks[task]()
    st.write(task_output)

if __name__ == '__main__':
    main()
