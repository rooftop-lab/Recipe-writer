import os
import urllib.request
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
    HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

def ensure_font():
    font_path = "NotoSansTamil.ttf"
    if not os.path.exists(font_path):
        url = "https://raw.githubusercontent.com/google/fonts/main/ofl/notosanstamil/NotoSansTamil%5Bwdth%2Cwght%5D.ttf"
        urllib.request.urlretrieve(url, font_path)
    pdfmetrics.registerFont(TTFont("NotoSansTamil", font_path))

def create_recipe_pdf(output_filename="travel_premix_recipes_bilingual.pdf"):
    ensure_font()

    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Title"],
        fontName="NotoSansTamil",
        fontSize=20,
        leading=26,
        textColor=colors.HexColor("#1A365D"),
        alignment=1,
        spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        "DocSubTitle",
        parent=styles["Normal"],
        fontName="NotoSansTamil",
        fontSize=11,
        leading=16,
        textColor=colors.HexColor("#4A5568"),
        alignment=1,
        spaceAfter=15
    )

    h2_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontName="NotoSansTamil",
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#2B6CB0"),
        spaceBefore=12,
        spaceAfter=8
    )

    th_style = ParagraphStyle(
        "TableHeader",
        parent=styles["Normal"],
        fontName="NotoSansTamil",
        fontSize=10,
        leading=13,
        fontStyle="bold",
        textColor=colors.white,
        alignment=0
    )

    cell_en_style = ParagraphStyle(
        "TableCellEn",
        parent=styles["Normal"],
        fontName="NotoSansTamil",
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#2D3748")
    )

    cell_ta_style = ParagraphStyle(
        "TableCellTa",
        parent=styles["Normal"],
        fontName="NotoSansTamil",
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#1A202C")
    )

    story = []

    # Title & Header
    story.append(Paragraph("Travel Premix Recipes / பயணத்திற்கான இன்ஸ்டன்ட் ப்ரீமிக்ஸ் ரெசிபிகள்", title_style))
    story.append(Paragraph("<b>Source Video:</b> Just Add Hot Water - Perfect Travel Premix Recipe Ideas (Hebbar's Kitchen)<br/><b>Format:</b> Bilingual Table (English & Tamil / ஆங்கிலம் மற்றும் தமிழ்)", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#CBD5E0"), spaceAfter=15))

    recipes = [
        {
            "title": "1. Sambar Premix | சாம்பார் ப்ரீமிக்ஸ்",
            "ingredients": [
                ("Toor Dal (துவரம் பருப்பு)", "1 cup / 1 கப்"),
                ("Chana Dal (கடலை பருப்பு)", "2 tbsp / 2 டேபிள் ஸ்பூன்"),
                ("Coriander Seeds (கொத்தமல்லி விதை / தனியா)", "¼ cup / ¼ கப்"),
                ("Cumin Seeds (சீரகம்)", "1 tbsp / 1 டேபிள் ஸ்பூன்"),
                ("Methi Seeds (வெந்தயம்)", "½ tsp / ½ டீஸ்பூன்"),
                ("Dry Red Chillies (காய்ந்த மிளகாய்)", "10-12 / 10-12 எண்ணிக்கை"),
                ("Curry Leaves (கறிவேப்பிலை)", "Few / சிறிதளவு"),
                ("Tamarind (புளி)", "Small marble size / சிறிய நெல்லிக்காய் அளவு"),
                ("Turmeric Powder (மஞ்சள் தூள்)", "½ tsp / ½ டீஸ்பூன்"),
                ("Asafoetida / Hing (பெருங்காயம்)", "½ tsp / ½ டீஸ்பூன்"),
                ("Mustard Seeds (கடுகு)", "1 tsp / 1 டீஸ்பூன்"),
                ("Oil (எண்ணெய்)", "1 tbsp / 1 டேபிள் ஸ்பூன்"),
                ("Salt (உப்பு)", "1 tsp / 1 டீஸ்பூன்")
            ],
            "steps": [
                ("1. Dry roast toor dal and chana dal until golden. Keep aside.", "1. துவரம் பருப்பு மற்றும் கடலை பருப்பை பொன்னிறமாக வறுத்து தனியாக வைக்கவும்."),
                ("2. Dry roast coriander, cumin, methi, red chillies, tamarind and curry leaves until aromatic.", "2. தனியா, சீரகம், வெந்தயம், காய்ந்த மிளகாய், புளி, கறிவேப்பிலையை வாசனை வரும் வரை வறுக்கவும்."),
                ("3. Cool completely and grind to a coarse/fine powder along with turmeric, hing, and salt.", "3. ஆறவைத்து, மஞ்சள் தூள், பெருங்காயம், உப்பு சேர்த்து பொடியாக அரைக்கவும்."),
                ("4. Temper mustard seeds and curry leaves in oil and mix with the powder.", "4. எண்ணெயில் கடுகு, கறிவேப்பிலை தாளித்து பொடியுடன் கலக்கவும்.")
            ],
            "usage": ("Mix 3 tbsp Sambar Premix in 1 cup hot water with boiled veggies or just hot water. Boil for 3-5 mins and serve.", "3 டேபிள் ஸ்பூன் சாம்பார் பொடியை 1 கப் சுடுதண்ணீரில் கலந்து 3-5 நிமிடங்கள் கொதிக்க வைத்து பரிமாறவும்.")
        },
        {
            "title": "2. Instant Dal Premix | இன்ஸ்டன்ட் பருப்பு ப்ரீமிக்ஸ்",
            "ingredients": [
                ("Toor Dal (துவரம் பருப்பு)", "1 cup / 1 கப்"),
                ("Moong Dal (பாசிப் பருப்பு)", "1 cup / 1 கப்"),
                ("Masoor Dal (மைசூர் பருப்பு)", "¾ cup / ¾ கப்"),
                ("Oil (எண்ணெய்)", "2 tbsp / 2 டேபிள் ஸ்பூன்"),
                ("Mustard & Cumin Seeds (கடுகு & சீரகம்)", "2 tsp each / தலா 2 டீஸ்பூன்"),
                ("Hing (பெருங்காயம்)", "¼ tsp / ¼ டீஸ்பூன்"),
                ("Dry Red & Green Chillies (மிளகாய்)", "4 Red, 3 Green / 4 சிவப்பு, 3 பச்சை"),
                ("Curry & Bay Leaves, Kasuri Methi", "Few / சிறிதளவு"),
                ("Spices (Turmeric, Chilli, Coriander, Garam Masala, Amchur, Salt)", "As required / தேவையான அளவு")
            ],
            "steps": [
                ("1. Clean and dry roast toor, moong, and masoor dal until aromatic.", "1. துவரம் பருப்பு, பாசிப் பருப்பு, மைசூர் பருப்பை வாசனை வரும் வரை வறுக்கவும்."),
                ("2. Grind the roasted dals to a fine powder.", "2. வறுத்த பருப்புகளை நைஸாக அரைத்துக் கொள்ளவும்."),
                ("3. Heat oil, splutter mustard, cumin, hing, chillies, bay leaf, kasuri methi.", "3. எண்ணெயில் கடுகு, சீரகம், பெருங்காயம், மிளகாய், கறிவேப்பிலை, கசூரி மேத்தி தாளிக்கவும்."),
                ("4. Add dal powder and all spice powders with salt. Mix and roast on low flame for 2 mins.", "4. பருப்பு பொடி, மசாலா தூள்கள், உப்பு சேர்த்து குறைந்த தீயில் 2 நிமிடங்கள் வறுக்கவும்.")
            ],
            "usage": ("Mix ½ cup Dal Premix with 2 cups hot water. Boil for 5 minutes until thick. Instant Dal is ready!", "½ கப் பருப்பு பொடியுடன் 2 கப் சுடுதண்ணீர் சேர்த்து 5 நிமிடங்கள் கொதிக்க வைக்கவும். பருப்பு தயார்!")
        },
        {
            "title": "3. Instant Chutney Premix (Peanut & Coconut) | இன்ஸ்டன்ட் சட்னி ப்ரீமிக்ஸ்",
            "ingredients": [
                ("Peanuts / Desiccated Coconut (வேர்க்கடலை / துருவிய தேங்காய்)", "½ cup Peanut / 1 cup Coconut"),
                ("Roasted Gram / Roasted Chana Dal (பொட்டுக்கடலை)", "1 cup / 1 கப்"),
                ("Dry Red Chillies (காய்ந்த மிளகாய்)", "3-5 / 3-5 எண்ணிக்கை"),
                ("Tamarind (புளி)", "Small piece / சிறிய துண்டு"),
                ("Salt (உப்பு)", "1 tsp / 1 டீஸ்பூன்"),
                ("Tempering: Oil, Mustard, Urad Dal, Curry Leaves", "2 tbsp Oil / 2 டேபிள் ஸ்பூன் எண்ணெய்")
            ],
            "steps": [
                ("1. Dry roast peanuts/coconut, roasted gram, red chillies, and tamarind.", "1. வேர்க்கடலை/தேங்காய், பொட்டுக்கடலை, மிளகாய், புளியை வறுக்கவும்."),
                ("2. Grind coarsely with salt after cooling.", "2. ஆறவைத்து உப்பு சேர்த்து கொரகொரப்பாக அரைக்கவும்."),
                ("3. Heat oil, temper mustard, urad dal, and curry leaves. Mix into the ground powder.", "3. எண்ணெயில் கடுகு, உளுத்தம் பருப்பு, கறிவேப்பிலை தாளித்து பொடியுடன் கலக்கவும்.")
            ],
            "usage": ("Take ¾ cup Chutney Mix, add warm/hot water, mix well and rest for 1 minute before serving.", "¾ கப் சட்னி பொடியில் தேவையான அளவு சுடுதண்ணீர் ஊற்றி நன்கு கலந்து 1 நிமிடம் கழித்து பரிமாறவும்.")
        },
        {
            "title": "4. Lemon Rice Gojju Premix | எலுமிச்சை சாத தொக்கு ப்ரீமிக்ஸ்",
            "ingredients": [
                ("Oil (எண்ணெய்)", "¼ cup / ¼ கப்"),
                ("Peanuts (வேர்க்கடலை)", "½ cup / ½ கப்"),
                ("Mustard, Urad Dal, Chana Dal, Cumin", "1 tbsp Mustard, 2 tbsp Urad/Chana, 1 tbsp Cumin"),
                ("Green Chillies, Ginger, Curry Leaves, Red Chillies", "Fine chopped / பொடியாக நறுக்கியவை"),
                ("Hing, Turmeric Powder, Salt", "¾ tsp Hing, 1 tsp Turmeric, 2 tbsp Salt")
            ],
            "steps": [
                ("1. Heat oil and roast peanuts until crunchy.", "1. எண்ணெயில் வேர்க்கடலையை மொறுமொறுப்பாக வறுக்கவும்."),
                ("2. Add mustard, urad dal, chana dal, cumin, chopped chillies, ginger, and curry leaves. Roast well.", "2. கடுகு, உளுத்தம் பருப்பு, கடலை பருப்பு, சீரகம், மிளகாய், இஞ்சி, கறிவேப்பிலை சேர்த்து வறுக்கவும்."),
                ("3. Turn off flame, add hing, turmeric, and salt. Mix thoroughly.", "3. அடுப்பை அணைத்து பெருங்காயம், மஞ்சள் தூள், உப்பு சேர்த்து கலக்கவும்.")
            ],
            "usage": ("Add 2 tbsp Lemon Rice Gojju and fresh lemon juice to 3 cups warm rice. Mix well for instant Lemon Rice.", "3 கப் சாதத்தில் 2 டேபிள் ஸ்பூன் எலுமிச்சை தொக்கு மற்றும் எலுமிச்சை சாறு சேர்த்து கலக்கவும்.")
        },
        {
            "title": "5. Instant Masala Chai Premix | இன்ஸ்டன்ட் மசாலா டீ ப்ரீமிக்ஸ்",
            "ingredients": [
                ("Cardamom, Cinnamon, Cloves, Black Pepper, Fennel", "1 tsp Cardamom, ½ inch Cinnamon, 1 tsp Cloves, ½ tsp Pepper, 1 tsp Fennel"),
                ("Dry Ginger, Nutmeg (சுக்கு, சாதிக்காய்)", "1 inch Dry Ginger, small nutmeg piece"),
                ("Tea Powder (டீ தூள்)", "½ cup / ½ கப்"),
                ("Milk Powder (பால் பவுடர்)", "1 cup / 1 கப்"),
                ("Sugar (சர்க்கரை)", "½ cup / ½ கப்")
            ],
            "steps": [
                ("1. Dry roast spices until aromatic, cool and grind with tea powder to fine powder.", "1. மசாலா பொருட்களை வறுத்து ஆறவைத்து டீ தூளுடன் நைஸாக அரைக்கவும்."),
                ("2. Sieve the tea spice powder.", "2. டீ மசாலா பொடியை சல்லடையில் சலிக்கவும்."),
                ("3. Grind milk powder and sugar together finely.", "3. பால் பவுடர் மற்றும் சர்க்கரையை ஒன்றாக நைஸாக அரைக்கவும்."),
                ("4. Combine all powders together uniformly and store in airtight jar.", "4. அனைத்து பொடிகளையும் ஒன்றாக கலந்து காற்று புகாத பாட்டிலில் சேமிக்கவும்.")
            ],
            "usage": ("Add 1 tbsp Chai Premix to 1 cup boiling hot water. Stir well, rest 1 minute, filter if desired and enjoy!", "1 கப் சுடுதண்ணீரில் 1 டேபிள் ஸ்பூன் டீ பவுடர் சேர்த்து கலந்து 1 நிமிடம் கழித்து பருகவும்.")
        }
    ]

    for recipe in recipes:
        recipe_story = []
        recipe_story.append(Paragraph(recipe["title"], h2_style))

        # Ingredients Table
        table_data = [
            [Paragraph("<b>Ingredient (ஆங்கிலம்)</b>", th_style), Paragraph("<b>பொருள் & அளவு (Tamil & Quantity)</b>", th_style)]
        ]
        for ing, qty in recipe["ingredients"]:
            table_data.append([
                Paragraph(ing, cell_en_style),
                Paragraph(f"{qty}", cell_ta_style)
            ])

        t_ing = Table(table_data, colWidths=[270, 270])
        t_ing.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2B6CB0")),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F7FAFC"), colors.white])
        ]))
        recipe_story.append(t_ing)
        recipe_story.append(Spacer(1, 8))

        # Steps Table
        steps_data = [
            [Paragraph("<b>Preparation Steps (English)</b>", th_style), Paragraph("<b>செய்முறை விளக்கம் (தமிழ்)</b>", th_style)]
        ]
        for en_step, ta_step in recipe["steps"]:
            steps_data.append([
                Paragraph(en_step, cell_en_style),
                Paragraph(ta_step, cell_ta_style)
            ])

        t_steps = Table(steps_data, colWidths=[270, 270])
        t_steps.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2C5282")),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#EDF2F7"), colors.white])
        ]))
        recipe_story.append(t_steps)
        recipe_story.append(Spacer(1, 8))

        # Usage Table
        usage_data = [
            [Paragraph("<b>How to Prepare / Serving Method</b>", th_style), Paragraph("<b>உபயோகிக்கும் முறை (சுடுதண்ணீர் சேர்க்கும் அளவு)</b>", th_style)],
            [Paragraph(recipe["usage"][0], cell_en_style), Paragraph(recipe["usage"][1], cell_ta_style)]
        ]
        t_usage = Table(usage_data, colWidths=[270, 270])
        t_usage.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#276749")),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
            ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#F0FFF4"))
        ]))
        recipe_story.append(t_usage)
        recipe_story.append(Spacer(1, 15))

        story.append(KeepTogether(recipe_story))

    doc.build(story)
    print(f"Successfully generated {output_filename}")

if __name__ == "__main__":
    create_recipe_pdf()
