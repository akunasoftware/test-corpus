import re
from pathlib import Path
from urllib.request import Request, urlopen

from markitdown import MarkItDown
from docx import Document


ARXIV_AI_CLASSICS = {
    "1706.03762": "Attention Is All You Need",
    "1810.04805": "BERT",
    "2005.14165": "Language Models are Few-Shot Learners",
    "1409.0473": "Neural Machine Translation by Jointly Learning to Align and Translate",
    "1512.03385": "Deep Residual Learning for Image Recognition",
    "1412.6980": "Adam: A Method for Stochastic Optimization",
    "1312.6114": "Auto-Encoding Variational Bayes",
    "1406.2661": "Generative Adversarial Networks",
    "1503.02531": "Distilling the Knowledge in a Neural Network",
    "1803.05457": "Deep Contextualized Word Representations",
    "1907.11692": "RoBERTa: A Robustly Optimized BERT Pretraining Approach",
    "1909.08053": "ALBERT: A Lite BERT for Self-supervised Learning of Language Representations",
    "1910.10683": "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer",
    "2103.00020": "Learning Transferable Visual Models From Natural Language Supervision",
    "2112.10752": "High-Resolution Image Synthesis with Latent Diffusion Models",
    "2201.11903": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
    "2303.08774": "GPT-4 Technical Report",
}

USER_AGENT = "akuna-test-corpus"


def main():
    output_dir = Path(__file__).parent / "content" / "downloads" / "arxiv"
    converter = MarkItDown()

    for arxiv_id, title in ARXIV_AI_CLASSICS.items():
        download_arxiv_paper(arxiv_id, title, output_dir, converter)


def download_arxiv_paper(
    arxiv_id: str,
    title: str,
    output_dir: Path,
    converter: MarkItDown,
):
    file_stem = f"{arxiv_id.replace('/', '_')}-{slugify(title)}"
    fixture_dir = output_dir / arxiv_id.replace("/", "_")
    fixture_dir.mkdir(parents=True, exist_ok=True)

    pdf_path = fixture_dir / f"{file_stem}.pdf"
    markdown_path = fixture_dir / f"{file_stem}.md"
    docx_path = fixture_dir / f"{file_stem}.docx"

    download_file(f"https://arxiv.org/pdf/{arxiv_id}.pdf", pdf_path)
    convert_pdf_to_markdown(converter, pdf_path, markdown_path)
    convert_markdown_to_docx(markdown_path, docx_path)


def normalize_whitespace(text: str) -> str:
    return " ".join(text.split())


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:120]


def download_file(url: str, file_path: Path):
    if file_path.exists():
        return

    request = Request(url, headers={"User-Agent": USER_AGENT})

    with urlopen(request) as response:
        file_path.write_bytes(response.read())


def convert_pdf_to_markdown(converter: MarkItDown, pdf_path: Path, markdown_path: Path):
    if markdown_path.exists():
        return

    result = converter.convert(pdf_path)
    markdown_path.write_text(result.markdown, encoding="utf-8")


def convert_markdown_to_docx(markdown_path: Path, docx_path: Path):
    if docx_path.exists():
        return

    document = Document()
    markdown = markdown_path.read_text(encoding="utf-8")

    for line in markdown.splitlines():
        paragraph = sanitize_xml_text(line).strip()

        if not paragraph:
            continue

        document.add_paragraph(paragraph)

    document.save(docx_path)


def sanitize_xml_text(text: str) -> str:
    return "".join(character for character in text if is_xml_character(character))


def is_xml_character(character: str) -> bool:
    codepoint = ord(character)

    return (
        codepoint == 0x09
        or codepoint == 0x0A
        or codepoint == 0x0D
        or 0x20 <= codepoint <= 0xD7FF
        or 0xE000 <= codepoint <= 0xFFFD
        or 0x10000 <= codepoint <= 0x10FFFF
    )


if __name__ == "__main__":
    main()
