from Application.brd import BRD_Generator
import streamlit as st
if __name__ == "__main__":
    text = "Face Recognition System"
    result = BRD_Generator(text)
    #print(result.generate_brd())
    st.title('Proposify')
    st.chat_input(placeholder='Requirements...', key='text')
    option = st.sidebar.radio('Select Option', ['BRD', 'Test Cases'])
    if option == 'BRD':
        # st.write(result.generate_brd())
        st.sidebar.title('Upload File')
        st.sidebar.file_uploader('Upload your file ', type=['pdf'])
    elif option == 'Test Cases':
        st.sidebar.title('Upload File')
