# Language Bridge App

The Language Bridge App is a Streamlit application designed to assist Indian students in translating their notes from English into multiple Indian languages. The app supports various file formats, including txt, docx, pdf, and pptx. It utilizes Azure services, specifically App Services: Web app and Cognitive Services: Translator, to provide seamless translation capabilities.

[Project Link]()

[Project Demo Link]()

## Features

- File Upload: Users can upload their English notes in txt, docx, pdf, or pptx formats.
- Language Selection: Users can choose the target language for translation from a list of available options, including Assamese, Hindi, Marathi, Tamil, and Telugu.
- Translation: The uploaded notes are automatically translated into the selected language using the Cognitive Services Translator API.
- Text Display: The translated text is displayed within the app, allowing users to review and verify the accuracy of the translation.
- Download as TXT: Users have the option to download the translated text as a TXT file for offline usage.

## Azure Services

The Language Bridge App utilizes the following Azure services:

- *App Services: Web app*: Provides the hosting infrastructure for the Streamlit application.
- *Cognitive Services: Translator*: Powers the translation functionality by leveraging the Translator API to translate the uploaded notes into the desired language.

## Python Packages

The Language Bridge App relies on the following Python packages:

- *requests*: Enables HTTP requests to interact with the Cognitive Services Translator API.
- *uuid*: Generates unique identifiers for tracking API requests.
- *streamlit*: Facilitates the creation of the web application interface and interactive elements.
- *docx2txt*: Extracts text from docx files for translation.
- *re*: Provides regular expression capabilities for text processing and formatting.
- *pdfplumber*: Extracts text from PDF files for translation.
- *pptx*: Extracts text from PowerPoint (PPTX) files for translation.

## Screenshots
