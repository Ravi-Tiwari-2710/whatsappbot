from IntentClassifier import IntentClassifier 
#from weather import weatherInfo

query = "hi"

#mappings = { }
assistant = IntentClassifier('intents.json',model_name="krishak_guide")
#assistant.train_model()
#assistant.save_model()
assistant.load_model('krishak_guide')
resp = str(assistant.request(query))
print(resp)

