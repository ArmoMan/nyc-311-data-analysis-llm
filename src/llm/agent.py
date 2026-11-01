from openai import OpenAI
import json
from src.llm.bridge_tools import get_top_noise_descriptor, get_top_rodent_location, get_slowest_zipcode, get_fastest_zipcode
from dotenv import load_dotenv

class Agent:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI()
        self.input_list = [] # Save conversation history for this agent
        
        self.available_functions = {
            "get_top_noise_descriptor": get_top_noise_descriptor,
            "get_top_rodent_location": get_top_rodent_location,
            "get_slowest_zipcode": get_slowest_zipcode,
            "get_fastest_zipcode": get_fastest_zipcode
        }
        
        # 1. Define a list of callable tools for the model

        self.tools = [
            {
                "type": "function",
                "name": "get_top_noise_descriptor",
                "description": "Find the most common noise complaint descriptor in nyc for a given month of 2024. Returns the month, descriptor name and percentage of all noise complaints that month.",
                "strict": True,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "month": {"type": "integer", "description": "Month number from 1 to 12"}
                    },
                    "required": ["month"],
                    "additionalProperties": False
                }
            },
            {
                "type": "function",
                "name": "get_top_rodent_location",
                "description": "Find the location type with the highest number of reported rodent complaints in nyc in 2024. Returns the location type, number of rodent complaints and percentage of all rodent complaints.",
                "strict": True,
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False
                }
            },
            {
                "type": "function",
                "name": "get_slowest_zipcode",
                "description": "Find the nyc zip code with the slowest average complaint response time for a given month of 2024, based on the complaint closing date. Returns the month, ZIP code and average response time in hours.",
                "strict": True,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "month": {"type": "integer", "description": "Month number from 1 to 12"}
                    },
                    "required": ["month"],
                    "additionalProperties": False
                }
            },
            {
                "type": "function",
                "name": "get_fastest_zipcode",
                "description": "Find the nyc zip code with the fastest average complaint response time for a given month of 2024, based on the complaint closing date. Returns the month, ZIP code and average response time in hours.",
                "strict": True,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "month": {"type": "integer", "description": "Month number from 1 to 12"}
                    },
                    "required": ["month"],
                    "additionalProperties": False
                }
            }
        ]


    def ask(self, question):
        self.input_list.append({"role": "user", "content": question})

        last_answer = ""

        for _ in range(3):
            
            # ask the question to model
            response = self.client.responses.create(
                model="gpt-6-astra",
                instructions="You are an NYC 311 data analysis assistant. Only answer questions related to NYC 311 data using the available tools. If a question is unrelated or cannot be answered using the available data, say that you cannot answer it. Respond in natural language, not raw JSON. Do not invent statistics.",
                tools=self.tools,
                input=self.input_list,
                tool_choice="auto"
            )
            
            # save resp
            self.input_list += response.output 
            
            # check if the model requested a function call and execute it if so
            has_function_call = False

            for item in response.output:
                if item.type == "function_call":
                    has_function_call = True

                    args = json.loads(item.arguments)
                    function = self.available_functions.get(item.name)
                    result = function(**args)

                    # Provide function call results to the model
                    self.input_list.append({
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": json.dumps(result)
                    })

            if response.output_text:
                last_answer = response.output_text
                
            # If no function was requested, return the answer
            if not has_function_call:
                return response.output_text
        
        if last_answer:
            return last_answer + "\nThe maximum number of function calls was reached."
        else:
            return "The maximum number of function calls was reached. No answer."