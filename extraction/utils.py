import fitz
import spacy

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Define keywords and phrases for investor insights
KEYWORDS = {
    "growth": ["growth prospects", "market expansion", "future potential", "revenue growth"],
    "changes": ["business change", "strategic shift", "leadership change", "restructuring"],
    "triggers": ["new product launch", "market entry", "regulatory change", "merger", "acquisition"],
    "material_impact": ["material effect", "impact on earnings", "profit growth", "market share"]
}

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page_num in range(pdf.page_count):
            page = pdf[page_num]
            text += page.get_text()
    return text

def find_relevant_sentences(text):
    """Finds sentences containing keywords related to investor insights."""
    doc = nlp(text)
    relevant_sentences = []

    for sentence in doc.sents:
        sentence_text = sentence.text.lower()
        for category, keywords in KEYWORDS.items():
            if any(keyword in sentence_text for keyword in keywords):
                relevant_sentences.append((category, sentence.text.strip()))
                break
    return relevant_sentences

def extract_insights_from_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    insights = find_relevant_sentences(text)
    return [{"category": category, "sentence": sentence} for category, sentence in insights]
