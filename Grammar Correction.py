from gingerit.gingerit import GingerIt

# Create a GingerIt parser object
parser = GingerIt()

# Input text with grammar mistakes
text = "I can has cheezburger"

# Parse the text for corrections
result = parser.parse(text)

# Print the corrected text
print(result['result'])
