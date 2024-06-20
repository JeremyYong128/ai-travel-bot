import agentops
import cohere
import os
import uuid
from dotenv import load_dotenv



load_dotenv()

agentops.init()

co = cohere.Client(os.environ["COHERE_API_KEY"])

conversation_id = str(uuid.uuid4())

query = input("What do you need help with today?\n")

while True:
	if query.lower() == "exit":
		break

	response = co.chat(
		preamble="You are a travel assistant who is passionate about helping users find the best location for their holidays. Guide users in choosing their perfect travel destination. If you are asked to do things that are not related to travel, remind the user that your only purpose is to aid in travel planning.",
		message=query,
		conversation_id=conversation_id
	)

	print(response.text)

	query = input()

agentops.end_session("Success")