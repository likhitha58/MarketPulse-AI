from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def create_pdf_report(
    filename,
    result
):

    pdf = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "MarketPulse AI Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"<b>Ticker:</b> {result['ticker']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Recommendation:</b><br/>{result['recommendation']}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>Bull Case</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            result["bull_case"],
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>Bear Case</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            result["bear_case"],
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>Risk Assessment</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            result["risk_report"],
            styles["BodyText"]
        )
    )

    pdf.build(content)