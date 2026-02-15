# Prompts Used for Development

This document contains the main prompts used during the development of Workflow Builder Lite.

## Initial Project Setup

```
Create a FastAPI project structure for a workflow builder application that:
- Allows users to create workflows with multiple AI processing steps
- Runs workflows on text input
- Stores workflows and runs in SQLite database
- Has a simple web interface
```

## Database Schema Design

```
Design SQLAlchemy models for:
1. Workflow model with name and steps (stored as JSON)
2. Run model with workflow_id, input_text, and outputs
Include proper relationships and timestamps
```

## LLM Integration

```
Create a Python function that:
- Connects to Groq API
- Takes a text prompt as input
- Returns the LLM response
- Handles errors gracefully
- Uses Llama 3.3 70B model
```

## Workflow Step Prompts

### Clean Text Prompt
```
Clean and normalize the following text by:
- Removing filler words (um, uh, like, you know)
- Fixing grammar and punctuation
- Making it more concise

Text: {input_text}
```

### Summarize Prompt
```
Create a clear 3-4 sentence summary of the following text. 
Focus on the main points and key takeaways:

{input_text}
```

### Extract Key Points Prompt
```
Extract 5-7 bullet points highlighting the most important 
information from this text:

{input_text}
```

### Tag Category Prompt
```
Analyze this text and classify it into ONE category. 
Choose from: Technology, Business, Education, Health, 
Entertainment, Science, Politics, Sports, Lifestyle, Other.

Text: {input_text}

Return ONLY the category name.
```

### Sentiment Analysis Prompt
```
Analyze the sentiment of this text. Provide:
1. Overall sentiment (Positive/Negative/Neutral/Mixed)
2. Confidence level (High/Medium/Low)
3. Brief explanation

Text: {input_text}
```

## API Endpoints

```
Create FastAPI routes for:
1. POST /api/workflows/ - Create new workflow
2. GET /api/workflows/ - List all workflows
3. GET /api/workflows/{id} - Get workflow details
4. POST /api/runs/ - Execute workflow
5. GET /api/runs/history - Get last 5 runs
6. GET /api/status - Health check endpoint
```

## Frontend Development

### Home Page Prompt
```
Create an HTML template for a workflow builder home page that:
- Explains what the app does
- Lists available workflow steps with icons
- Has a clear call-to-action button
- Uses modern, clean design
```

### Workflow Builder UI Prompt
```
Create a workflow builder interface that:
- Has input field for workflow name
- Shows checkboxes for available steps
- Validates that at least one step is selected
- Provides clear success feedback
- Has a clean, card-based design
```

### Run Workflow UI Prompt
```
Create a workflow execution page that:
- Has dropdown to select workflow
- Large textarea for input text
- Shows loading indicator during processing
- Displays each step's output in separate, styled boxes
- Handles empty input validation
```

## Styling & UI

```
Create modern CSS for the workflow builder with:
- Gradient purple background
- White container card with shadow
- Smooth transitions and hover effects
- Responsive design for mobile
- Clean typography
- Button hover animations
```

## Status Page Logic

```
Create a system status endpoint that checks:
1. Backend health (always OK if responding)
2. Database connectivity (try a test query)
3. LLM API key is loaded
4. LLM connection (send test prompt)
Return status for each component
```

## Error Handling

```
Add comprehensive error handling for:
- Missing workflow IDs
- Empty text input
- LLM API failures
- Database connection issues
- Invalid workflow configurations
Return user-friendly error messages
```

## Testing Prompts

```
Write a basic test that:
- Creates a test workflow
- Runs the workflow with sample text
- Verifies output format
- Checks database persistence
```

## Deployment Configuration

```
Create deployment configuration for:
- Render.com web service
- Include start command with uvicorn
- Specify Python version
- List environment variables needed
- Add health check endpoint
```

## Documentation

```
Write a comprehensive README that includes:
- Project overview and features
- Installation instructions
- Usage guide with examples
- Project structure
- Deployment instructions
- API endpoint documentation
```

## Code Optimization

```
Review the following code and suggest improvements for:
- Error handling
- Code organization
- Performance optimization
- Security best practices
- Following Python conventions
```

## UI/UX Improvements

```
Suggest UI improvements for better user experience:
- Better loading indicators
- Input validation feedback
- Success/error messages
- Responsive mobile design
- Accessibility features
```

---

## Notes on Prompt Engineering

### What Worked Well
- Being specific about desired output format
- Providing examples of expected behavior
- Breaking complex tasks into smaller prompts
- Including error handling requirements upfront

### What Needed Refinement
- Initial prompts were too generic
- Had to iterate on UI styling multiple times
- LLM prompts needed testing with real data
- API structure evolved after initial design

### Lessons Learned
1. Start with high-level architecture, then drill down
2. Test LLM prompts with edge cases
3. Request error handling in every prompt
4. Specify exact tech stack and versions
5. Ask for comments and documentation in code