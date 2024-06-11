# Proposify

Proposify is a powerful Streamlit application designed to help you generate comprehensive Business Requirements Documents or Proposal files. Whether you need a customized document with specific sections or a default template, Proposify makes it easy to create, view, and download your BRDs in text format.

## Tech Stack

* **Python:** Core programming language used for developing the application.

* **Streamlit:** Framework for building the interactive web application.

* **OpenAI API:** Used for generating BRD content using advanced language models.

* **FPDF:** Library for generating PDF files.

* **dotenv:** For managing environment variables securely.

* **langchain-community:** Provides utilities for interacting with OpenAI models.

## Features

- **Customizable BRD Sections**: Select the sections you need from a predefined list to create a tailored BRD.
- **Default BRD Option**: Quickly generate a BRD with default sections for a fast, standardized document.
- **User-Friendly Interface**: Input your requirements through an intuitive text input field.
- **Integration with OpenAI**: Leverages OpenAI's powerful language models to generate detailed and accurate document content.

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- OpenAI API key

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/proposify.git
    cd proposify
    ```

2. **Set Up a Virtual Environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    - Create a `.env` file in the root directory.
    - Add your OpenAI API key to the `.env` file:
        ```ini
        OPENAI_API_KEY=your_openai_api_key
        ```

## Usage

1. **Run the Streamlit Application**:
    ```bash
    streamlit run main.py
    ```

2. **Open the Application**:
    - Usually available at `http://localhost:8501` in your web browser.

3. **Generate Your Business Proposal File**:
    - Select "Customized" to choose specific sections, or "Default" for a standard template.
    - Enter your requirements in the provided text input field.
    - View the generated document and download it as a text file.

### Dependencies

- **Streamlit**: For building the web application interface.
- **OpenAI**: For generating document content using language models.
- **FPDF**: For creating PDF documents.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code adheres to the project's coding standards and includes relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
