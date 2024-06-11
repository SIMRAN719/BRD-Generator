from Application.proposal_doc import Required_Document_Generator
import streamlit as st

if __name__ == "__main__":
    st.title('Proposify')

    user_choice = st.radio('Select Document Type', ['Customized', 'Default'])

    if user_choice == 'Customized':
        section_options = ['Introduction', 'Purpose', 'Scope', 'Objectives', 'Stakeholders', 'Business Background',
                           'Overview Of Company', 'Functional Requirements', 'Non-Functional Requirements', 'Assumptions',
                           'Constraints', 'Risks', 'Dependencies', 'Project Timeline', 'Risk Management', 'References',
                           'Conclusion', 'Glossary of terms', 'Appendix', 'Sign-Off']
        
        selected_sections = st.multiselect('Select Sections to Include', section_options)
        document_sections = selected_sections if selected_sections else []

    elif user_choice == 'Default':
        document_sections = 'default'

    requirements_text = st.text_input(placeholder='Enter your requirements here', key='requirements', label='Prompt')

    if requirements_text:
        document_generator = Required_Document_Generator(requirements_text, document_sections)
        generated_document = document_generator.generate_mainfile()
        
        st.write(generated_document)
        
        document_bytes = generated_document.encode('utf-8')

        st.download_button(
            label="Download Document",
            data=document_bytes,
            file_name="generated_document.txt",
            mime="text/plain"
        )
