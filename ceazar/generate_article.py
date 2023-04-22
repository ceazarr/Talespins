
import openai
import base64
import time
import os


# Set up the OpenAI API credentials
openai.api_key = "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"

def generate_text(prompt):
    # Generate text using the OpenAI API
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.7,
    )
    text = response.choices[0].text.strip()
    return text

def generate_article(topic):
    # Generate text for the article sections using OpenAI
    text = generate_text("Applications of " + topic + ":\n")
    applications = text.split("\nEffects of " + topic + ":\n")[0][:250]
    
    text = generate_text("Effects of " + topic + ":\n")
    effects = text.split("\nBenefits of " + topic + ":\n")[0][:250]

    text = generate_text("Benefits of " + topic + ":\n")
    benefits = text[:250]
    
    # Pad the sections with empty lines to have the same number of lines
    max_lines = max(applications.count('\n'), effects.count('\n'), benefits.count('\n'))
    applications += '\n' * (max_lines - applications.count('\n'))
    effects += '\n' * (max_lines - effects.count('\n'))
    benefits += '\n' * (max_lines - benefits.count('\n'))
    
    # Construct the article from the generated sections
    article = "<h2>Applications of " + topic + "</h2>\n"
    article += "<p>" + applications.replace('\n','') + "</p>\n"
    article += "<h2>Effects of " + topic + "</h2>\n"
    article += "<p>" + effects.replace('\n','') + "</p>\n"
    article += "<h2>Benefits of " + topic + "</h2>\n"
    article += "<p>" + benefits.replace('\n','') + "</p>\n"
    
    return article

# #generating images

# openai.api_key = os.getenv("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")



# res = openai.Image.create(
#     prompt=f"{topic}, very render, high resolution",
#     n=3,
#     size="512x512",
#     response_format="b64_json"
#     )

# for i in range(0, len(res['data'])):
#     b64 = res['data'][i]['b64_jason']
#     filename = f'images_{int(time.time())}_{i}.png'
#     print('Saving file' + filename)
#     with open(filename,'wb') as f:
#         f.write(base64.urlsafe_b64decode(b64))

