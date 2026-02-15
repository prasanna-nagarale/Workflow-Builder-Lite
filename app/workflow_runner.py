from app.llm import call_llm

STEP_PROMPTS = {
    "Clean Text": """Clean and normalize the following text by:
- Removing filler words (um, uh, like, you know)
- Fixing grammar and punctuation
- Making it more concise

Text:
{}""",
    
    "Summarize": """Create a clear 3-4 sentence summary of the following text. Focus on the main points and key takeaways:

{}""",
    
    "Extract Key Points": """Extract 5-7 bullet points highlighting the most important information from this text:

{}""",
    
    "Tag Category": """Analyze this text and classify it into ONE category. Choose from: Technology, Business, Education, Health, Entertainment, Science, Politics, Sports, Lifestyle, Other.

Text:
{}

Return ONLY the category name.""",
    
    "Sentiment": """Analyze the sentiment of this text. Provide:
1. Overall sentiment (Positive/Negative/Neutral/Mixed)
2. Confidence level (High/Medium/Low)
3. Brief explanation

Text:
{}"""
}

def run_workflow(steps: list, text: str) -> dict:
    """Execute workflow steps sequentially"""
    outputs = {}
    current_text = text

    for step in steps:
        if step not in STEP_PROMPTS:
            outputs[step] = f"❌ Unknown step: {step}"
            continue
            
        prompt = STEP_PROMPTS[step].format(current_text)
        result = call_llm(prompt)
        outputs[step] = result
        
        # Chain output for next step (except for Tag Category and Sentiment)
        if step not in ["Tag Category", "Sentiment"]:
            current_text = result

    return outputs