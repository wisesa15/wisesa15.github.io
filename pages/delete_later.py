import requests
import json

# Replace with your Gemini API key
MODEL_NAME = 'gemini-1.5-flash-002' # 'gemini-1.5-flash'
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

# Define the tools and tool_config (if applicable)
TOOLS = [
        {
        "function_declarations": [
            {
  "name": "split_bill",
  "description": "Split user's bill based on extracted expense from user chat.",
  "parameters": {
    "type": "object",
    "properties": {
      "expenses": {
        "type": "array",
        "description": "Array of expenses with details about payers, amounts, discounts, and distribution.",
        "items": {
          "type": "object",
          "properties": {
            "people": {
              "type": "array",
              "description": "List of names of people involved in splitting the bill.",
              "items": {
                "type": "string"
              }
            },
            "expenses": {
              "type": "array",
              "description": "List of individual expenses.",
              "items": {
                "type": "object",
                "properties": {
                  "payer": {
                    "type": "string",
                    "description": "The name of the person who paid for this expense."
                  },
                  "amount": {
                    "type": "integer",
                    "description": "The amount paid for this expense."
                  },
                  "discount": {
                    "type": "integer",
                    "description": "The discount applied to this expense (optional)."
                  },
                  "description": {
                    "type": "string",
                    "description": "A description of the expense."
                  },
                  "distribution": {
                      "type": "array",
                      "description": "The distribution of the expense among people.",
                      "items": {
                          "type": "object",
                          "properties": {
                              "person": {
                                  "type": "string",
                                  "description": "The name of the person."
                              },
                              "share": {
                                  "type": "integer",
                                  "description": "The share of the expense for this person."
                              }
                          },
                          "required": ["person", "share"]
                      }
                  }
                },
                "required": ["payer", "amount", "description", "distribution"]
              }
            }
          },
          "required": ["people", "expenses"]
        }
      }
    },
    "required": ["expenses"]
  }
},
            {
            "name": "response",
            "description": "Use this function when you want to do basic interaction with user without calling any function. e.g. when you want to ask user to fill the parameter needed to call some function. if all the parameters already completed, you didnt need to use this function",
            "parameters": {
                "type": "object",
                "properties": {
                "resp": {
                    "type": "string",
                    "description": "Your response to user"
                }
                },
                "required": [
                "resp"
                ]
            },
            }
        ]
        }
    ]  # Add your tools definition here
TOOLS_CONFIG = TOOLS_CONFIG = {
    "function_calling_config": {
        "mode": "ANY"
    }
} # Add your tool_config here

# System instruction (prompt)
PROMPT = """You are a helpful assistant that gonna help to extract user expenses from their chat. 
If you don't do function calling, only answer user's question in Bahasa Indonesia. """

def generate_response(payload):
    """Send a request to the Gemini API and return the response."""
    headers = {"Content-Type": "application/json"}
    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}.")
    
    return response.json()

def main():
    """Main loop for continuous interaction."""
    while True:
        # Get user input
        message = input("You: ")
        
        # Exit the loop if the user types "exit"
        if message.lower() == "exit":
            print("Goodbye!")
            break
        
        # Define the request payload
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": message},
                    ],
                    "role": "user"
                }
            ],
            "tools": TOOLS,
            "tool_config": TOOLS_CONFIG,
            "system_instruction": {
                "parts": [
                    {"text": PROMPT}
                ]
            }
        }
        
        try:
            # Generate a response
            response = generate_response(payload)
            
            # Extract the answer
            if 'candidates' in response and response['candidates']:
                function_call = response['candidates'][0]['content']['parts'][0].get('functionCall')
                if function_call:
                    print(f"Assistant: {function_call}")
                else:
                    print(f"Assistant: {response['candidates'][0]['content']['parts'][0]['text']}")
            else:
                print("Assistant: No response generated.")
        
        except Exception as e:
            print(f"Error: {e}")

# Run the main loop
if __name__ == "__main__":
    main()